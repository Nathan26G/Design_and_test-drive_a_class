from lib.music_tracker import *
def test_starts_with_no_tracks():
    tracks = Tracks()
    assert tracks.music_list == []

def test_add_single_track():
    tracks = Tracks()
    tracks.add_track("bohemian rhapsody")
    assert tracks.music_list == ["bohemian rhapsody"]
    
def test_add_multiple_tracks():
    tracks = Tracks()
    tracks.add_track("bohemian rhapsody")
    tracks.add_track("Billie jean")
    tracks.add_track("weird fishes")
    assert tracks.music_list == ['bohemian rhapsody', 'Billie jean', 'weird fishes']
    
def test_return_after_add_single_track():
    tracks = Tracks()
    tracks.add_track("bohemian rhapsody")
    assert tracks.list_tracks() == 'bohemian rhapsody'
    
def test_return_after_add_multiple_tracks():
    tracks = Tracks()
    tracks.add_track("bohemian rhapsody")
    tracks.add_track("Billie jean")
    tracks.add_track("weird fishes")
    assert tracks.list_tracks() == 'bohemian rhapsody, Billie jean, weird fishes'