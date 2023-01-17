''' 
Python 3.8
Name: Cole Edwards
CWID: -
Date: 11/13/21
Desc: Implementaion of Othello (Reversi) along with min-max search tree and alpha-beta pruning.
      Also has the ability to trace a previous game.
      Handles PvP and PvAI
'''

import math
import copy

#Declare Global Variables
DEBUG = False
ABP = True
TotalnumberofGameStatesChecked = 0


def ABC_Conversion(userInput):
    ABC = [" ", "a", "b", "c", "d", "e", "f", "g", "h"]
    #Split the String array into two parts, the X and Y Coords
    part1Letter = userInput[0]
    part2 = int(userInput[1])
    #Convert the letter to a usable number for a coordinate plane
    part1Number = ABC.index(part1Letter)
    return [part1Number, part2]


def rev_ABC_Conversion(Move):
    #this is for making an input that looks like [5,6] into e6
    ABC = [" ", "a", "b", "c", "d", "e", "f", "g", "h"]
    #Get the index of the letter
    part1Letter = ABC[Move[0]]
    return part1Letter +str(Move[1]) + "\n"


#Find the possible moves that can be made by the Player who's turn it is (Active Player)
def moveCalculator(Board, ActivePlayer, InactivePlayer):
    possibleMoves = []
    AdditiveScores = []
    X = 0
    Y = 0
    possibleActivePlayerScore = 0
    #find current pieces owned by the players
    for r in Board:
        for c in r:
            if(Board[Y][X] == ActivePlayer):
                possibleActivePlayerScore = 0
                #check for the inactive player's piece North of the active player's piece and make sure its not out of bounds
                if((Y-1) != 0 and Board[Y-1][X] == InactivePlayer):
                    i = 1
                    #Check the lane for more of the inactive player's pieces
                    while((Y-i) != 0 and Board[Y-i][X] == InactivePlayer):
                        #increment the number of pieces found
                        i+=1
                    possibleActivePlayerScore += i
                    if(Y-i != 0 and ([X,Y-i] in Board) == False and Board[Y-i][X] != ActivePlayer):
                        #check the bounds of the possible playable position and that its already not taken
                        possibleMoves.append([X,Y-i])
                        AdditiveScores.append(possibleActivePlayerScore)
                possibleActivePlayerScore = 0
                #check for the inactive player's piece North East of the active player's piece and make sure its not out of bounds
                if((X+1) != 9 and (Y-1) != 0 and Board[Y-1][X+1] == InactivePlayer):
                    i = 1
                    #Check the lane for more of the inactive player's pieces
                    while((X+i) != 9 and (Y-i) != 0 and Board[Y-i][X+i] == InactivePlayer):
                        #increment the number of pieces found
                        i+=1
                    possibleActivePlayerScore += i
                    if(X+i != 9 and Y-i != 0 and ([X+i,Y-i] in Board) == False and Board[Y-i][X+i] != ActivePlayer):
                        #check the bounds of the possible playable position and that its already not taken
                        possibleMoves.append([X+i,Y-i])
                        AdditiveScores.append(possibleActivePlayerScore)
                possibleActivePlayerScore = 0
                #check for the inactive player's piece East of the active player's piece and make sure its not out of bounds
                if((X+1) != 9 and Board[Y][X+1] == InactivePlayer):
                    i = 1
                    #Check the lane for more of the inactive player's pieces
                    while((X+i) != 9 and Board[Y][X+i] == InactivePlayer):
                        #increment the number of pieces found
                        i+=1
                    possibleActivePlayerScore += i
                    if(X+i != 9 and ([X+i,Y] in Board) == False and Board[Y][X+i] != ActivePlayer):
                        #check the bounds of the possible playable position and that its already not taken
                        possibleMoves.append([X+i,Y])
                        AdditiveScores.append(possibleActivePlayerScore)
                possibleActivePlayerScore = 0
                #check for the inactive player's piece South East of the active player's piece and make sure its not out of bounds
                if((X+1) != 9 and (Y+1) != 9 and Board[Y+1][X+1] == InactivePlayer):
                    i = 1
                    #Check the lane for more of the inactive player's pieces
                    while((X+i) != 9 and (Y+i) != 9 and Board[Y+i][X+i] == InactivePlayer):
                        #increment the number of pieces found
                        i+=1
                    possibleActivePlayerScore += i
                    if(X+i != 9 and Y+i != 9 and ([X+i,Y+i] in Board) == False and Board[Y+i][X+i] != ActivePlayer):
                        #check the bounds of the possible playable position and that its already not taken
                        possibleMoves.append([X+i,Y+i])
                        AdditiveScores.append(possibleActivePlayerScore)
                    #print()
                possibleActivePlayerScore = 0
                #check for the inactive player's piece South of the active player's piece and make sure its not out of bounds
                if((Y+1) != 9 and Board[Y+1][X] == InactivePlayer):
                    i = 1
                    #Check the lane for more of the inactive player's pieces
                    while((Y+i) != 9 and Board[Y+i][X] == InactivePlayer):
                        #increment the number of pieces found
                        i+=1
                    possibleActivePlayerScore += i
                    if(Y+i != 9 and ([X,Y+i] in Board) == False and Board[Y+i][X] != ActivePlayer):
                        #check the bounds of the possible playable position and that its already not taken
                        possibleMoves.append([X,Y+i])
                        AdditiveScores.append(possibleActivePlayerScore)
                possibleActivePlayerScore = 0
                #check for the inactive player's piece South West of the active player's piece and make sure its not out of bounds
                if((X-1) != 0 and (Y+1) != 9 and Board[Y+1][X-1] == InactivePlayer):
                    i = 1
                    #Check the lane for more of the inactive player's pieces
                    while((X-i) != 0 and (Y+i) != 9 and Board[Y+i][X-i] == InactivePlayer):
                        #increment the number of pieces found
                        i+=1
                    possibleActivePlayerScore += i
                    if(X-i != 0 and Y+i != 9 and ([X-i,Y+i] in Board) == False and Board[Y+i][X-i] != ActivePlayer):
                        #check the bounds of the possible playable position and that its already not taken
                        possibleMoves.append([X-i,Y+i])
                        AdditiveScores.append(possibleActivePlayerScore)
                possibleActivePlayerScore = 0
                #check for the inactive player's piece West of the active player's piece and make sure its not out of bounds
                if((X-1) != 9 and Board[Y][X-1] == InactivePlayer):
                    i = 1
                    #Check the lane for more of the inactive player's pieces
                    while((X-i) != 9 and Board[Y][X-i] == InactivePlayer):
                        #increment the number of pieces found
                        i+=1
                    possibleActivePlayerScore += i
                    if(X-i != 0 and ([X-i,Y] in Board) == False and Board[Y][X-i] != ActivePlayer):
                        #check the bounds of the possible playable position and that its already not taken
                        possibleMoves.append([X-i,Y])
                        AdditiveScores.append(possibleActivePlayerScore)
                possibleActivePlayerScore = 0
                #check for the inactive player's piece North West of the active player's piece and make sure its not out of bounds
                if((X-1) != 0 and (Y-1) != 0 and Board[Y-1][X-1] == InactivePlayer):
                    i = 1
                    #Check the lane for more of the inactive player's pieces
                    while((X-i) != 0 and (Y-i) != 0 and Board[Y-i][X-i] == InactivePlayer):
                        #increment the number of pieces found
                        i+=1
                    possibleActivePlayerScore += i
                    if(X-i != 0 and Y-i != 0 and ([X-i,Y-i] in Board) == False and Board[Y-i][X-i] != ActivePlayer):
                        #check the bounds of the possible playable position and that its already not taken
                        possibleMoves.append([X-i,Y-i])
                        AdditiveScores.append(possibleActivePlayerScore)
                    #print()
            X += 1
        Y += 1
        X = 0
    #Return the array of all possible moves
    return possibleMoves, AdditiveScores

