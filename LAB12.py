# TEAM MAKESMART
# Maco Doussias, Pavlos Papadonikolakis, Jake McGhee
# LAB12
# 11-28-17

# CAVE ESCAPE Game Description:
# An explorer has fallen down a hole in the ground and into a cave. In order to navigate through the cave,
# s/he has to use specific commands that lead to specific directions inside the cave. If the user is lost
# or confused, there is a map or a help description available.
# MAP OF CAVE
#  [startRoom]    -  [darkRoom]  -  [islandRoom]
#      |                                   |
#  [skeletonRoom] -  [batRoom]
#
# Win Condition for Game:  Get the rope from the island room and use it to climb out of the cave
# Lose Condition for Game:  Do more than twenty room changes
# Secret room.  Use the matches, if you find them, to light up the dark room, reveals a new secret room


#TODO Major bug, cannot find out why secret room always crashes when exiting the secret room.
#TODO find a solution so that it doesn't automatically print the room details when help or map is entered
#TODO Note that every time the user is prompted to press enter, they MUST have the... 
# ...ability to EXIT or press HELP according to instructions... this needs fixed.
#TODO MAJOR BUG!!! Why is the secret room crashing the program?  Can't get out of the secret room.
#TODO see if maxRoomChanges variable can be chagned to a CONSTANT variable 

def map():  # Serves as the additional feature required per classroom instruction
    """ Prints map of the cave """
    """ Map can only be read in rooms with sufficient lighting """
    printNow('************************')
    printNow('MAP OF CAVE:')
    printNow("[startRoom]    -  [darkRoom]  -  [islandRoom]")
    printNow("     |                                  |")
    printNow("[skeletonRoom] -  [batRoom]")
    printNow('************************')


def getHelp():
    """ Prints help instructions to the user, if the user enters the 'HELP' command """
    printNow (welcomeMessage())


def welcomeMessage():
    """ displays a wellcome message that displays the rules of the game """
    return '*** WELLCOME TO THE CAVE ESCAPE GAME! ***\n' \
           '-- In each room you will be told which directions you can go\n-- You\'ll be' \
           'able to go UP, DOWN, LEFT or RIGHT by typing that direction\n' \
           '-- Type HELP to redisplay this introduction --\n' \
           '-- Type MAP for a cave map\n' \
           '-- Type EXIT to quit at any time\n'


def printDetails(description):
    """ prints the details of each room """

    printNow('************************')
    printNow ('YOU ARE CURRENTLY in :')
    printNow(description)
    printNow('************************')


def getCommand(roomSpecificCommands):
    """ Gets a command from the user, ensure it is an acceptable command for the program and returns command
        If the command is not a valid entry, displays error message and requests user to enter a valid command
        :param roomSpecificCommands (list) the specific commands for the given room
        :return command (string) the command typed by the user
    """

    acceptableCommands = ['EXIT', 'HELP', 'MAP'] + roomSpecificCommands
    allValidCommands = "COMMANDS: "

    for i in range(0, len(acceptableCommands)):  # This for loops puts all the acceptable commands into a single string
        allValidCommands += acceptableCommands[i] + ' '

    while True:

        command = requestString(
            allValidCommands + '\nEnter Command:')
        command = command.upper()

        if command not in acceptableCommands:
            printNow('************************')
            printNow("ERROR! Not a valid entry!")
            printNow("Acceptable Commands for this room are")
            printNow(acceptableCommands)
            printNow('************************')
        else:
            return command


def startRoom(acceptableCommands):
    """ the first room
         :return userCommand (string) the command typed by the user
    """
    description = 'START ROOM!\nThis area is big and expansive.\n' \
                  'You can see daylight coming from where you fell.\nIf you have rope you can climb out!'
    printDetails(description)
    userCommand = getCommand(acceptableCommands)#['RIGHT', 'DOWN']
    return userCommand


def darkRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'DARK ROOM!\nThe room is dark and you cannot see much\n' \
                  'It smells damp and you can hear critters in the nearby water.\n' \
                  'This room needs more light!'
    printDetails(description)
    userCommand = getCommand(acceptableCommands)#['RIGHT', 'DOWN', 'LEFT']
    return userCommand

def secretRoom(acceptableCommands):
    #""" one of the rooms
    #    :return userCommand (string) the command typed by the user
    #"""
    description = 'SECRET ROOM!\nWow this room is not on map.  There is a commodore 64 computer in this room!\n' \
                  'If you play the game War Games(WOPR) on this you might accidentally break into NORAD!\n' \
                  'Best to leave this secret room alone!'
    printDetails(description)
    userCommand = getCommand(acceptableCommands)
    return userCommand  

def skeletonRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'SKELETON ROOM!\nStalagmites fill this cavern.\n' \
                  'You see skeletons of past victims that fell down the well.\nPoor souls!'
    printDetails(description)
    userCommand = getCommand(acceptableCommands)#['UP', 'RIGHT']
    return userCommand


def batRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'BATROOM!\n The walls of the cavern are filled with thousands of hanging bats\n ' \
                  'It smells of bat guano... Yuck.\nAnother explorer left their pack here with a bunch of matches!'
    printDetails(description)
    userCommand = getCommand(acceptableCommands)#['LEFT', 'UP']
    return userCommand


def islandRoom(acceptableCommands):
    """ one of the rooms
        :return userCommand (string) the command typed by the user
    """
    description = 'ISLAND ROOM!\nThe room is surrounded by a large lake that looks pristine\n' \
                  'The water is blue and it refracts light on the cavern walls.\nThere is a lot of rope laying around!'
    printDetails(description)
    userCommand = getCommand(acceptableCommands)#['LEFT']
    return userCommand


def main():
    """main function, starts the game """

    printNow (welcomeMessage())
    requestString('Press ENTER to contine...')
    x = 0  # represents an x cartestian coordinate
    y = 0  # represents a y cartestian coordinate
    
    #additional items and actions 
    darkRoomLit = false #changes to true if matches used in dark room 
    hasMatches = false #changes to true if user picks up matches
    hasRope = false #changes to true if user picks up rope
    secretRoomAccess = false #user can only gain access to secret room by lighting a match in the dark room
    roomChanges = 0 #If room changes exceeds maxRoomChanges, you lose the game
    maxRoomChanges = 20 #Lose condition if you exceed maxRoomChanges   
    # Get input from user by calling the room functions.  Input will be specific to each room
    while true:

        if x == 0 and y == 0:
          if hasRope == false:
            userCommand = startRoom(['RIGHT', 'DOWN'])
          else:
            userCommand = startRoom(['RIGHT', 'DOWN', 'CLIMBOUT'])            
        elif x == 0 and y == -1:
            userCommand = skeletonRoom(['UP', 'RIGHT'])
        elif x == 1 and y == 0:
         if secretRoomAccess == true:
           userCommand = darkRoom(['RIGHT', 'DOWN', 'LEFT', 'UP'])
         elif hasMatches == true:
           userCommand = darkRoom(['RIGHT', 'DOWN', 'LEFT', 'STRIKEMATCH'])
         else:
           userCommand = darkRoom(['RIGHT', 'DOWN', 'LEFT'])
        elif x == 1 and y == 1:
          secretRoom(['DOWN'])       
        elif x == 2 and y == 0:
          if hasRope == false:    
            userCommand = islandRoom(['LEFT','GETROPE'])
          else:
            userCommand = islandRoom(['LEFT'])   
        elif x == 1 and y == -1:
          if hasMatches == true:  
            userCommand = batRoom(['LEFT', 'UP'])
          else:
            userCommand = batRoom(['LEFT', 'UP', 'GETMATCHES'])
                        

        # Process off of what user input or userCommand is
        if userCommand == 'HELP':
            getHelp()
            requestString('Press ENTER to contine...') #TODO change to end of while
        elif userCommand == 'EXIT':
            print("Even though you are a quiter, thank you for playing!")
            return  # effectively exit the program
        elif userCommand == 'MAP':
            if x == 1 and y == 0:
                printNow('************************')
                printNow('You cannot read your map in the Dark Room... Too dark!')
                printNow('************************')
                requestString('Press ENTER to contine...')#TODO change to end of while
            else:
                map() #Display the map to the console
                requestString('Press ENTER to contine...')#TODO change to end of while
        elif userCommand == 'GETMATCHES':
          printNow('************************')
          printNow('You have picked up several matches!')
          printNow('************************')
          requestString('Press ENTER to contine...')#TODO change to end of while
          hasMatches = true
        elif userCommand == 'STRIKEMATCH':
          printNow('************************')
          printNow('After stirking the match, you see a secret room hidden in the shadows!')
          printNow('You can now enter the secret room!')
          printNow('************************')
          requestString('Press ENTER to contine...')#TODO change to end of while  
          secretRoomAccess = true #Now user can access secret room  
        elif userCommand == 'GETROPE':
          printNow('************************')
          printNow('You have picked up rope!')
          printNow('You can use rope to climb!')
          printNow('************************')
          hasRope = true
          requestString('Press ENTER to contine...')#TODO change to end of while   
        elif userCommand == 'CLIMBOUT':
          printNow('************************')
          printNow('YOU WIN! You use the rope to climb out!')
          printNow('You have survived the game!')
          printNow('************************')   
          return #end of game, user has won               
        elif userCommand == 'UP':
            y += 1
            roomChanges += 1 
        elif userCommand == 'DOWN':
            y -= 1
            roomChanges += 1
        elif userCommand == 'RIGHT':
            x += 1
            roomChanges += 1
        elif userCommand == 'LEFT':
            x -= 1
            roomChanges += 1
    
        #GAME OVER condition        
        if roomChanges > maxRoomChanges:
          printNow('GAME OVER\nYOU HAVE DIED FROM OXYGEN DEPREVATION\nTOO MANY ROOM CHANGES SO YOU HAVE LOST THE GAME!')
          return #end of game  
           
#executes the main function on load
main()