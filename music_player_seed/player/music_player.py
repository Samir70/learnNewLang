import subprocess

class MusicPlayer():
    def __init__(self, subP):
        self.subP = subP
    def play(self, file_name):
        self.subP.call(["afplay", file_name])

# player = MusicPlayer(subprocess) 
#  #                    ^^^^^^^^^^
#  # We'll need to pass in (inject) `subprocess`
#  # in order to isolate our tests.
# player.play("./player/data/tunes/myfav.wav")
#  # A pause while it plays the file.
