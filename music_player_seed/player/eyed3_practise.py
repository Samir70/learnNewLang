import eyed3
from os import listdir, getcwd
from os.path import isfile, join

# print(getcwd())
path = join(getcwd(), "data", "mp3s")
# print(path)
files = [f for f in listdir(path) if f.endswith("mp3") and isfile(join(path, f))]

for f in files:
    audio = eyed3.load(join(path, f))
    print("Found a file:")
    print(audio.tag.title)
    print(audio.tag.artist)
    print(audio.tag.genre)
    print()
