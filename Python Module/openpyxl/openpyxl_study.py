from __future__ import print_function

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_active_sheet()

for t in sheet.rows:
    for c in t:
        print(c.value, end=', ')
    print()

print('*' * 80)

for row in sheet['A2':'C3']:
    for c in row:
        print(c.value, end=', ')
    print()

avg_column = sheet.max_column + 1
sum_column = sheet.max_column + 2

cell = sheet.cell(row=1, column=avg_column)
cell.value = 'avg'

cell = sheet.cell(row=1, column=sum_column)
cell.value = 'sum'

for row in sheet['C2':'E11']:
    scores = [c.value for c in row]
    sum_score = sum(scores)
    avg_score = sum_score / len(scores)
    cell = sheet.cell(row=row[0].row, column=avg_column)
    cell.value = avg_score

    cell = sheet.cell(row=row[0].row, column=sum_column)
    cell.value = sum_score

wb.save('example_copy.xlsx')