#Make sure the move is not already taken
def isMoveTaken(Board, newMove, ActivePlayer, InactivePlayer):
    #split the desired move
    if(Board[newMove[1]][newMove[0]] == " "):
        return False
    elif(Board[newMove[1]][newMove[0]] == ActivePlayer or Board[newMove[1]][newMove[0]] == InactivePlayer):
        return True
    else:
        print("Error")
        return -1


#Make sure the move that is taking place is legal
def moveChecker(Board, userInput, ActivePlayer, InactivePlayer):
    #convert the desired move into an easier format. ie [5,6]
    wantedPosition = ABC_Conversion(userInput)
    #see if the move is already occupied
    if(isMoveTaken(Board, wantedPosition, ActivePlayer, InactivePlayer)):
        #if so, get a new input and check it
        userInput = input("This move is already taken, please give another valid move: ").lower()
        wantedPosition = moveChecker(Board, userInput, ActivePlayer, InactivePlayer)
    #find all possible moves
    possibleMoves, notneeded = moveCalculator(Board, ActivePlayer, InactivePlayer)
    #see if the desired move is in the list of possible moves
    isMovePossible = wantedPosition in possibleMoves
    if(not isMovePossible):
        #if the move is not possible, get another and check it
        userInput = input("invalid move, please give a valid move: ").lower()
        wantedPosition = moveChecker(Board, userInput, ActivePlayer, InactivePlayer)
    return wantedPosition

