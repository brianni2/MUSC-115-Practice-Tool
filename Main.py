import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *

from Song import Song
from Menu import *
from Sidebar import *

WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("MUSC 115: Pop, Rock, and Soul Music Quiz Tool")
FPS = 60

def drawWindow(mode, currList, mainpan, sidebar, selectMode):
    '''
    draw window on initial call
    resizes window and elements on later calls
    '''
    mainpan.update(WIN)
    sidebar.update(WIN)
    sidebar.drawModeSelect(WIN, selectMode)
    if(mode == 0):
        mainpan.viewSongs(WIN)
        mainpan.renderSongs(WIN, currList)
    pygame.display.update()

def updateMainpanel(mode, currList, mainpan):
    mainpan.update(WIN)
    if(mode == 0):
        mainpan.viewSongs(WIN)
        mainpan.renderSongs(WIN, currList)
    pygame.display.update(mainpan.mainpan)
    
def unlockModes(sidebar, selectMode):
    sidebar.drawModeSelect(WIN, selectMode)
    pygame.display.update(sidebar.sidebar)
    
def loadSongs(songsList):
    songs = []
    with open(songsList) as f:
        line = f.readline()
        while line:
            title, line = line.split(":")
            artist, year, genre = line.split(";")
            artist = artist[2:]
            genre = genre[2:]
            genre, catch = genre.split("]")
            songs.append(Song(title, artist, year, genre))
            line = f.readline()
    return songs

def debugPrint(currList):
    count = 1
    for song in currList:
        print(str(count) + ": " + song.print())
        count+=1

def main():
    pygame.init()
    gameClock = pygame.time.Clock()
    gameIsRun = True
    selectMode = False
    mode = -1
    currList = []
    hideList = []
    maxSize = len(currList)
    mainpan = Mainpanel(WIN)
    sidebar = Sidebar(WIN)
    drawWindow(mode, currList, mainpan, sidebar, selectMode)
    while(gameIsRun):
        gameClock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                gameIsRun = False
                pygame.display.quit()
                pygame.quit()
            elif(event.type == VIDEORESIZE):
                drawWindow(mode, currList, mainpan, sidebar, selectMode)
            elif(event.type == MOUSEWHEEL):
                if(mode == 0):
                    if(event.y < 0):
                        if(len(currList) == 1):
                            continue
                        hideList.append(currList[0])
                        currList.pop(0)
                        updateMainpanel(mode, currList, mainpan)
                    if(event.y > 0):
                        if(len(currList) == maxSize):
                            continue
                        currList.insert(0, hideList[-1])
                        hideList.pop(-1)
                        updateMainpanel(mode, currList, mainpan)
            elif(event.type == MOUSEBUTTONDOWN):
                if(sidebar.quiz1Button.collidepoint(event.pos)):
                    selectMode = True
                    unlockModes(sidebar, selectMode)
                    mode = 0
                    songsList = os.path.join("Songs", "Quiz 1", "Quiz 1 Songs List.txt")
                    currList = loadSongs(songsList)
                    maxSize = len(currList)
                    drawWindow(mode, currList, mainpan, sidebar, selectMode)
                if(sidebar.quiz2Button.collidepoint(event.pos)):
                    selectMode = True
                    unlockModes(sidebar, selectMode)
                    mode = 0
                    songsList = os.path.join("Songs", "Quiz 2", "Quiz 2 Songs List.txt")
                    currList = loadSongs(songsList)
                    maxSize = len(currList)
                    drawWindow(mode, currList, mainpan, sidebar, selectMode)
                if(sidebar.quiz3Button.collidepoint(event.pos)):
                    selectMode = True
                    unlockModes(sidebar, selectMode)
                    mode = 0
                    songsList = os.path.join("Songs", "Quiz 3", "Quiz 3 Songs List.txt")
                    currList = loadSongs(songsList)
                    maxSize = len(currList)
                    drawWindow(mode, currList, mainpan, sidebar, selectMode)
                if(sidebar.quiz4Button.collidepoint(event.pos)):
                    selectMode = True
                    unlockModes(sidebar, selectMode)
                    mode = 0
                    songsList = os.path.join("Songs", "Quiz 4", "Quiz 4 Songs List.txt")
                    currList = loadSongs(songsList)
                    maxSize = len(currList)
                    drawWindow(mode, currList, mainpan, sidebar, selectMode)
                if(sidebar.quiz5Button.collidepoint(event.pos)):
                    selectMode = True
                    unlockModes(sidebar, selectMode)
                    mode = 0
                    songsList = os.path.join("Songs", "Quiz 5", "Quiz 5 Songs List.txt")
                    currList = loadSongs(songsList)
                    maxSize = len(currList)
                    drawWindow(mode, currList, mainpan, sidebar, selectMode)
        
        
if __name__ == "__main__":
    main()