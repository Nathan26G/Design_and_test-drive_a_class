# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface


```python
# EXAMPLE

class Tracks:

    def __init__(self):
        # Parameters: nothing 
        # output: nothing 
        # side effects: creates song list

    def add_track(self, song):
        # Parameters: the song that is to be added, a string 
        # output: nothing
        # side effects: adds the parameter to list

    def list_track(self):
        # Parameters: nothing 
        # output: the list items as a string
        # side effects: nothing
```

## 3. Create Examples as Tests



``` python
# EXAMPLE

"""
test_starts_with_no_tracks:
input: tracks = Tracks()
Expected output = empty list, []

"""

"""
test_add_single_track:
input: track.add_track('bohemian rhapsody')
Expected output = ['bohemian rhapsody']

"""

"""
test_add_multiple_tracks:
input: track.add_track('bohemian rhapsody')
       track.add_track('Billie jean')
       track.add_track('weird fishes')
Expected output = ['bohemian rhapsody', 'Billie jean', 'weird fishes']

"""

"""
test_return_after_add_single_track:
input: track.add_track('bohemian rhapsody')
Expected output = 'bohemian rhapsody'

"""

"""
test_return_after_add_multiple_tracks:
input: track.add_track('bohemian rhapsody')
       track.add_track('Billie jean')
       track.add_track('weird fishes')
Expected output = 'bohemian rhapsody, Billie jean, weird fishes'

"""
_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
