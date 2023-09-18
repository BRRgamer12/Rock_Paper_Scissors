import random

#Definition of variables

Player = 0
Player_status = 0
Player_wins = 0
Rival_status = 0
Rival_wins = 0
Match = 'Y'

#Start of the match loop function

while Match == 'Y':

    #Command that filters the "Choice" input to accept only Rock, Paper and Scissors, and defines a value to the decision

    while True:
        print('Select an option (R, P, S):')
        Choice = input().upper()
        if Choice == 'R':
            Player = 1
            break
        elif Choice == 'P':
            Player = 2
            break
        elif Choice == 'S':
            Player = 3
            break
        else:
            print ('Invalid choice. Please enter again')
            continue

    #Random choice for the rivel

    Rival = random.randint(1,3)

    '''
    Rock = 1
    Paper = 2
    Scissors = 3
    '''

    #Decision of the player and the rival choice

    if Player == 1:
        Player_status = 'Rock'
    elif Player == 2:
        Player_status = 'Paper'
    elif Player == 3:
        Player_status = 'Scissors'

    if Rival == 1:
        Rival_status = 'Rock'
    elif Rival == 2:
        Rival_status = 'Paper'
    elif Rival == 3:
        Rival_status = 'Scissors'

    #Code that shows the status of the player and rival

    print ('The player chose', Player_status, 'and his rival chose', Rival_status)

    #Decision that defines the winner of the match

    if Player == Rival:
        print ("it's a draw!")
    elif Player == 1 and Rival == 3:
        print("The player won!")
        Player_wins = Player_wins + 1
    elif Player == 2 and Rival == 1:
        print("The player won!")
        Player_wins = Player_wins + 1
    elif Player == 3 and Rival == 2:
        print("The player won!")
        Player_wins = Player_wins + 1
    else:
        print("The rival won!")
        Rival_wins = Rival_wins + 1

    #input and loop for another match

    while True:
        print('Want to play another match? (Y, N)')
        Match = input().upper()
        if Match == 'Y':
            break
        elif Match == 'N':
            break
        else:
            print ('Invalid choice. Please enter again')
            continue

#Statistic of the total wins of the player and rivalr

print ('Player total wins:', Player_wins)
print ('Rival total wins', Rival_wins)

if Player_wins > Rival_wins:
    print('The Player is the winner')
elif Player_wins == Rival_wins:
    print("It's a draw")
else:
    print("The rival is the winner")
