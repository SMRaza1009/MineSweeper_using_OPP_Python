from tkinter import Button, Label
import random
import settings
import ctypes # A library that handle any kind errors of things to come up with them 
import sys

class Cell:
    all_ = []
    cell_count = settings.CELL_COUNT
    cell_count_label = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False # a boolean type of variable that we can set vy default to false. 
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y =y
        
    # Append the object to the Cell.all_ list
        Cell.all_.append(self)
    
    def create_btn_object(self,location):
        btn = Button(
            location,
            width = 12,
            height= 4,
            #text = f"{self.x}, {self.y}"
        )
        btn.bind('<Button-1>',self.left_clicked_actions ) # Left Click
        btn.bind('<Button-3>',self.right_clicked_actions ) # Left Click
        self.cell_btn_object = btn    # instance object button 
    
    @staticmethod #a static method is just for use case of the class and not for the use case of the instance.     
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = "black",
            fg="white",
            text=f"Cells Left {Cell.cell_count}",
            font=("",30)
        )
        Cell.cell_count_label_object = lbl
        
        
        
    def left_clicked_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cell_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # if mines count is equal to the cells left count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations! You won the gamee', 'Game Over' ,0)
            # Cancel Left and Right clicks events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')
            
    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x, y
        for cell in Cell.all_:
            if cell.x == x and cell.y == y:
                return cell 
    @property # now we can access all the attributes in this propoerty decorators    
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        # To remove None values we use list comprehension because it remove the None values from list comprehension
        # in list comprehension we can use a for loop with if statement
        
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cell_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter +=1
        return counter
    
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -=1
            self.cell_btn_object.configure(text=self.surrounded_cell_mines_length)
            #print(self.surrounded_cell_mines_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left {Cell.cell_count}") 
            
            # If this was a mine candidate, then for safety, we should configure the background color to SystemButtonFace
            self.cell_btn_object.configure(bg = "SystemButtonFace")
                
        # Mark the cell as opened (use is as the last line of this method)
        self.is_opened = True     
        
    def show_mine(self):
        # A logic do interrupt the game and display a message that player has lost game!
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over',0)
        sys.exit()
       
        # print(event) # It will give the exact information about button and its position 
        # print("I am left clicked!")    
    
    def right_clicked_actions(self, event):
        if not self.is_mine_candidate:
           self.cell_btn_object.configure(bg="orange")
        
           self.is_mine_candidate = True 
        else:
            self.cell_btn_object.configure(bg="SystemButtonFace")    
            
            self.is_mine_candidate = False    
        # print(event) # It will give the exact information about button and its position 
        # print("I am right clicked!")        
        
    @staticmethod
    def randonmize_mines():
        picked_cells = random.sample(Cell.all_, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    
    # Defining (overrinding) magic method, to change the way that the object is being represented
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})" 