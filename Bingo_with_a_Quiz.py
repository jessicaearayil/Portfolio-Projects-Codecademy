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
                print(f"Row: {row} Column: {column}")
                a = self.getNumber(checkList)
                self.bingoCard[row][column] = a

    def display(self):
        for row in self.bingoCard:
            print(row)
            print("\n")
            
  



