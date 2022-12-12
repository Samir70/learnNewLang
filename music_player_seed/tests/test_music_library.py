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
