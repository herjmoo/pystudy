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
from data_analysis.data_manage_H1 import *


class Menu:
    def __init__(self):
        self.current_pos = 0
        self.filename = "H-1B_Disclosure_Data_FY2018-Q3"
        self.data = pd.DataFrame({})

    def goto(self, n):
        if self.current_pos == 0:
            if n == 0:
                exit(0)
            elif n == 1:
                self.current_pos = 1
            elif n == 2:
                self.current_pos = 2
            elif n == 3:
                self.current_pos = 3
            else:
                print("ERROR: Undefined menu")
        elif self.current_pos == 1:
            if n == 0:
                self.current_pos = 0
            elif n == 1:
                id = ImportData()
                filename = input("File name (default='" + self.filename + "'): ")
                if filename == "":
                    filename = self.filename
                self.data = id.panda_to_panda(filename)
            else:
                print("ERROR: Undefined menu")
        elif self.current_pos == 2:
            if n == 0:
                self.current_pos = 0
            elif n == 1:
                cd = ChangeData()
                filename = input("File name (default='" + self.filename + "'): ")
                if filename == "":
                    filename = self.filename
                res = cd.excel_to_panda(filename)
                if res != "":
                    print("'" + res + "' is created")
            elif n == 2:
                cd = ChangeData()
                filename = input("File name (default='" + self.filename + "'): ")
                if filename == "":
                    filename = self.filename
                res = cd.csv_to_panda(filename)
                if res != "":
                    print("'" + res + "' is created")
            else:
                print("ERROR: Undefined menu")
        elif self.current_pos == 3:
            m = ManageH1(self.data)
            if n == 0:
                self.current_pos = 0
            elif n == 1:
                m.print_all_data()
            elif n == 2:
                m.search_by_employer(input("Enter employer name: "))
            elif n == 3:
                m.search_by_jobtitle(input("Enter job title: "))
            elif n == 4:
                m.search_by_city(input("Enter city name: "))
            else:
                print("ERROR: Undefined menu")
        else:
            print("ERROR: Undefined menu")

    def print_string(self, data):
        print("# " + "{0: <96}".format(data) + " #")

    def print_menu(self):
        if self.current_pos == 0:
            self.print_string("0. Exit program")
            self.print_string("1. Import H1 data")
            self.print_string("2. Change H1 data")
            self.print_string("3. Manage H1 data")
        elif self.current_pos == 1:
            self.print_string("0. Back to previous menu")
            self.print_string("1. Import H1 data from panda format")
        elif self.current_pos == 2:
            self.print_string("0. Back to previous menu")
            self.print_string("1. Change H1 data from excel to panda")
            self.print_string("2. Change H1 data from csv to panda")
        elif self.current_pos == 3:
            self.print_string("0. Back to previous menu")
            self.print_string("1. Print all data")
            self.print_string("2. Search data by employer name")
            self.print_string("3. Search data by job title")
            self.print_string("4. Search data by city")
        else:
            self.print_string("ERROR: Undefined menu position")

    def print_header(self):
        print("")
        print("####################################################################################################")
        if self.data.empty:
            self.print_string("No Data")
        else:
            self.print_string(self.filename)
        print("# ================================================================================================ #")
        self.print_menu()
        print("####################################################################################################")

    def run(self):
        while True:
            menu.print_header()
            while True:
                n_str = input("Select the function: ")
                if n_str.isdigit():
                    n_num = int(n_str)
                    break
                else:
                    print("ERROR: Enter a number")
            self.goto(n_num)


menu = Menu()
menu.run()
