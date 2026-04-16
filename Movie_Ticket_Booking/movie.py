class Movie:
    def __init__(self, title, duration, genre):
        self.title = title
        self.genre = genre
        self.duration = duration  # in minutes

    def __str__(self):
        return f"{self.title} ({self.genre}, {self.duration} mins)"

    def get_duration(self):
        return self.duration
