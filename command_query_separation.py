# Command query separation principle:

"""
    Our methods or functions should either be a command (that performs an action to change the state of the system) or a query (return an answer without changing the state of the system) but not both. 
"""

# Let's understand the principle using the transactions.xlsx workbook example


"""
// Let's load the workbook. 

wb = openxyl.load_workbook("transactions.xslx")
sheet = wb["sheet1"]
for row in range(1,10):
    cell = sheet.cell(row, 1)
    print(cell.value)

sheet.append([1,2,3])
wb.save("transactions2.xslx")

You only had four rows in the original excel file. So, accessing the sheet.cell(row,1) and then creating it if the row doesn't exist violates the command query principle. 

The solution will be to raise an exception if the cell doesn't exist and not allow the creation.

"""