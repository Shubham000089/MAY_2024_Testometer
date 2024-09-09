import openpyxl

files = "..\\testdata\\Test.xlsx"

class Excel:
    def read_data(self, sheet, cell_chords):
        self.workbook = openpyxl.load_workbook(files)
        self.sheet = self.workbook[sheet]
        return self.sheet[cell_chords].value