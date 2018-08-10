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
            return ""


