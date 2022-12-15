from os import listdir, getcwd
from os.path import join, isfile
import eyed3
import subprocess
from gui.gui import GUI

class MyFileSys:
    def __init__(self) -> None:
        self.listdir = listdir
        self.getcwd = getcwd
        self.join = join
        self.is_file = isfile

interface = GUI(subprocess, MyFileSys(), eyed3)
interface.run()