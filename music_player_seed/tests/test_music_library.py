import unittest

from player.music_library import MusicLibrary, Track


class TestMusicLibrary(unittest.TestCase):
    def test_constructs(self):
        MusicLibrary()

    def test_lists_all(self):
        ml = MusicLibrary()
        self.assertEqual(ml.all(), [])

    def test_adds_an_album(self):
        ml = MusicLibrary()
        t1 = Track("Seventh Son of a Seventh Son", "Iron Maiden", "7th.mp3")
        ml.add(t1)
        self.assertEqual(ml.all(), [t1])

    def test_adds_3_albums(self):
        ml = MusicLibrary()
        t1 = Track("Seventh Son of a Seventh Son", "Iron Maiden", "7th.mp3")
        t2 = Track("Sixth Son of a Sixth Son", "Iron Maiden", "6th.mp3")
        t3 = Track("Fifth Son of a Fifth Son", "Iron Maiden", "5th.mp3")
        ml.add(t1)
        ml.add(t2)
        ml.add(t3)
        self.assertEqual(ml.all(), [t1, t2, t3])

    def test_deletes_an_album(self):
        ml = MusicLibrary()
        t1 = Track("Seventh Son of a Seventh Son", "Iron Maiden", "7th.mp3")
        t2 = Track("Sixth Son of a Sixth Son", "Iron Maiden", "6th.mp3")
        t3 = Track("Fifth Son of a Fifth Son", "Iron Maiden", "5th.mp3")
        ml.add(t1)
        ml.add(t2)
        ml.add(t3)
        self.assertEqual(ml.remove(1), True)
        self.assertEqual(ml.all(), [t1, t3])

    def test_reports_unable_to_delete_album(self):
        ml = MusicLibrary()
        t1 = Track("Seventh Son of a Seventh Son", "Iron Maiden", "7th.mp3")
        t2 = Track("Sixth Son of a Sixth Son", "Iron Maiden", "6th.mp3")
        t3 = Track("Fifth Son of a Fifth Son", "Iron Maiden", "5th.mp3")
        ml.add(t1)
        ml.add(t2)
        ml.add(t3)
        self.assertEqual(ml.remove(10), False)
        self.assertEqual(ml.all(), [t1, t2, t3])