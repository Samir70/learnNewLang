import unittest
from unittest.mock import Mock

from player.music_player import MusicPlayer

class TestTrack(unittest.TestCase):
    def test_constructs(self):
        mock_process = Mock()
        MusicPlayer(mock_process)

    def test_plays(self):
        mock_process = Mock()
        mp = MusicPlayer(mock_process)
        mp.play("data/tunes/myfav.wav")
        mock_process.call.assert_called_with(["afplay", "data/tunes/myfav.wav"])