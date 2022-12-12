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