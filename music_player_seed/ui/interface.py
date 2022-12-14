# Over to you!
# I'm outta here!
# ~Kez xoxo

from player.music_library import MusicLibrary, Track
from player.music_player import MusicPlayer
from player.mp3_loader import Mp3Loader

class Interface:
    def __init__(self, console, subprocess, file_sys, tag_reader):
        self.console = console
        self.music_library = MusicLibrary()
        self.music_player = MusicPlayer(subprocess)
        self.mp3_loader = Mp3Loader(["data", "mp3s"], tag_reader, file_sys)

    def run(self):
        self.console.print("Welcome to your music library!")
        self.mp3_loader.get_files()
        for track in self.mp3_loader.file_data:
            # self.console.print("Found a track:")
            # self.console.print(track["title"])
            # self.console.print(track["artist"])
            # self.console.print(track["file"])
            # self.console.print("")
            self.music_library.add(Track(track["title"], track["artist"], track["file"]))
        self.console.print(f"added {len(self.mp3_loader.file_data)} tracks")

        while True:
            choice = self._prompt()
            if choice == "a":
                self._add_track()
            elif choice == "p":
                self._play_track()
            elif choice == "d":
                self._remove_track()
            elif choice == "l":
                self._list_tracks(self.music_library.all())
            elif choice == "s":
                self._search_tracks()
            elif choice == "q":
                return
            else:
                self.console.print("No such command! Try again.")

    def _prompt(self):
        self.console.print("Enter:")
        self.console.print("  a: to add a track")
        self.console.print("  p: to play a track")
        self.console.print("  d: to delete a track")
        self.console.print("  l: to list your tracks")
        self.console.print("  s: to search your tracks")
        self.console.print("  q: to quit")
        return self.console.input("What do you pick? ")

    def _add_track(self):
        title = self.console.input("What's the title? ")
        artist = self.console.input("What's the artist? ")
        file = self.console.input("What's the file? ")
        self.music_library.add(Track(title, artist, file))
        self.console.print("Added successfully.")

    def _list_tracks(self, tracks):
        for idx, track in enumerate(tracks):
            self.console.print(
                f"{idx + 1}. {track}"
            )

    def _search_tracks(self):
        self.console.print("Search by:")
        self.console.print("  t: title")
        self.console.print("  a: artist")
        self.console.print("  f: file")
        self.console.print("  *: anything")
        choice = self.console.input("What do you want to search by? ")
        search_term = self.console.input("What do you want to search for? ").lower()
        attribute_name = {
            "t": "title",
            "a": "artist",
            "f": "file",
            "*": "all"
        }[choice]
        found = self.music_library.search(attribute_name, search_term)
        self._list_tracks(found)
        return found
        # if choice == "t":
        #     # DONE: Find tracks by title
        #     found = self.music_library.search(
        #         lambda track: search_term in track.title.lower())
        #     self._list_tracks(found)
        # elif choice == "a":
        #     # DONE: Find tracks by artist
        #     found = self.music_library.search(
        #         lambda track: search_term in track.artist.lower())
        #     self._list_tracks(found)
        # elif choice == "f":
        #     # DONE: Find tracks by file
        #     found = self.music_library.search(
        #         lambda track: search_term in track.file.lower())
        #     self._list_tracks(found)
        # elif choice == "*":
        #     # DONE: Find tracks by any field
        #     found = self.music_library.search(
        #         lambda track: search_term in track.title.lower() or search_term in track.artist.lower() or search_term in track.file.lower()
        #     )
        #     self._list_tracks(found)
        # else:
        #     self.console.print("No such field!")

    def _play_track(self):
        tracks = self._search_tracks()
        # tracks = self.music_library.all()
        track_id = int(self.console.input("Which do you want to play? ")) - 1
        if track_id >= 0 and track_id < len(tracks):
            track = tracks[track_id]
            t_str = f"{track}".split(" @")[0]
            self.console.print(f"Playing {t_str}...")
            self.music_player.play(track.file)
            self.console.print("Done.")
        else:
            self.console.print("No such track.")

    def _remove_track(self):
        self._list_tracks(self.music_library.all())
        track_id = int(self.console.input("Which do you want to delete? ")) - 1
        if self.music_library.remove(track_id):
            self.console.print("Deleted successfully.")
        else:
            self.console.print("No such track.")


class ConsoleIO:
    def print(self, message):
        print(message)

    def input(self, prompt=None):
        if prompt is None:
            return input()
        return input(prompt)
