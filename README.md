![adventureGame](https://user-images.githubusercontent.com/75710628/223285469-56c414c2-1181-4a5d-8dda-5ff954f99b20.png)

# Story Adventure
This is a simple text adventure game built in Python 3. It uses a CSV file to store the story and decision points, and allows the player to make choices and progress through the story.

## Installation
- Python 3.10.2 
- Visual Studio Code

## Game Instruction
- Run Terminal in Visual Studio Code
- The player will be asked whether to start a new game or load the game saved last time or quit
- If the player haven't saved any game before, the system will display an error message and automatically start the new game for them
- Questions will be asked to let player choose options 
- Each options will direct the player to the next story line based on the pre-set stories saved in an excel document
- The player could save the story anytime and a txt.file will be saved to store their record.
- Once the player lose the game, the system will automatically restart the game for them after 2 seconds

## Code Explaination
- Error checking is added if the user enter any other except option provided
- If else statement is used
- While loop is used
- Python libraries (os, csv, time) are used

## Credit/Acknowledgment
- Nova Scotia Community College school project
