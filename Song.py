import os

class Song:
    def __init__(self, tit, art, yr, gen):
        self.Title = tit
        self.Artist = art
        self.Year = yr
        #self.YearRange = [yr-5, yr+5]
        self.Genre = gen
        #self.Path = path
    
    def print(self):
        songPrint = (self.Title + " " + self.Artist + " " + self.Year + " " + self.Genre)
        return songPrint
    
    def play(self):
        pass