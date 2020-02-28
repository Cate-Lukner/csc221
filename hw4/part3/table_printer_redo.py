''' Table Printer practice project

Author: Cate Lukner
'''

COLUMN_WIDTH=25

def set_col_widths(lst):
    ''' Check if length of each string is shorter than the set COLUMN_WIDTH'''
    max_lengths = []
    for i in range(len(lst) - 1):
        max_len = len(max(lst[i], key=len))
        max_lengths.append(max_len)
    return max_lengths 

def printTable(tableData):
    '''given list of strings, tableData, displays in a 
    well-organized table with each column right-justified'''
    colWidths = set_col_widths(tableData) 
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i], end=' ')
        print()
