from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


class FileEditor:
    def __init__(self):
        window = Tk()
        window.title("Simple Text Editor")
        # Create a menu bar
        menu_bar = Menu(window)
        window.config(menu=menu_bar)  # Display the menu bar
        # Create a pull-down menu and add it to the menu bar
        operationMenu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=operationMenu)
        operationMenu.add_command(label="Open",
                                  command=self.openFile)
        operationMenu.add_command(label="Save",
                                  command=self.saveFile)
        # Add a tool bar frame
        frame0 = Frame(window)  # Create and add a frame to window
        frame0.grid(row=1, column=1, sticky=W)

        frame1 = Frame(window)  # Hold editor pane
        frame1.grid(row=2, column=1)
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text = Text(frame1, width=100, height=30,
                         wrap=WORD, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
        window.mainloop()

    def openFile(self):
        filenameforReading = askopenfilename()

        infile = open(filenameforReading, "r")
        self.text.insert(END, infile.read())  # Read all from the file
        infile.close()  # Close the input file open file

    def saveFile(self):
        filenameforWriting = asksaveasfilename()

        outfile = open(filenameforWriting, "w")
        # Write to the file
        outfile.write(self.text.get(1.0, END))
        outfile.close()  # Close the output file


FileEditor()
