################################################################################
# play_game.py
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

from game.baseball import *
from game.rps import *

print("1. Baseball")
print("2. (coming soon)")
print("3. (coming soon)")
n = input("Select the game: ")

if n == "1":
    print("Baseball game configurations")
    b = Baseball()

    difficulty = input("Select the difficulty (Easy/Normal/Hard): ")
    if difficulty == "Easy":
        print("Difficulty is set to Easy")
        b.setup_ans_len(3)
        b.setup_try_limit(20)
    elif difficulty == "Normal":
        print("Difficulty is set to Normal")
        b.setup_ans_len(3)
        b.setup_try_limit(10)
    elif difficulty == "Hard":
        print("Difficulty is set to Hard")
        b.setup_ans_len(3)
        b.setup_try_limit(7)
    else:
        print("Unrecognizable difficulty")
        print("Difficulty is set to Normal")
        b.setup_ans_len(3)
        b.setup_try_limit(10)

    b.start()

elif n == "2":
    print("let's play RockPaperScissors!")
    g=RockPaperScissors()
    g.start()

elif n == "3":
    print("New game is developing, please try the next version later")