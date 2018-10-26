import tkinter
# Lots of tutorials have from tkinter import *, but that is pretty much always a bad idea
from tkinter import ttk
import abc
from miscc import bubble_sort


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
        self.parent.rowconfigure(1, weight=1)

        # Create Widgets
        self.label_title = ttk.Label(self.parent, text="Enter nine values (In form a,b,c...)")
        self.contentframe = ttk.Frame(self.parent, relief="sunken")

        self.heightInputLabel = ttk.Label(self.contentframe, text='Array:')
        self.heightInputTest = ttk.Entry(self.contentframe, width=30, validate='focusout',
                                         validatecommand=(self.validate_notempty))

        self.runButton = ttk.Button(self.parent, text='Run', command=self.do_something)
        self.cancelButton = ttk.Button(self.parent, text='Cancel', command=self.close_win)

        # Layout
        self.label_title.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.contentframe.grid(row=1, column=0, columnspan=2, sticky='nsew')

        self.heightInputLabel.grid(row=0, column=0)
        self.heightInputTest.grid(row=0, column=1, sticky='w')

        self.runButton.grid(row=3, column=0, sticky='e')
        self.cancelButton.grid(row=3, column=1, sticky='e')

        # Padding
        for child in self.parent.winfo_children():
            child.grid_configure(padx=10, pady=5)
        for child in self.contentframe.winfo_children():
            child.grid_configure(padx=5, pady=2)

    def do_something(self):
        '''Does something'''

        ara = str(self.heightInputTest.get().strip())
        print(ara)
        ara = ara.split(',')
        print(ara)
        bubble_sort.run(ara)
        self.close_win()


def run():
    root2 = tkinter.Tk()
    OpenNewWindow(root2)
    root2.mainloop()


run()