def makeMove(Board, newMove, ActivePlayer, InactivePlayer, ActivePlayerScore, InactivePlayerScore):
    #insert the move
    Board[newMove[1]][newMove[0]] = ActivePlayer
    #add 1 point for the piece being placed
    ActivePlayerScore += 1
    #change any inactive player pieces to the active player pieces
    #check for inactive pieces just like moveCalculator()
    #Check North pos for inactive player's pieces
    if((newMove[1]-1) != 0 and Board[newMove[1]-1][newMove[0]] == InactivePlayer):
        i = 1
        while((newMove[1]-i) != 0 and Board[newMove[1]-i][newMove[0]] == InactivePlayer):
            #check the bound and look for an active player piece that out flanks it
            if((newMove[1]-i-1) != 0 and Board[newMove[1]-i-1][newMove[0]] == ActivePlayer):
                for t in range(i+1):
                    #change the position to an active player piece
                    Board[newMove[1]-t][newMove[0]] = ActivePlayer
                #update score
                ActivePlayerScore += i
                InactivePlayerScore -= i
            i+=1
    #Check North East
    if((newMove[1]-1) != 0 and (newMove[0]+1) != 9 and Board[newMove[1]-1][newMove[0]+1] == InactivePlayer):
        i = 1
        while((newMove[1]-i) != 0 and (newMove[0]+i) != 9 and Board[newMove[1]-i][newMove[0]+i] == InactivePlayer):
             #check the bound and look for an active player piece that out flanks it
            if((newMove[1]-i-1) != 0 and (newMove[0]+i+1) != 9 and Board[newMove[1]-i-1][newMove[0]+i+1] == ActivePlayer):
                for t in range(i+1):
                    #change the position to an active player piece
                    Board[newMove[1]-t][newMove[0]+t] = ActivePlayer
                #update score
                ActivePlayerScore += i
                InactivePlayerScore -= i
            i+=1
    #Check East
    if((newMove[0]+1) != 9 and Board[newMove[1]][newMove[0]+1] == InactivePlayer):
        i = 1
        while((newMove[0]+i) != 9 and Board[newMove[1]][newMove[0]+i] == InactivePlayer):
             #check the bound and look for an active player piece that out flanks it
            if((newMove[0]+i+1) != 9 and Board[newMove[1]][newMove[0]+i+1] == ActivePlayer):
                for t in range(i+1):
                    #change the position to an active player piece
                    Board[newMove[1]][newMove[0]+t] = ActivePlayer
                #update score
                ActivePlayerScore += i
                InactivePlayerScore -= i
            i+=1
    #Check South East
    if((newMove[1]+1) != 9 and (newMove[0]+1) != 9 and Board[newMove[1]+1][newMove[0]+1] == InactivePlayer):
        i = 1
        while((newMove[1]+i) != 9 and (newMove[0]+i) != 9 and Board[newMove[1]+i][newMove[0]+i] == InactivePlayer):
             #check the bound and look for an active player piece that out flanks it
            if((newMove[1]+i+1) != 9 and (newMove[0]+i+1) != 9 and Board[newMove[1]+i+1][newMove[0]+i+1] == ActivePlayer):
                for t in range(i+1):
                    #change the position to an active player piece
                    Board[newMove[1]+t][newMove[0]+t] = ActivePlayer
                #update score
                ActivePlayerScore += i
                InactivePlayerScore -= i
            i+=1
    #check south
    if((newMove[1]+1) != 9 and Board[newMove[1]+1][newMove[0]] == InactivePlayer):
        i = 1
        while((newMove[1]+i) != 9 and Board[newMove[1]+i][newMove[0]] == InactivePlayer):
             #check the bound and look for an active player piece that out flanks it
            if((newMove[1]+i+1) != 9 and Board[newMove[1]+i+1][newMove[0]] == ActivePlayer):
                for t in range(i+1):
                    #change the position to an active player piece
                    Board[newMove[1]+t][newMove[0]] = ActivePlayer
                #update score
                ActivePlayerScore += i
                InactivePlayerScore -= i
            i+=1
    #Check South West
    if((newMove[1]+1) != 9 and (newMove[0]-1) != 0 and Board[newMove[1]+1][newMove[0]-1] == InactivePlayer):
        i = 1
        while((newMove[1]+i) != 9 and (newMove[0]-i) != 0 and Board[newMove[1]+i][newMove[0]-i] == InactivePlayer):
             #check the bound and look for an active player piece that out flanks it
            if((newMove[1]+i+1) != 9 and (newMove[0]-i-1) != 0 and Board[newMove[1]+i+1][newMove[0]-i-1] == ActivePlayer):
                for t in range(i+1):
                    #change the position to an active player piece
                    Board[newMove[1]+t][newMove[0]-t] = ActivePlayer
                #update score
                ActivePlayerScore += i
                InactivePlayerScore -= i
            i+=1
    #Check West
    if((newMove[0]-1) != 0 and Board[newMove[1]][newMove[0]-1] == InactivePlayer):
        i = 1
        while((newMove[0]-i) != 0 and Board[newMove[1]][newMove[0]-i] == InactivePlayer):
             #check the bound and look for an active player piece that out flanks it
            if((newMove[0]-i-1) != 0 and Board[newMove[1]][newMove[0]-i-1] == ActivePlayer):
                for t in range(i+1):
                    #change the position to an active player piece
                    Board[newMove[1]][newMove[0]-t] = ActivePlayer
                #update score
                ActivePlayerScore += i
                InactivePlayerScore -= i
            i+=1
    #Check North West
    if((newMove[1]-1) != 0 and (newMove[0]-1) != 0 and Board[newMove[1]-1][newMove[0]-1] == InactivePlayer):
        i = 1
        while((newMove[1]-i) != 0 and (newMove[0]-i) != 0 and Board[newMove[1]-i][newMove[0]-i] == InactivePlayer):
             #check the bound and look for an active player piece that out flanks it
            if((newMove[1]-i-1) != 0 and (newMove[0]-i-1) != 0 and Board[newMove[1]-i-1][newMove[0]-i-1] == ActivePlayer):
                for t in range(i+1):
                    #change the position to an active player piece
                    Board[newMove[1]-t][newMove[0]-t] = ActivePlayer
                #update score
                ActivePlayerScore += i
                InactivePlayerScore -= i
            i+=1

    return Board, ActivePlayerScore, InactivePlayerScore

