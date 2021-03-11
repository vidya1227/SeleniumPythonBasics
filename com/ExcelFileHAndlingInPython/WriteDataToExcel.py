import openpyxl
#createExcel = open('E:\\CreateWrite.xlsx', 'w')

path = 'E:\\CreateWrite.xlsx'

wb = openpyxl.load_workbook(path)
sheet = wb.active

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(row=r, column=c).value='Welcome'

wb.save(path)

