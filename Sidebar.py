import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.font.init()

COLOR_SIDEBAR = (115, 115, 115)
COLOR_BUTTON_ACTIVE = (225, 255, 255)
COLOR_BUTTON_PASSIVE = COLOR_SIDEBAR
COLOR_FONT_ACTIVE = (0, 0, 0)
COLOR_FONT_PASSIVE = COLOR_BUTTON_PASSIVE
FONT_BUTTON = pygame.font.Font(None, 48)

class Sidebar:
    def __init__(self, WIN):
        self.width = WIN.get_width()*.16            #percentage of screen width
        self.height = WIN.get_height()              #percentage of screen height
        self.x = WIN.get_width() - self.width       #right align
        self.y = 0                                  #top align

    def drawQuizSelect(self, WIN): 
        buttonWidth, buttonHeight = self.width*.80, self.height*.08
        buttonXOffset = self.x + (self.width*.10)
        buttonYOffset = self.height*.10
        self.quiz1Button = pygame.Rect(buttonXOffset, self.height*.05, buttonWidth, buttonHeight)
        self.quiz2Button = pygame.Rect(buttonXOffset, self.quiz1Button.y + buttonYOffset, buttonWidth, buttonHeight)
        self.quiz3Button = pygame.Rect(buttonXOffset, self.quiz2Button.y + buttonYOffset, buttonWidth, buttonHeight)
        self.quiz4Button = pygame.Rect(buttonXOffset, self.quiz3Button.y + buttonYOffset, buttonWidth, buttonHeight)
        self.quiz5Button = pygame.Rect(buttonXOffset, self.quiz4Button.y + buttonYOffset, buttonWidth, buttonHeight)
        
        pygame.draw.rect(WIN, COLOR_BUTTON_ACTIVE, self.quiz1Button)
        pygame.draw.rect(WIN, COLOR_BUTTON_ACTIVE, self.quiz2Button)
        pygame.draw.rect(WIN, COLOR_BUTTON_ACTIVE, self.quiz3Button)
        pygame.draw.rect(WIN, COLOR_BUTTON_ACTIVE, self.quiz4Button)
        pygame.draw.rect(WIN, COLOR_BUTTON_ACTIVE, self.quiz5Button)
        
        label_1 = FONT_BUTTON.render("Quiz 1", True, COLOR_FONT_ACTIVE)
        label_2 = FONT_BUTTON.render("Quiz 2", True, COLOR_FONT_ACTIVE)
        label_3 = FONT_BUTTON.render("Quiz 3", True, COLOR_FONT_ACTIVE)
        label_4 = FONT_BUTTON.render("Quiz 4", True, COLOR_FONT_ACTIVE)
        label_5 = FONT_BUTTON.render("Quiz 5", True, COLOR_FONT_ACTIVE)
        
        WIN.blit(label_1, (self.quiz1Button.x, self.quiz1Button.y + (self.quiz1Button.height*.25)))
        WIN.blit(label_2, (self.quiz2Button.x, self.quiz2Button.y + (self.quiz2Button.height*.25)))
        WIN.blit(label_3, (self.quiz3Button.x, self.quiz3Button.y + (self.quiz3Button.height*.25)))
        WIN.blit(label_4, (self.quiz4Button.x, self.quiz4Button.y + (self.quiz4Button.height*.25)))
        WIN.blit(label_5, (self.quiz5Button.x, self.quiz5Button.y + (self.quiz5Button.height*.25)))
        
    def drawModeSelect(self, WIN, MODE):
        if MODE:
            currFontColor = COLOR_FONT_ACTIVE
            currButtColor = COLOR_BUTTON_ACTIVE
        else:
            currFontColor = COLOR_FONT_PASSIVE
            currButtColor = COLOR_BUTTON_PASSIVE
        buttonWidth, buttonHeight = self.width*.80, self.height*.08
        buttonXOffset = self.x + (self.width*.10)
        buttonYOffset = self.height*.10
        
        self.viewButton = pygame.Rect(buttonXOffset, self.quiz5Button.bottom + buttonHeight*.5, buttonWidth, buttonHeight)
        self.learnButton = pygame.Rect(buttonXOffset, self.viewButton.y + buttonYOffset, buttonWidth, buttonHeight)
        self.practiceButton = pygame.Rect(buttonXOffset, self.learnButton.y + buttonYOffset, buttonWidth, buttonHeight)
        self.historyButton = pygame.Rect(buttonXOffset, self.practiceButton.y + buttonYOffset, buttonWidth, buttonHeight)
        
        pygame.draw.rect(WIN, currButtColor, self.viewButton)
        pygame.draw.rect(WIN, currButtColor, self.learnButton)
        pygame.draw.rect(WIN, currButtColor, self.practiceButton)
        pygame.draw.rect(WIN, currButtColor, self.historyButton)
        
        label_View = FONT_BUTTON.render("View", True, currFontColor)
        label_Learn = FONT_BUTTON.render("Learn", True, currFontColor)
        label_Practice = FONT_BUTTON.render("Practice", True, currFontColor)
        label_History = FONT_BUTTON.render("History", True, currFontColor)
        
        WIN.blit(label_View, (self.viewButton.x, self.viewButton.y + (self.viewButton.height*.25)))
        WIN.blit(label_Learn, (self.learnButton.x, self.learnButton.y + (self.learnButton.height*.25)))
        WIN.blit(label_Practice, (self.practiceButton.x, self.practiceButton.y + (self.practiceButton.height*.25)))
        WIN.blit(label_History, (self.historyButton.x, self.historyButton.y + (self.historyButton.height*.25)))

    def update(self, WIN):
        self.width = WIN.get_width()*.16
        self.height = WIN.get_height()
        self.x = WIN.get_width() - self.width
        self.sidebar = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(WIN, COLOR_SIDEBAR, self.sidebar)
        self.drawQuizSelect(WIN)