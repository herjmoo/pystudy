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
import pickle


def to_panda(data, filename):
    f = open(filename + ".panda", 'wb')
    pickle.dump(data, f)
    f.close()
    return filename + ".panda"


class ChangeData:
    def excel_to_panda(self, filename):
        try:
            data = pd.read_excel(filename + ".xls")
            new_filename = to_panda(data, filename)
        except FileNotFoundError as e:
            try:
                data = pd.read_excel(filename + ".xlsx")
                new_filename = to_panda(data, filename)
            except FileNotFoundError as e:
                print("ERROR: No excel file named " + filename + " found")
                return ""

        return new_filename

    def csv_to_panda(self, filename):
        try:
            data = pd.read_csv(filename + ".csv")
            new_filename = to_panda(data, filename)
        except FileNotFoundError as e:
            print("ERROR: No csv file named " + filename + " found")
            return ""

        return new_filename


class ImportData:
    def panda_to_panda(self, filename):
        try:
            f = open(filename + ".panda", 'rb')
            return pickle.load(f)
        except OSError as e:
            print("ERROR: No panda file named " + filename + " found")
            return pd.DataFrame({})
