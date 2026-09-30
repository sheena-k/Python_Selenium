import openpyxl
from openpyxl.utils import get_column_letter


class ExcelUtility:
    def __init__(self, file_path):
        # Initialize with the file path to the Excel file
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(file_path)


    def get_string_data(self, row, col, sheet_name):
        """Get a string value from a specific cell (row, column)"""
        sheet = self.workbook[sheet_name]
        cell_value = sheet.cell(row=row, column=col)  # openpyxl uses 1-based indexing
        return str(cell_value.value)

    def get_integer_data(self, row, col, sheet_name):
        """Get an integer value from a specific cell (row, column)"""
        sheet = self.workbook[sheet_name]
        cell_value = sheet.cell(row=row, column=col)  # openpyxl uses 1-based indexing
        # Ensuring the cell contains a number and then casting to int
        return int(cell_value.value) if cell_value.value is not None else None