def minimax(Board, possibleMove, additiveScore, depth, alpha, beta, maximizingPlayer, p2S, p1S):
    #get the possible moves so we can make sure there are possible moves to make
    possibleMovesforY, notneeded = moveCalculator(Board, "O","X")
    possibleAIMove = []
    #if no possible moves or the depth == 0, then send the desired move and its heuristic back
    if(depth == 0 or len(possibleMovesforY) == 0):
        return possibleMove, additiveScore
    #maximise the heuristic
    if(maximizingPlayer):
        #set the maxeval to -inf so it will change
        maxEval = -math.inf
        #make the possible move to go deeper in the minmax tree
        newBoard, p2S, p1S = makeMove(Board, possibleMove, "O", "X", p2S, p1S)
        #update the game state checks
        global TotalnumberofGameStatesChecked
        TotalnumberofGameStatesChecked += 1
        #Get new possible moves
        possibleMovesforX, PossibleAddingScores = moveCalculator(Board, "X","O")
        #show the board for each move
        if(DEBUG):
            print("display board in max node")
            displayBoard(newBoard)
        #iterate through the possible moves
        for i in range(len(possibleMovesforX)):
            #make the move on a different board then find the possible moves for the next player
            possibleAIMove, hueristicValue= minimax(Board, possibleMovesforX[i], PossibleAddingScores[i], depth-1, alpha, beta, False, p2S, p1S)
            #update the game state checks
            TotalnumberofGameStatesChecked += 1
            #update the maxeval and alpha values
            maxEval = max(maxEval, hueristicValue)
            alpha = max(alpha, hueristicValue)
            #more debug statments
            if(DEBUG):
                print("Possible Move of the AI is : ", possibleAIMove)
                print("With a Hueristic Value of: ", hueristicValue)
            #alpha-beta pruning, if ABp is false, then it no run
            if(beta <= alpha and ABP == True):
                break
        return possibleAIMove, maxEval
    #Minimise the heuristic
    else:
        #update mineval to inf so it has to change
        minEval = math.inf
        #make the possible move
        newBoard, p1S, p2S = makeMove(Board, possibleMove, "X", "O", p1S, p2S)
        #update the game state move
        TotalnumberofGameStatesChecked += 1
        #get new possible moves
        possibleMovesforY, PossibleAddingScores = moveCalculator(Board, "O","X")
        #show board for each move made
        if(DEBUG):
            print("display board in mini node")
            displayBoard(newBoard)
        for i in range(len(possibleMovesforY)):
            #make the move on a different board then find the possible moves for the next player
            possibleAIMove, hueristicValue = minimax(Board, possibleMovesforY[i], PossibleAddingScores[i], depth-1, alpha, beta, True, p2S, p1S)
            #update the game state check
            TotalnumberofGameStatesChecked += 1
            #update the mineval and beta values
            minEval = min(minEval, hueristicValue)
            beta = min(beta, hueristicValue)
            #show the possible moves and their corresponding heuristic value
            if(DEBUG):
                print("Possible Move of the AI is : ", possibleAIMove)
                print("With a Hueristic Value of: ", hueristicValue)
            #alpha-beta pruning, if ABp is false, then it no run
            if(beta <= alpha and ABP == True):
                break
        #Return the move and its hueristic
        return possibleAIMove, minEval
        

