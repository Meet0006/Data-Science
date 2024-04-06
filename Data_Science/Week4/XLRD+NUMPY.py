import numpy as np
import xlrd

loc = ('mydata.xlsx')
work_book = xlrd.open_workbook(loc)
sheet2 = work_book.sheet_by_index(1)

# ADVANCE : XLRD + NUMPY

# Perform operation on storedata.xlsx
# https://www.infolabz.in/resources/index.html

# Fetch data from xlrd and store(append) it in variable februarydata
februarydata = []
for i in range(1, sheet2.nrows):
    februarydata.append(int(sheet2.cell_value(i, 2)))
print(februarydata)

# Convert februarydatato numpy array name it februarydatanp
februarydatanp = np.array(februarydata)
print(februarydatanp)

# Print count of minimum product sold, maximum product sold, total product sold.
print(np.min(februarydatanp))
print(np.max(februarydatanp))
print(np.sum(februarydatanp))

# Create a mask of 50+ products sold.
mask = 50 < februarydatanp
print(februarydatanp[mask])

# Apply mask in March data.
Marchdata = []
for i in range(1, sheet2.nrows):
    Marchdata.append(int(sheet2.cell_value(i, 3)))
marchdatanp = np.array(Marchdata)
March_mask = marchdatanp % 2 == 0
print(March_mask)

# Print how many categories observed sell of 50+ products in August month.
AUGUST_Array = []
for i in range(1, sheet2.nrows):
    AUGUST_Array.append(int(sheet2.cell_value(i, 8)))
AUGUSTdatanp = np.array(AUGUST_Array)
AUGUSTMask = 50 < AUGUSTdatanp
print(len(AUGUSTdatanp[AUGUSTMask]))
