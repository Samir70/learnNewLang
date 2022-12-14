from ui.interface import Interface, ConsoleIO
import subprocess

from os import listdir, getcwd
from os.path import join, isfile
import eyed3


class MyFileSys:
    def __init__(self) -> None:
        self.listdir = listdir
        self.getcwd = getcwd
        self.join = join
        self.is_file = isfile

interface = Interface(ConsoleIO(), subprocess, MyFileSys(), eyed3)
interface.run()
