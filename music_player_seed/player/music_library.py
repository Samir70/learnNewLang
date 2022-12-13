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

    def search(self, attr_name, search_term):
        # return list(filter(func, self.music_list))
        if attr_name == "all":
            return [track for track in self.music_list if search_term in track.title.lower() or search_term in track.artist.lower() or search_term in track.file.lower()]
        return [track for track in self.music_list if search_term in getattr(track, attr_name).lower()]

class Track():
    def __init__(self, title, artist, file_name):
        self.title = title
        self.artist = artist
        self.file = file_name
