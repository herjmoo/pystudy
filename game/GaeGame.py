# Tic-Tac-Toe
import random

class Tic:
    def drawBoard(self,board):
        print(board[7] + '|' + board[8] + '|' + board[9])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[1] + '|' + board[2] + '|' + board[3])

    def inputPlayerLetter(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        if random.randint(0,1) == 0:
            return 'computer'
        else:
            return 'player'

    def makeMove(self,board,letter,move):
        board[move] = letter

    def isWinner(self,bo,le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or \
                (bo[4] == le and bo[5] == le and bo[6] == le) or \
                (bo[1] == le and bo[2] == le and bo[3] == le) or \
                (bo[7] == le and bo[4] == le and bo[1] == le) or \
                (bo[8] == le and bo[5] == le and bo[2] == le) or \
                (bo[9] == le and bo[6] == le and bo[3] == le) or \
                (bo[7] == le and bo[5] == le and bo[3] == le) or \
                (bo[9] == le and bo[5] == le and bo[1] == le))

    def getBoardCopy(self,board):
        boardCopy = []
        for i in board:
            boardCopy.append(i)
        return boardCopy

    def isSpaceFree(self,board, move):
        return board[move] == ' '

    def getPlayerMove(self,board):
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(self,board, movesList):
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board,i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None


    def getComputerMove(self, board, computerLetter):
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        for i in range(1,10):
            boardCopy = self.getBoardCopy(board)
            if self.isSpaceFree(boardCopy,i):
                return i
        for i in range(1,10):
            boardCopy = self.getBoardCopy(board)
            if self.isSpaceFree(boardCopy,i):
                self.makeMove(boardCopy,playerLetter,i)
                if self.isWinner(boardCopy,playerLetter):
                    return i

        move = self.chooseRandomMoveFromList(board, [1,3,7,9])
        if move != None:
            return move

        if self.isSpaceFree(board,5):
            return 5

        return self.chooseRandomMoveFromList(board,[2,4,6,8])


    def isBoardFull(self,board):
        for i in range(1,10):
            if self.isSpaceFree(board,i):
                return False
        return True

    def run(self):
        print('======== Welcome Tic-Tac-Toe ========')

        while True:
            theBoard = [' ']*10
            playerLetter, computerLetter = self.inputPlayerLetter()
            turn = self.whoGoesFirst()
            print('The'+ turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player':
                    self.drawBoard(theBoard)
                    move = self.getPlayerMove(theBoard)
                    self.makeMove(theBoard,playerLetter,move)

                    if self.isWinner(theBoard,playerLetter):
                        self.drawBoard(theBoard)
                        print('Hooray! You have won the game!')
                        gameIsPlaying = False
                    else:
                        if self.isBoardFull(theBoard):
                            self.drawBoard(theBoard)
                            print('the Game is a tie!')
                            break
                        else:
                            turn =  'computer'
                else:
                    move = self.getComputerMove(theBoard,computerLetter)
                    self.makeMove(theBoard, computerLetter, move)

                    if self.isWinner(theBoard,computerLetter):
                        self.drawBoard(theBoard)
                        print('The computer has beaten you! You lose.')
                        gameIsPlaying = False
                    else:
                        if self.isBoardFull(theBoard):
                            self.drawBoard(theBoard)
                            print('The game is a tie!')
                        else:
                            turn = 'player'
            print('Do you want to play again? (yes or no)')
            if not input().lower().startswith('y'):
                break

if __name__ == '__main__':
    a = Tic()
    a.run()


