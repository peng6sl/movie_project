class MovieInfo():
	""" This class contains the movive information:
	- Titls
	- Summary
	- Poster image url
	- Trailer youtube url"""
	def __init__(self, title, summary, poster_image_url, trailer_youtube_url) :
		self.title = title
		self.summary = summary
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url