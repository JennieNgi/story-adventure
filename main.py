import csv
import os
import time

def getUserInput():
    validated = False
    while (validated == False):
        num = input("> ")
        if ( (num.isdigit() == False) ):
            print("***Invalid input..Please try again***") 
        elif ( (int(num) <= 0) or (int(num) > 3) ):
            print("***Invalid input..Must be 1,2 or 3***") 
        else:
            num = int(num)
            validated = True 
    return num

def gameStart():
    print("")
    print("****** Text Adventure Game v1.0 *******")
    print("%-37s *" % ("*"))
    print("%-12s1 - New Game %14s" % ("*", "*"))
    print("%-12s2 - Load Game %13s" % ("*", "*"))
    print("%-12s3 - Quit %18s" % ("*", "*"))
    print("%-37s *" % ("*"))
    print("***************************************")


def newGame(story):
    print("")
    print(story[0][0])
    print("What do you want to do?")
    print("1 - %1s" % (story[0][1]))
    print("2 - %1s" % (story[0][2]))
    print("3 - Save Game")


def storyGenerator(story, currentPosition):
    validated = False
    while ((story[currentPosition][3] != "") and (story[currentPosition][4] != "") and (validated == False)):
        num = getUserInput()
        if (num == 1):
            # rewrite current position
            currentPosition = int(story[currentPosition][3])
            currentPosition = currentPosition - 1
            # print(currentPosition)
            print("")
            print(story[currentPosition][0])
            if (story[currentPosition][3] != ""):
                print("What do you want to do?")
                print("1 - %1s" % (story[currentPosition][1]))
                print("2 - %1s" % (story[currentPosition][2]))
                print("3 - Save Game")

        elif (num == 2):
            currentPosition = int(story[currentPosition][4])
            currentPosition = currentPosition - 1
            print("")
            print(story[currentPosition][0])
            if (story[currentPosition][4] != ""):
                print("What do you want to do?")
                print("1 - %1s" % (story[currentPosition][1]))
                print("2 - %1s" % (story[currentPosition][2]))
                print("3 - Save Game")
            
        elif (num == 3):
            outfile = open("saved" + ".txt", "w")
            outfile.write(story[currentPosition][0])
            print("")
            print(story[currentPosition][0])
            print("What do you want to do?")
            print("1 - %1s" % (story[currentPosition][1]))
            print("2 - %1s" % (story[currentPosition][2]))
            print("3 - Save Game")
            outfile.close()
                
def main():

    while True:

        gameStart()

        infile = open("story.csv", "r")
        # construct a CSV Reader object
        csvReader = csv.reader(infile)
        # create a list to store everything of the csv 
        story = []
        for row in csvReader:
            story.append(row)
        infile.close()

        num = getUserInput()

        # 1 - New Game
        if (num == 1):
            newGame(story)

            # new game start at zero
            currentPosition = 0
            storyGenerator(story, currentPosition)
        
        # 2 - Load Game
        elif (num == 2):
            # error check for whether the saved.txt exist
            if(os.path.isfile('./saved.txt') == False):
                print("*** No saved.txt exists. A new game will be started ***")
                time.sleep(2.0)
                # if the saved.txt do not exist, start a new game
                newGame(story)
                # new game start at zero
                currentPosition = 0
                storyGenerator(story, currentPosition)

            else:
                #creating the text file
                infile = open("saved.txt","r")
                line = infile.readline()
                # print(line)
                # creating a checklist to match the content in the textfile
                checklist = []
                # print(story[len(story)][0])
                for p in range(0, len(story)):
                    # print(story[p][0])    
                    checklist.append(story[p][0])
                # print(checklist)
                # check which decision point is the player at 
                position = checklist.index(line)
                infile.close()
                print(story[position][0])
                print("What do you want to do?")
                print("1 - %1s" % (story[position][1]))
                print("2 - %1s" % (story[position][2]))
                print("3 - Save Game")
                #continue the game
                currentPosition = position
                storyGenerator(story, currentPosition)

        # 3 - Quit
        elif (num == 3):
            #shut off the program
            return

        time.sleep(2.0)

main()