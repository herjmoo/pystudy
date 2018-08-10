################################################################################
# rps.py
# Copyright (c) 2018, PyStudy-GoGoogle
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################
import sys
sys.path.append("/Users/jinasong/PycharmProjects/pystudy")

from random import randint
from lib.string import *

class RockPaperScissors:
    def __init__(self):
        self.ans_len = 3
        self.game_chance = 5

    def start(self):
        print("==================== GAME START ====================")
        print("You have a chance at five times! Ready? Ready!")

        # create a list of play options
        t = ["Rock", "Paper", "Scissors"]

        # assign a random play to the computer
        computer = t[randint(0, 2)]

        # set player to False
        game_num = 0
        player = False

        while game_num < self.game_chance:
            # set player to True
            player = input("Rock, Paper, Scissors?")
            if player == computer:
                print("Tie!")
            elif player == "Rock":
                if computer == "Paper":
                    print("You lose!", computer, "covers", player)
                else:
                    print("You win!", player, "smashes", computer)
            elif player == "Paper":
                if computer == "Scissors":
                    print("You lose!", computer, "cut", player)
                else:
                    print("You win!", player, "covers", computer)
            elif player == "Scissors":
                if computer == "Rock":
                    print("You lose...", computer, "smashes", player)
                else:
                    print("You win!", player, "cut", computer)
            else:
                print("That's not a valid play. Check your spelling!")
            # player was set to True, but we want it to be False so the loop continues
            game_num += 1
            player = False
            computer = t[randint(0, 2)]

        print("==================== GAME END ====================")

if __name__ == "__main__":
    g=RockPaperScissors()
    g.start()
