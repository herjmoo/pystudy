################################################################################
# baseball.py
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

import random
from lib.string import *


class Baseball:
    def __init__(self):
        self.ans_len = 3
        self.limit = 10

    def setup_ans_len(self, n):
        if n > 10:
            print("No support, the length of answer should be less or equal than 10")
            return
        self.ans_len = n
        print("Length of answer is set to {0}".format(n))

    def setup_try_limit(self, n):
        self.limit = n
        print("Limit of try(ies) is set to {0}".format(n))

    def start(self):
        print("==================== GAME START ====================")

        # Generate random numbers
        ans = ""
        while check_duplication(ans):
            ans = ""
            for i in range(self.ans_len):
                ans += str(int(random.random() * 10))

        guess = ""
        tries = 0
        while guess != ans and tries < self.limit:

            # Check the input numbers
            guess = ""
            while len(guess) != self.ans_len or check_duplication(guess):
                guess = input("Enter the {0} digit number with no duplication: ".format(self.ans_len))

            # Check the numbers and count Strike and Ball
            strike = 0
            ball = 0
            for idx in range(self.ans_len):
                if ans[idx] == guess[idx]:
                    strike += 1
                elif guess.count(ans[idx]):
                    ball += 1
            print("{0}S{1}B".format(strike, ball))

            tries += 1

        if tries == 1:
            print("Go out and get Powerball tickets")
        elif guess == ans:
            print("Congratulation!!! You did it on {0} tries".format(tries))
        else:
            print("Sorry you lose. The answer is " + ans)

        print("==================== GAME END ====================")
