"""Classes for different media types (so far limited to Movie)."""


class Movie(object):
  """Store movie related information."""
  
  def __init__(self, title, story, genre, released, poster, trailer):
    """Inits Movie class with its title, story, genre, release year, poster url and trailer url."""
    self.title = title
    self.story = story
    self.genre = genre
    self.released = released
    self.poster_image_url = poster
    self.trailer_youtube_url = trailer




    
    