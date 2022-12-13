class MusicLibrary:
    def __init__(self):
        self.music_list = []

    def all(self):
        return self.music_list

    def add(self, title):
        self.music_list.append(title)

    def remove(self, id):
        if id >= len(self.music_list):
            return False
        self.music_list.remove(self.music_list[id])
        return True

class Track():
    def __init__(self, title, artist, file_name):
        self.title = title
        self.artist = artist
        self.file = file_name