import random
import os
import time
# List of Questions (contains a set of 3 each having 25 questions) :
Questions = [{1: "The only number that can be divided by itself", 2: "An even prime number",
              3: "First odd prime number", 4: "Has same number of alphabets as the number",
              5: "Number of rings in symbol of Olympics", 6: "Smallest perfect number",
              7: "A mersenne prime", 8: "Atomic number of Oxygen", 9: "An ennead", 10: "Decade",
              11: "First repdigit", 12: "A dozen", 13: "Triskaidekaphobia", 14: "A fortnight in days",
              15: "A crystal anniversary", 16: "Atomic number of Sulphur",
              17: "Final mission of NASA's Apollo program", 18: "Holes on a golf course",
              19: "Adele's Debut Album", 20: "In older english literature, called Score",
              21: "Total number of dots on a regular dice", 22: "Number of bones of a human skull",
              23: "Michael Jordan's and David Beckham's jersey number",
              24: "Number of carats in 100% pure gold", 25: "World Pasta Day is held on October"},
             {1: "The number referred to as multiplicative identity", 2: "Atomic number of Helium",
              3: "Number of primary colors", 4: "Smallest composite number", 5: "Atomic number of Boron",
              6: "Hex in Greek", 7: "Number of continents", 8: "An Octave",
              9: "Highest single digit Arabic numeral", 10: "Sum of first 3 prime numbers",
              11: "A Canadian loonie", 12: "Inches in a feat", 13: "The Blue Moon", 14: "Valentines Day",
              15: "Players in a rugby team", 16: "Total pawns in a chessboard",
              17: "The coming of age for wizards in the Harry Potter universe", 18: "Age to vote",
              19: "A centred hexagonal number", 20: "Number of “baby teeth” or “milk teeth” for a child",
              21: "Number of consonants in English language", 22: "Title track by Taylor Swift",
              23: "Chromosomes in human DNA", 24: "Age of the oldest cat",
              25: "Pairs of chromosomes in Rice"},
             {1: "The value represented by the ace card", 2: "Base of binary numbers",
              3: "Categories of medals in Olympic Games", 4: "Number of Teenage Mutant Ninjas",
              5: "Number of sides in pentagon", 6: "Number of sides in dice", 7: "Rainbow colors",
              8: "Largest cube in Fibanocci series", 9: "Number of innings in baseball",
              10: "1 cm in mm", 11: "Players in a football team", 12: "Pair of ribs in human body",
              13: "Stripes in the US flag", 14: "Number of Russia's neighbors",
              15: "Grid of squares in Scrabble board", 16: "A sweet birthday",
              17: "Syllables in a Haiku poem", 18: "Pairs of ribs in a horse",
              19: "World record for the most countries visited in one day",
              20: "The atomic number of Calcium ", 21: "The Royal Salute",
              22: "Letters in the Hebrew Alphabet", 23: "Seconds for blood to circulate the body(average)",
              24: "Total elements that make up the human body", 25: "Quarter of 100"}]

size = 5

# Class definition

class bingo(object):
    checklist = []
    bingoCard = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def __init__(self, player_name):
        self.player_name = player_name

    def getNumber(self, checklist):
        a = int(input("Enter number between 1 and 25: "))
        if a in checklist:
            print("This is already in the Bingo Card")
            return self.getNumber(checklist)
        else:
            checklist.append(a)
        if a < 26 and a > 0:
            return a
        else:
            return self.getNumber(checklist)

    def addTo_bingoCard(self):
        checkList = []
        for row in range(size):
            for column in range(size):
                print(f"Row: {row+1} Column: {column+1}")
                a = self.getNumber(checkList)
                self.bingoCard[row][column] = a

    def display(self):
        for row in self.bingoCard:
            print(row)
            print("\n")
            
  
questions_asked = []

# Generate a random number

def randomNumber_generator(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)


# Get the question

def getQuestion(question_no):
    question_set = randomNumber_generator(0, 2)
    question = Questions[question_set][question_no]
    print(question)
    answer = input("Your answer: ")
    answer = int(answer)
    if (answer == question_no):
        return True
    else:
        return False


# Cross out the right answers

def crossOut(number, bingoCard):
    for i in range(size):
        for j in range(size):
            if (bingoCard[i][j] == number):
                bingoCard[i][j] = 0
    return bingoCard


# Check if card is Bingo

def isBingo(crossCard):
    count = 0
    total_count = 0
    for i in range(size):
        for j in range(size):
            if (crossCard[i][j] == 0):
                count += 1
        if count == size:
            total_count += 1
        count = 0
    for j in range(size):
        for i in range(size):
            if (crossCard[i][j] == 0):
                count += 1
        if count == size:
            total_count += 1
        count = 0
    if total_count == 3:
        return True
    else:
        return False


# Set the game

print("\t \t \t WELCOME TO THIS GAME OF BINGO WITH A TWIST OF QUIZ......")
print("\n \t \t \t This is a 2 player game so grab a friend and let's get started....")
player1 = input("\n Hi! Enter your name Player 1 : ")
player2 = input("\n Player 2, Hi! Enter your name : ")
print("\n\n\n")
print("\n" + player1 + " ,go ahead and enter the values for your bingo card..")
player1_obj = bingo(player1)
player1_obj.addTo_bingoCard()
player1_obj.display()
time.sleep(5)
os.system('cls')
print("\n\n\n")
print("\n" + player2 + " ,go ahead and enter the values for your bingo card..")
player2_obj = bingo(player2)
player2_obj.addTo_bingoCard()
player2_obj.display()
time.sleep(5)
os.system('cls')


# Start the game

while (not (isBingo(player1_obj.bingoCard) or isBingo(player2_obj.bingoCard)) and len(questions_asked) < 25):
    print("List of numbers called: ")
    print(questions_asked)
    time.sleep(3)
    os.system('cls')
    q = randomNumber_generator(1, 25)
    if q not in questions_asked:
        questions_asked.append(q)
        print("\n\n")
        print("Turn Player1: " + player1)
        if (getQuestion(q)):
            print("\n")
            print("Yaay.." + player1 + " got it right.. :D")
            crossOut(q, player1_obj.bingoCard)
        else:
            print("\n")
            print("Oops..Looks like you got it wrong, " + player1)
        player1_obj.display()
        time.sleep(2)
        os.system('cls')
        print("\n\n")
        print("Turn Player2: " + player2)
        if (getQuestion(q)):
            print("\n")
            print("Yaay.." + player2 + " got it right.. :D")
            crossOut(q, player2_obj.bingoCard)
        else:
            print("\n")
            print("Oops..Looks like you got it wrong, " + player2)
        player2_obj.display()
        time.sleep(2)
        os.system('cls')
        
        
# Check who won the game

if (isBingo(player1_obj.bingoCard)):
    print("\n\n \t \t CONGRATULATIONS....." + player1.upper() +
          " \n \t \t You are the WINNER of BINGO WITH A TWIST OF QUIZ !!!!")
elif (isBingo(player2_obj.bingoCard)):
    print("\n\n \t \t CONGRATULATIONS....." + player2.upper() +
          " \n \t \t You are the WINNER of BINGO WITH A TWIST OF QUIZ !!!!")
elif (len(questions_asked) > 24):
    print("\n\n Oh noo... No one won :( \n Better luck next time...")



