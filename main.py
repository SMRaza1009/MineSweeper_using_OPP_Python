from tkinter import *
import cell
import settings
import utilities


root = Tk()
# Override the settings of the windows
root.configure(bg='black') # Change the background color of the window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') # Giving the size of window to open!
root.title('Minesweeper Game using OOP') # Giving the title to window 
root.resizable(False, False) # We are not allowed to resized the size of window


# Making different frames in the window

top_frame = Frame(root, 
                  bg = 'black', 
                  width = settings.WIDTH, 
                  height=utilities.height_prct(25)
                  )
top_frame.place(x=0, y=0) # x and y works as position of windows

game_title = Label(top_frame,
                   bg='black',
                   fg='white',
                   text ='Minesweeper Game',
                   font=('', 48))

game_title.place(x= utilities.width_prct(25), y=0)

left_frame = Frame(root, 
                  bg = 'black',
                  width = utilities.width_prct(25),
                  height=utilities.height_prct(75)
                  )
left_frame.place(x=0, y=utilities.height_prct(25)) 

center_frame = Frame(root, 
                     bg = 'black',
                     width = utilities.width_prct(75),
                     height = utilities.height_prct(75))

center_frame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = cell.Cell(x, y)
        c1.create_btn_object(center_frame)
        c1.cell_btn_object.grid(
            column=x, row=y, 
        )

# Cell the label from the Cell class
cell.Cell.create_cell_count_label(left_frame)
cell.Cell.cell_count_label_object.place(x=0, y=0)
        
        
#print(cell.Cell.all_)        
cell.Cell.randonmize_mines  ()


# for c in cell.Cell.all_:
#     print(c.is_mine)

        
# Run the window
root.mainloop()