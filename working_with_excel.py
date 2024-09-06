import openpyxl
import openpyxl.workbook

# Either load an existing workbook or open an empty sheet

# Empty sheet -> 
# openpyxl.workbook()

# Load an existing workboook:

wb = openpyxl.load_workbook("transactions.xlsx")
print(wb.sheetnames)
print(wb["Sheet1"])  #It is case-sensitive. 

# Few methods on workbook objects are wb.create_sheet and wb.remove_sheet

# Accessing attributes. 
sheet = wb["Sheet1"]
cell = sheet["a1"]
# print(cell.value)
# You can also change the value of the cell, cell.value = 1
# We have row, column, and coordinate for each cell
# print(cell.row)
# print(cell.column)
# print(cell.coordinate)

# Instead of calling individual row, column, coordinate. Instead of using square bracket, we can use the cell object on the sheet

cells = sheet.cell(row=1, column=1) # This is equivalent of cell = sheet["a1"]
print("Cells of transactions", cells)

# Dynamic access to cells. 
print("Max row: ", sheet.max_row)
print("Max column: ", sheet.max_column)

# We can easily iterate over the rows and columns. 

for row in range(1, sheet.max_row):
    for column in range(1, sheet.max_column+1):
        cell = sheet.cell(row, column)
        print("Cell values using the functional approach:", cell.value)

# You can also use the bracket approach
column1 = sheet["A"]
print(column1) # This will give a tuple
# You can access all columns at once using the range within the square bracket

columns = sheet["A:C"]
print("All columns using square bracket: ", columns) #It gives tuples of tuples

# Inner tuples are columns

# Coordinates can also be used

column_coordinates = sheet["a1:c3"]
print(column_coordinates)

# Sheet has few methods that I should be aware of:
# 1. append, 2. insert_rows (To insert a row at a given index), 3. insert_columns, 4. delete_rows, 5. delete_columns

# wb.save("transactions.xlsx")