def TracePreviousGame(Board):
    #open the previous game file
    #Note: There may be a GameMoves file within another folder so it doesn't get changed.
    #To run that file, make a copy of it and put it in the same folder as the program and delete any copies of it
    f = open("GameMoves.txt", "r")

    #set scores and initialize Move
    P1Score = 2
    P2Score = 2
    Move = " "

    #continue to read move until f is at the end of the file
    while(Move != ""):
        displayBoard(Board)
        Move = f.readline()
        #ask about settings
        giveninput = input("Would you like to change any settings? [y/n]: ").lower()
        if(giveninput == 'y'):
            depth = int(settings())
        if(DEBUG):
            print("DEBUG Mode On")
            print("All game states will be displayed")
         #if at the end of the file, get out of the while loop or it will crash
        if(Move == ""):
            break
        print("Player 1's Move:", Move)
        newMove = moveChecker(Board, Move, "X", "O")
        Board, P1Score, P2Score = makeMove(Board, newMove, "X", "O", P1Score, P2Score)
        print("Score: Player 1 = ", P1Score, " Player 2 = ", P2Score)
        #ask about settings
        giveninput = input("Would you like to change any settings? [y/n]: ").lower()
        if(giveninput == 'y'):
            depth = int(settings())
        if(DEBUG):
            print("DEBUG Mode On")
            print("All game states will be displayed")
        input("Press enter to continue...")
        displayBoard(Board)
        Move = f.readline()
        #if at the end of the file, get out of the while loop or it will crash
        if(Move == ""):
            break
        print("Player 2's Move:", Move)
        newMove = moveChecker(Board, Move, "O", "X")
        Board, P2Score, P1Score = makeMove(Board, newMove, "O", "X", P2Score, P1Score)
        print("Score: Player 1 = ", P1Score, " Player 2 = ", P2Score)
        input("Press enter to continue...")
    #closer the file and dictate who won the game
    f.close()
    print("\nGame Over")
    print("Score: Player 1 = ", P1Score, " Player 2 = ", P2Score)
    if(P1Score > P2Score):
        print("Player 1 has won the game!")
    elif(P2Score > P1Score):
        print("Player 2 has won the game!")
    elif(P1Score == P2Score):
        print("The game has ended in a tie!")
    else:
        print("Scoring Error")


