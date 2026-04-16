from datetime import datetime

from .movie import Movie
from .room import Room

class Screening:
    count = 0
    def __init__(self, movie: Movie, room: Room, start_time: datetime, end_time: datetime):
        self.id = Screening.count + 1
        self.movie = movie
        self.room = room
        self.start_time = start_time
        self.end_time = end_time
        
        Screening.count+=1
    
    def get_duration(self):
        return (self.end_time - self.start_time).total_seconds() / 60


    def get_movie(self):
        return self.movie
    

    def get_room(self):
        return self.room
    
    def get_id(self):
        return self.id