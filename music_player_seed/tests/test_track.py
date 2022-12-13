import unittest

from player.music_library import Track

class TestTrack(unittest.TestCase):
    def test_constructs(self):
        Track(1, 2, 3)

    def test_has_correct_data(self):
        t = Track("title", "artist", "file.mp3")
        t2 = Track("title2", "artist2", "file2.mp3")
        self.assertEqual(t.title, "title")
        self.assertEqual(t.artist, "artist")
        self.assertEqual(t.file, "file.mp3")
        self.assertEqual(t2.title, "title2")
        self.assertEqual(t2.artist, "artist2")
        self.assertEqual(t2.file, "file2.mp3")