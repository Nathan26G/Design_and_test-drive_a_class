from lib.music_tracker import *
def test_starts_with_no_tracks():
    tracks = Tracks()
    assert tracks.music_list == []

def test_add_single_track():
    tracks = Tracks()
    tracks.add_track("bohemian rhapsody")
    assert tracks.music_list == ["bohemian rhapsody"]