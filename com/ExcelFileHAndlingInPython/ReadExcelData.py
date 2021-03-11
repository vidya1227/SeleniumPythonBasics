#E:\SampleTestData.xlsx
# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("E:\\SampleTestData.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
#sheet = wb.sheet_by_index(0)
sheet = wb.sheet_by_name('Sheet1')

# For row 0 and column 0
#print(sheet.cell_value(1, 1))
#print(sheet.cell(0,4))


# 2 : Extract number of rows
# Program to extract number
# of rows using Python

# Give the location of the file
loc = ("E:\\SampleTestData.xlsx")

wb = xlrd.open_workbook(loc)
sheet1 = wb.sheet_by_index(0)
sheet1.cell_value(0, 0)

# Extracting number of rows
print(sheet.nrows)

# Extracting number of columns
print(sheet.ncols)

#4 : Extracting all columns name
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))

#extracting first column
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))

#6 : Extract a particular row value
print(sheet.row_values(1))


#reference: https://www.geeksforgeeks.org/reading-excel-file-using-python/