def Multiplayer(Board):
    #initialize Variables
    GameInProgress = True
    P1Score = 2
    P2Score = 2
    currentRound = 0

    #State who is what and who goes first
    print("Player 1 will go first and is X")
    print("Player 2 will go second and is O")

    #Start the Game
    while(GameInProgress):
        #Tell player what turn it is and show them what an input looks like
        currentRound += 1
        print("\nWhen Inputting your move, use the notation: Column Row. Ex: a4")
        print("Current Round: ", currentRound)
        #Show Board
        displayBoard(Board)
        #Player 1's turn
        #Check if the game is over
        possibleMovesforX, notneeded = moveCalculator(Board, "X","O")
        possibleMovesforY, notneeded = moveCalculator(Board, "O","X")
        #Check for Possible Moves
        #if there is moves, then let the player make a move
        if(len(possibleMovesforX) > 0):
            userInput = input("Player 1's (X) move: ").lower()
            newMove = moveChecker(Board, userInput, "X", "O")
            Board, P1Score, P2Score = makeMove(Board, newMove, "X", "O", P1Score, P2Score)
            displayBoard(Board)
        #if no moves, skip the players turn
        else:
            print("Player 1 has no possible moves so skipping their turn")

        #if neither player can make a move, the game is over
        if(len(possibleMovesforX) == 0 and len(possibleMovesforY) == 0):
            break
        #Display the score
        print("Score: Player 1 = ", P1Score, " Player 2 = ", P2Score)

        #Player 2's Turn:
        currentRound += 1
        print("Current Round: ", currentRound)
        #find all possible moves
        possibleMovesforX, notneeded = moveCalculator(Board, "X","O")
        possibleMovesforY, notneeded = moveCalculator(Board, "O","X")
        #determine if the player can make a move.
        #if so, do it
        if(len(possibleMovesforY) > 0):
            userInput = input("Player 2's (O) move: ").lower()
            newMove = moveChecker(Board, userInput, "O", "X")
            Board, P2Score, P1Score = makeMove(Board, newMove, "O", "X", P2Score, P1Score)
            displayBoard(Board)
        #if not, skip
        else:
            print("Player 2 has no possible moves so skipping their turn")

        #Check if the game is over
        if(len(possibleMovesforX) == 0 and len(possibleMovesforY) == 0):
            break

        #display scores
        print("Score: Player 1 = ", P1Score, " Player 2 = ", P2Score)
    #once the while loop ends, dictate who won and display scores
    print("\nGame Over")
    print("Score: Player 1 = ", P1Score, " Player 2 = ", P2Score)
    if(P1Score > P2Score):
        print("Player 1 has won the game!")
    elif(P2Score > P1Score):
        print("Player 2 has won the game!")
    elif(P1Score == P2Score):
        print("The game has ended in a tie!")
    else:
        print("Scoring Error")

    
