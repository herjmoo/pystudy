################################################################################
# play_data.py
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
from data_analysis.data import *

print("1. Change H1 data from excel to panda")
print("2. Change H1 data from csv to panda")
print("3. Import H1 data from panda to panda")
n = input("Select the function: ")

if n == "1":
    cd = ChangeData()
    cd.excel_to_panda("H-1B_Disclosure_Data_FY2018-Q3")

elif n == "2":
    cd = ChangeData()
    cd.csv_to_panda("H-1B_Disclosure_Data_FY2018-Q3")

elif n == "3":
    id = ImportData()
    data = id.panda_to_panda("H-1B_Disclosure_Data_FY2018-Q3")
    print(data.head(10))



