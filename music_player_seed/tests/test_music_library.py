import unittest

from player.music_library import MusicLibrary


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_lists_all(self):
        ml = MusicLibrary()
        self.assertEqual(ml.all(), [])

    def test_adds_an_album(self):
        ml = MusicLibrary()
        ml.add("Seventh Son of a Seventh Son")
        self.assertEqual(ml.all(), ["Seventh Son of a Seventh Son"])

    def test_adds_3_albums(self):
        ml = MusicLibrary()
        ml.add("Seventh Son of a Seventh Son")
        ml.add("album 2")
        ml.add("album 3")
        self.assertEqual(ml.all(), ["Seventh Son of a Seventh Son", "album 2", "album 3"])

    def test_deletes_an_album(self):
        ml = MusicLibrary()
        ml.add("Seventh Son of a Seventh Son")
        ml.add("album 2")
        ml.add("album 3")
        self.assertEqual(ml.remove(1), True)
        self.assertEqual(ml.all(), ["Seventh Son of a Seventh Son", "album 3"])
    def test_reports_unable_to_delete_album(self):
        ml = MusicLibrary()
        ml.add("Seventh Son of a Seventh Son")
        ml.add("album 2")
        ml.add("album 3")
        self.assertEqual(ml.remove(10), False)
        self.assertEqual(ml.all(), ["Seventh Son of a Seventh Son", "album 2", "album 3"])