def Singleplayer(Board):
    #initialize variables
    GameInProgress = True
    P1Score = 2
    P2Score = 2
    currentRound = 0
    depth = 3

    #Open a file so we can save the moves made for tracing later on
    f = open('GameMoves.txt', 'w')

    #Tell who goes first and what pices they will be
    print("Player 1 will go first and is X")
    print("Player 2 will go second and is O")

    #ask player if they want to go first or second
    fsinput = input("Would you like to go first or second? [f/s]").lower()

    #start game
    while(GameInProgress):
        print()
        #ask about settings
        giveninput = input("Would you like to change any settings? [y/n]: ").lower()
        if(giveninput == 'y'):
            depth = int(settings())
        if(DEBUG):
            print("DEBUG Mode On")
            print("All game states will be displayed")

        #PLAYER GOES FIRST
        if(fsinput == "f"):
            currentRound += 1
            print("\nWhen Inputting your move, use the notation: Column Row. Ex: a4")
            print("Current Round: ", currentRound)
            displayBoard(Board)
            #Player 1's turn
            #Check if the game is over
            possibleMovesforX, notneeded = moveCalculator(Board, "X","O")
            possibleMovesforY, notneeded = moveCalculator(Board, "O","X")
            #Check for possible moves
            #if so, move
            if(len(possibleMovesforX) > 0):
                #get player move
                userInput = input("Player 1's (X) move: ").lower()
                #check it and put it in a better format
                newMove = moveChecker(Board, userInput, "X", "O")
                #make the move and update scores
                Board, P1Score, P2Score = makeMove(Board, newMove, "X", "O", P1Score, P2Score)
                #update the file with the new move
                f.write(rev_ABC_Conversion(newMove))
                #Show board
                displayBoard(Board)
            #if no moves, skip
            else:
                print("Player 1 has no possible moves so skipping their turn")

            #if neither can move, game is over
            if(len(possibleMovesforX) == 0 and len(possibleMovesforY) == 0):
                break

            #show score
            print("Score: Player 1 (You) = ", P1Score, " Player 2 = ", P2Score)

            #Player 2's Turn:
            #get all possible moves for depth 1
            print("Ai's turn.")
            #tell if alpha-beta pruning (ABP) is on or off
            if(ABP):
                print("Alpha-Beta Pruning is on!")
            else:
                print("Alpha-Beta Pruning is off!")
            #display the current depth
            print("Current depth is = ", depth)

            #get possible moves and their possible score additions
            possibleMovesforX, notneeded = moveCalculator(Board, "X","O")
            possibleMovesforY, Temp = moveCalculator(Board, "O","X")

            #rest list and total
            listofAdditiveScores = []
            TotalnumberofGameStatesChecked = 0

            #check for possible moves
            if(len(possibleMovesforY) > 0):
                #make a copy of the board, deepcopy makes a whole new copy.
                #if the board is just 'copyofboard = board' does not work
                #the original board is still affected, possibly copying the location rather than the list 
                pseudoBoard = copy.deepcopy(Board)
                #Each possible move will become the root node for the min max tree
                for i in range(len(possibleMovesforY)):
                    #get the heuristic for each current possible move
                    aimove, possibleAdditiveScore = minimax(pseudoBoard, possibleMovesforY[i], Temp[i], depth, -math.inf, math.inf, True, P2Score, P1Score)
                    #add to the list
                    listofAdditiveScores.append(possibleAdditiveScore)
                    #update the game state checks
                    TotalnumberofGameStatesChecked += 1
                #show the number of game state checked
                print("Number of Game States checked",TotalnumberofGameStatesChecked)
                #determine which would give the most number of pieces
                bestMove = listofAdditiveScores[0]
                for t in range(len(listofAdditiveScores)):
                    bestMove = max(bestMove, listofAdditiveScores[t])
                #make the move
                Board, P2Score, P1Score = makeMove(Board, possibleMovesforY[listofAdditiveScores.index(bestMove)], "O", "X", P2Score, P1Score)
                #record the move
                f.write(rev_ABC_Conversion(possibleMovesforY[listofAdditiveScores.index(bestMove)])) 
            #if no move, skip the ai's turn
            else:
                print("Player 2 has no possible moves so skipping their turn")

            #if neither can move, game over
            if(len(possibleMovesforX) == 0 and len(possibleMovesforY) == 0):
                break

            #display scores
            print("Score: Player 1 (You) = ", P1Score, " Player 2 = ", P2Score)

        #PLAYER GOES SECOND
        elif(fsinput == "s"):
            print("\nWhen Inputting your move, use the notation: Column Row. Ex: a4")
            print("Current Round: ", currentRound)
            displayBoard(Board)
            #Player 1's Turn:
            #get all possible moves for depth 1
            print("Ai's turn.")

            #tell if alpha-beta pruning (ABP) is on or off
            if(ABP):
                print("Alpha-Beta Pruning is on!")
            else:
                print("Alpha-Beta Pruning is off!")
            #display the current depth
            print("Current depth is = ", depth)

            #get possible moves and their possible score additions
            possibleMovesforX, Temp = moveCalculator(Board, "X","O")
            possibleMovesforY, notneeded = moveCalculator(Board, "O","X")

            #rest list and total
            listofAdditiveScores = []
            TotalnumberofGameStatesChecked = 0

            #check for possible moves
            if(len(possibleMovesforX) > 0):
                #make a copy of the board, deepcopy makes a whole new copy.
                pseudoBoard = copy.deepcopy(Board)
                #Each possible move will become the root node for the min max tree
                for i in range(len(possibleMovesforX)):
                    #get the heuristic for each current possible move
                    aimove, possibleAdditiveScore = minimax(pseudoBoard, possibleMovesforX[i], Temp[i], depth, -math.inf, math.inf, True, P1Score, P2Score)
                    #add to the list
                    listofAdditiveScores.append(possibleAdditiveScore)
                    #update the game state checks
                    TotalnumberofGameStatesChecked += 1
                #show the number of game state checked
                print("Number of Game States checked",TotalnumberofGameStatesChecked)
                 #determine which would give the most number of pieces
                bestMove = listofAdditiveScores[0]
                #determine which would give the most number of pieces
                for t in range(len(listofAdditiveScores)):
                    bestMove = max(bestMove, listofAdditiveScores[t])
                #make the move
                Board, P1Score, P2Score = makeMove(Board, possibleMovesforX[listofAdditiveScores.index(bestMove)], "X", "O", P1Score, P2Score)
                #record the move
                f.write(rev_ABC_Conversion(possibleMovesforX[listofAdditiveScores.index(bestMove)])) 
            #if no move, skip the ai's turn
            else:
                print("Player 1 has no possible moves so skipping their turn")

            #if neither can move, game over
            if(len(possibleMovesforX) == 0 and len(possibleMovesforY) == 0):
                break
            
            #display scores and board
            displayBoard(Board)
            print("Score: Player 1 = ", P1Score, " Player 2 (You) = ", P2Score)

            #Player 2's turn
            #Check if the game is over
            possibleMovesforX, notneeded = moveCalculator(Board, "X","O")
            possibleMovesforY, notneeded = moveCalculator(Board, "O","X")
            if(len(possibleMovesforY) > 0):
                #get move from player
                userInput = input("Player 2's (O) move: ").lower()
                #check if move is legal and format it
                newMove = moveChecker(Board, userInput, "O", "X")
                #make the move
                Board, P2Score, P1Score = makeMove(Board, newMove, "O", "X", P2Score, P1Score)
                #record the move
                f.write(rev_ABC_Conversion(newMove))
                #display updated board
                displayBoard(Board)
            #if no moves possible, skip turn
            else:
                print("Player 2 has no possible moves so skipping their turn")
            
            #if neither can play, game over
            if(len(possibleMovesforX) == 0 and len(possibleMovesforY) == 0):
                break

            #show scores
            print("Score: Player 1 = ", P1Score, " Player 2 (You) = ", P2Score)
    #close file and dictate who won
    f.close()
    print("\nGame Over")
    print("Score: Player 1 = ", P1Score, " Player 2 = ", P2Score)
    if(P1Score > P2Score):
        print("Player 1 has won the game!")
    elif(P2Score > P1Score):
        print("Player 2 has won the game!")
    elif(P1Score == P2Score):
        print("The game has ended in a tie!")
    else:
        print("Scoring Error")


