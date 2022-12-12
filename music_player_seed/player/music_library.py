class MusicLibrary:
    def __init__(self):
        self.music_list = []

    def all(self):
        return self.music_list

    def add(self, title):
        self.music_list.append(title)