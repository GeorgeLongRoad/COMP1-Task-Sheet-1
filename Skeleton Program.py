# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014


import random
import datetime
import pdb

NO_OF_RECENT_SCORES = 10

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = ''

Deck = [None]
RecentScores = [None]
Choice = ''
SameScore = False

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  elif RankNo == 14:
    Rank = 'Ace'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print('6. Save high scores' )
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  Choice = Choice[0].lower()
  print()
  return Choice


#==================================TASK 6============================================
def DisplayOptions():
  print('OPTION MENU')
  print('')
  print('1. Set Ace to be HIGH or LOW')
  print('2. Setting cards the same score ')
  print()
  print()

def GetOptionChoice():
  OptionChoice = input('Select an option from the menu (or enter q to quit): ')
  OptionChoice = OptionChoice[0]
  print()
  return OptionChoice

def SetOptions(OptionChoice):
  if OptionChoice == "1":
    SetAceHighLow()
  elif OptionChoice == "2":
    SetSameScore()
    
def SetAceHighLow():
  global High
  aceHL = input("Do you want ace to be high or low?(h/l): ").lower()
  High = None
  if aceHL == "h":
    High = True
  elif aceHL == "l":
    High = False

#================================================================================
    
#========================Task 11========
def SetSameScore():
  SameScore = input('Do you want equal cards to have the same score?:  ')
  #valid = False
  if SameScore == 'y':
    SameScore = True
  elif SameScore == 'n':
    SameScore = False
#===============    
def LoadDeck(Deck, High):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    if Deck[Count].Rank == 1 and High == True:
      Deck[Count].Rank = 14
    Count = Count + 1
  
 
def ShuffleDeck(Deck):
  #pdb.set_trace()
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  PlayerName = input('Please enter your name: ')
  while len(PlayerName) == 0:
    print('You must enter something for your name.')
    PlayerName = input('Please enter your name: ')
  return PlayerName


def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)?: ')
  Choice = Choice[0].upper()
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = ''

def DisplayRecentScores(RecentScores):
  BubbleSortScores(RecentScores) #task 7
  print()
  print('Recent Scores: ')
  print()
  print("{0:<15}{1:<15}{2:<15}".format("Name","Score","Date"))
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<15}{1:<15}{2:<15}".format(RecentScores[Count].Name,RecentScores[Count].Score,RecentScores[Count].Date))
  print() 
  print('Press the Enter key to return to the main menu')
  input()
  print()

########################Task 7############################
def BubbleSortScores(RecentScores):
  sort = False
  while not sort:
    sort = True
    for Count in range(1, NO_OF_RECENT_SCORES):
      if RecentScores[Count].Score < RecentScores[Count + 1].Score:
        sort = False
        temp = RecentScores[Count + 1]
        RecentScores[Count + 1] = RecentScores[Count]
        RecentScores[Count] = temp
############################################################      

def UpdateRecentScores(RecentScores, Score):
  Leaderboard = input('Do you want to add your score to the high score table? (y or n): ')
  if Leaderboard[0].lower() == 'y':
    CurrentDate = datetime.date.today()
    TodaysDate = datetime.date.strftime(CurrentDate,"%d/%m/%y")
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
        RecentScores[Count].Date = RecentScores[Count + 1].Date
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].Date = TodaysDate
  elif Leaderboard[0].lower() == 'n':
    DisplayMenu()
    GetMenuChoice()

def PlayGame(Deck, RecentScores):
  global SameScore
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'Y') and (Choice != 'N'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1 
    if SameScore == True and NextCard.Rank == LastCard.Rank:
      GameOver = True
    if SameScore == False and NextCard.Rank == LastCard.Rank:
      GameOver = False
      NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard) 
    if (Higher and Choice == 'Y') or (not Higher and Choice == 'N'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

#######################Task 8#######################
def SaveScores(RecentScores):
  with open("save_scores.txt",mode="w",encoding="utf-8")as my_file:
    for Count in range(1,NO_OF_RECENT_SCORES+1):
      Name = RecentScores[Count].Name
      Score = ("{0}".format(RecentScores[Count].Score))
      Date = RecentScores[Count].Date
      my_file.write(Name+("\n"))
      my_file.write(Score+("\n"))
      my_file.write(Date+("\n"))
    print("Scores Saved.")
#############################################

########################Task 9###################
def LoadScores():
  with open("save_scores.txt",mode="r",encoding="utf-8")as my_file:
    for Count in range(1,NO_OF_RECENT_SCORES+1):
      Name = my_file.readline()
      Score = my_file.readline()
      Date = my_file.readline()
      Name = Name.rstrip("\n")
      Score = Score.rstrip("\n")
      Score = int(Score)
      Date = Date.rstrip("\n")
      RecentScores[Count].Name = Name
      RecentScores[Count].Score = Score
      RecentScores[Count].Date = Date
    
if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  try:
    LoadScores()
  except IOError:
    print()
    print('saved games file not found, a new file has been created.')
    print()
    SaveScores(RecentScores)
  Choice = ''
  High = False #Task 6
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      #pdb.set_trace()
      LoadDeck(Deck, High)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck, High)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      SetOptions(OptionChoice)
    elif Choice == '6':
      SaveScores(RecentScores) #Task 7