def settings():
    #call global variables
    global DEBUG
    global ABP
    #ask if they wanna change these settings, if so change them
    userinput = input("Would you like to turn on the DEBUG Mode? [y/n]: ").lower()
    if(userinput == "y"):
        DEBUG = True
    elif(userinput):
        DEBUG = False
    userinput = input("Turn on/off alpha-beta pruning? (It's on by default) ").lower()
    if(userinput == "on"):
        ABP = True
    elif(userinput == "off"):
        ABP = False
    userinput = input("Would you like to change the search depth of the minmax tree? (depth is 3 by default) [y/n]: ").lower()
    if(userinput == "y"):
        newDepth = input("Please give an integer for the depth search. (number has to be larger than 0): ")
    else:
        newDepth = 3
    print("Returning to the game")
    return newDepth

def displayBoard(Board):
    #iterate through the 2D array and split the indices with a pipe
    for r in Board:
        for c in r:
            print(c,end = "|")
        print()


def InitialMenu(Board):
    #welcome player then as if they wanna play a certain mode, watch a prev game, or leave
    print("Welcome to Othello!")
    while(True):
        userInput = input("Would you like to: \n[2p] Play vs another person \n[ai] Play vs an AI \n[t] Trace a previous Game \n[q] Quit\n\n").lower()
        if(userInput == "2p"):
            Multiplayer(Board)
            break
        elif(userInput == "ai"):
            Singleplayer(Board)
            break
        elif(userInput == "t"):
            TracePreviousGame(Board)
            break
        elif(userInput == "q"):
            exit(0)
        else:
            print("Invalid Input")


def main():
    #create board
    Board = [[" ","A","B","C","D","E","F","G","H"],
            ["1"," "," "," "," "," "," "," "," "],
            ["2"," "," "," "," "," "," "," "," "],
            ["3"," "," "," "," "," "," "," "," "],
            ["4"," "," "," ","X","O"," "," "," "],
            ["5"," "," "," ","O","X"," "," "," "],
            ["6"," "," "," "," "," "," "," "," "],
            ["7"," "," "," "," "," "," "," "," "],
            ["8"," "," "," "," "," "," "," "," "]]

    #Send the user to the Main Menu
    InitialMenu(Board)

#Start the program
main()
