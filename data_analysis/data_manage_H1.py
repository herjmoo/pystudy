################################################################################
# data_manage_H1.py
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

import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)


class ManageH1:
    def __init__(self, data):
        self.data = data

    def print_all_data(self):
        print(self.data)

    def search_by_employer(self, name):
        if self.data.empty:
            print("No data loaded")
            return
        res = self.data['EMPLOYER_NAME'] == name
        new_data = self.data[res]
        print(new_data[['JOB_TITLE',
                       'WORKSITE_CITY',
                       'WORKSITE_STATE',
                       'EMPLOYER_CITY',
                       'EMPLOYER_STATE',
                       'PREVAILING_WAGE',
                       'PW_WAGE_LEVEL',
                       'WAGE_RATE_OF_PAY_FROM',
                       'WAGE_RATE_OF_PAY_TO',
                       'WAGE_UNIT_OF_PAY']])
