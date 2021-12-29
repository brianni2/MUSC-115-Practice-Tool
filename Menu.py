import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.font.init()

COLOR_MAINPAN = (85, 85, 85)
COLOR_TAB = (195, 200, 200)
COLOR_FONT = (0, 0, 0)
FONT_TAB = pygame.font.Font(None, 24)

class Mainpanel:
    def __init__(self, WIN):
        self.width = WIN.get_width()*.84            #percentage of screen width
        self.height = WIN.get_height()              #screen height
        self.x = 0                                  #left align
        self.y = 0                                  #top align
        
    def update(self, WIN):
        self.width = WIN.get_width()*.84
        self.height = WIN.get_height()
        self.mainpan = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(WIN, COLOR_MAINPAN, self.mainpan)
        
    def viewSongs(self, WIN):
        tabHeight, tabXOffset = self.height*.04, self.width*.015
        self.tabPlay = pygame.Rect(self.width*.01, 0, self.width*.04, tabHeight)
        self.tabTitle = pygame.Rect(self.tabPlay.right + tabXOffset, 0, self.width*.255, tabHeight)
        self.tabArtist = pygame.Rect(self.tabTitle.right + tabXOffset, 0, self.width*.23, tabHeight)
        self.tabGenre = pygame.Rect(self.tabArtist.right + tabXOffset, 0, self.width*.25, tabHeight)
        self.tabYear = pygame.Rect(self.tabGenre.right + tabXOffset, 0, self.width*.05, tabHeight)
        self.tabRatio = pygame.Rect(self.tabYear.right + tabXOffset, 0, self.width*.05, tabHeight)
            
        pygame.draw.rect(WIN, COLOR_TAB, self.tabPlay)
        pygame.draw.rect(WIN, COLOR_TAB, self.tabTitle)
        pygame.draw.rect(WIN, COLOR_TAB, self.tabArtist)
        pygame.draw.rect(WIN, COLOR_TAB, self.tabGenre)
        pygame.draw.rect(WIN, COLOR_TAB, self.tabYear)
        pygame.draw.rect(WIN, COLOR_TAB, self.tabRatio)
        
        labelPlay = FONT_TAB.render("Play", True, COLOR_FONT)
        labelTitle = FONT_TAB.render("Title", True, COLOR_FONT)
        labelArtist = FONT_TAB.render("Artist", True, COLOR_FONT)
        labelGenre = FONT_TAB.render("Genre", True, COLOR_FONT)
        labelYear = FONT_TAB.render("Year", True, COLOR_FONT)
        labelRatio = FONT_TAB.render("Ratio", True, COLOR_FONT)       #ratio of last 8 attempts 
            
        WIN.blit(labelPlay, (self.tabPlay.x, self.tabPlay.y + (self.tabPlay.height*.25)))
        WIN.blit(labelTitle, (self.tabTitle.x, self.tabTitle.y + (self.tabTitle.height*.25)))
        WIN.blit(labelArtist, (self.tabArtist.x, self.tabArtist.y + (self.tabArtist.height*.25)))
        WIN.blit(labelGenre, (self.tabGenre.x, self.tabGenre.y + (self.tabGenre.height*.25)))
        WIN.blit(labelYear, (self.tabYear.x, self.tabYear.y + (self.tabYear.height*.25)))
        WIN.blit(labelRatio, (self.tabRatio.x, self.tabRatio.y + (self.tabRatio.height*.25)))
        
        
    def renderSongs(self, WIN, songsList): 
        self.songsList = songsList
        tabHeight = self.height*.04
        tabXOffset, tabYOffset = self.width*.015, self.height*.01
        lastTab = self.tabTitle.bottom
        for song in self.songsList:
            lastTab += tabYOffset           #use this as the y value for the song rects
            songPlay = pygame.Rect(self.width*.01, lastTab, self.width*.04, tabHeight)
            songTitle = pygame.Rect(self.tabPlay.right + tabXOffset, lastTab, self.width*.255, tabHeight)
            songArtist = pygame.Rect(self.tabTitle.right + tabXOffset, lastTab, self.width*.23, tabHeight)
            songGenre = pygame.Rect(self.tabArtist.right + tabXOffset, lastTab, self.width*.25, tabHeight)
            songYear = pygame.Rect(self.tabGenre.right + tabXOffset, lastTab, self.width*.05, tabHeight)
            songRatio = pygame.Rect(self.tabYear.right + tabXOffset, lastTab, self.width*.05, tabHeight)
            
            pygame.draw.rect(WIN, COLOR_TAB, songPlay)
            pygame.draw.rect(WIN, COLOR_TAB, songTitle)
            pygame.draw.rect(WIN, COLOR_TAB, songArtist)
            pygame.draw.rect(WIN, COLOR_TAB, songGenre)
            pygame.draw.rect(WIN, COLOR_TAB, songYear)
            pygame.draw.rect(WIN, COLOR_TAB, songRatio)
            
            labelPlay = FONT_TAB.render("Play", True, COLOR_FONT)
            labelTitle = FONT_TAB.render(song.Title, True, COLOR_FONT)
            labelArtist = FONT_TAB.render(song.Artist, True, COLOR_FONT)
            labelGenre = FONT_TAB.render(song.Genre, True, COLOR_FONT)
            labelYear = FONT_TAB.render(song.Year, True, COLOR_FONT)
            labelRatio = FONT_TAB.render("Ratio", True, COLOR_FONT)       #ratio of last 8 attempts 
            
            WIN.blit(labelPlay, (songPlay.x, songPlay.y + (songPlay.height*.25)))
            WIN.blit(labelTitle, (songTitle.x, songTitle.y + (songTitle.height*.25)))
            WIN.blit(labelArtist, (songArtist.x, songArtist.y + (songArtist.height*.25)))
            WIN.blit(labelGenre, (songGenre.x, songGenre.y + (songGenre.height*.25)))
            WIN.blit(labelYear, (songYear.x, songYear.y + (songYear.height*.25)))
            WIN.blit(labelRatio, (songRatio.x, songRatio.y + (songRatio.height*.25)))
            
            lastTab = songTitle.bottom