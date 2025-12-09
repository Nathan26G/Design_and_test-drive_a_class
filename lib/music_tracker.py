class Tracks:
    def __init__(self):
        self.music_list = []

    def add_track(self, song):
        self.music_list.append(song)
        
    def list_tracks(self):
        return ', '.join(self.music_list)