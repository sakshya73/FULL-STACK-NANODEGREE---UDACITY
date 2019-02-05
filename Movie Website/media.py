""" class Movie initializes the instances when media.movie() is called
 and initializes the attributes when its constructor is called."""


class Movie:
    """ special function which is called when instance of class Movie is created.
     constructor of the class."""
    def __init__(self, title, story, boxArt, trailer):
        self.title = title
        self.storyline = story
        self.poster_image_url = boxArt
        self.trailer_youtube_url = trailer
