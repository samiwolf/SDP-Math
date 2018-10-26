import tkinter
# Lots of tutorials have from tkinter import *, but that is pretty much always a bad idea
from tkinter import ttk
import GameofLife2
import abc


class Window(ttk.Frame):
    """Abstract base class for a popup window"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, parent):
        ''' Constructor '''
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(width=False, height=False)  # Disallows window resizing
        self.validate_notempty = (self.register(self.notEmpty),
                                  '%P')  # Creates Tcl wrapper for python function. %P = new contents of field after the edit.
        self.init_gui()

    @abc.abstractmethod  # Must be overwriten by subclasses
    def init_gui(self):
        '''Initiates GUI of any popup window'''
        pass

    @abc.abstractmethod
    def do_something(self):
        '''Does something that all popup windows need to do'''
        pass

    def notEmpty(self, P):
        '''Validates Entry fields to ensure they aren't empty'''
        if P.strip():
            valid = True
        else:
            print("Error: Field must not be empty.")  # Prints to console
            valid = False
        return valid

    def close_win(self):
        '''Closes window'''
        self.parent.destroy()


class OpenNewWindow(Window):
    """ New popup window """

    def init_gui(self):
        self.parent.title("Enter Details")
        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(3, weight=1)

        # Create Widgets
        self.label_title = ttk.Label(self.parent, text="This sure is a new window!")
        self.contentframe = ttk.Frame(self.parent, relief="sunken")

        self.heightInputLabel = ttk.Label(self.contentframe, text='Height:')
        self.heightInputTest = ttk.Entry(self.contentframe, width=30, validate='focusout',
                                         validatecommand=(self.validate_notempty))
        self.widthInputLabel = ttk.Label(self.contentframe, text='Width:')
        self.widthInputTest = ttk.Entry(self.contentframe, width=30, validate='focusout',
                                        validatecommand=(self.validate_notempty))
        self.sizeInputLabel = ttk.Label(self.contentframe, text='Size:')
        self.sizeInputTest = ttk.Entry(self.contentframe, width=30, validate='focusout',
                                       validatecommand=(self.validate_notempty))

        self.runButton = ttk.Button(self.parent, text='Run', command=self.do_something)
        self.cancelButton = ttk.Button(self.parent, text='Cancel', command=self.close_win)

        # Layout
        self.label_title.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.contentframe.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.heightInputLabel.grid(row=0, column=0)
        self.heightInputTest.grid(row=0, column=1, sticky='w')

        self.widthInputLabel.grid(row=1, column=0)
        self.widthInputTest.grid(row=1, column=1, sticky='w')

        self.sizeInputLabel.grid(row=2, column=0)
        self.sizeInputTest.grid(row=2, column=1, sticky='w')

        self.runButton.grid(row=3, column=0, sticky='e')
        self.cancelButton.grid(row=3, column=1, sticky='e')

        # Padding
        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)

    def do_something(self):
        '''Does something'''
        height = self.heightInputTest.get().strip()
        width = self.widthInputTest.get().strip()
        size = self.sizeInputTest.get().strip()

        if (height is "" or width is "" or size is ""):
            print("Error: Field must not be empty.")

        else:
            # Do things with text
            print(height + width + size)
            GameofLife2.game(int(height), int(width), int(size))
            self.close_win()


class GUI(ttk.Frame):
    """Main GUI class"""

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.init_gui()

    def openwindow(self):
        self.newWindow = tkinter.Toplevel(self.parent)  # Set parent
        OpenNewWindow(self.newWindow)

    def init_gui(self):
        self.parent.title('Test GUI')
        self.parent.geometry("600x400")
        self.grid(column=0, row=0, sticky='nsew')
        self.grid_columnconfigure(0, weight=1)  # Allows column to stretch upon resizing
        self.grid_rowconfigure(0, weight=1)  # Same with row
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.option_add('*tearOff', 'FALSE')  # Disables ability to tear menu bar into own window

        # Create Widgets
        self.btn = ttk.Button(self, text='Game of Life', command=self.openwindow)

        # Layout using grid
        self.btn.grid(row=0, column=0)

        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)


if __name__ == '__main__':
    root = tkinter.Tk()
    OpenNewWindow(root)
    root.mainloop()
