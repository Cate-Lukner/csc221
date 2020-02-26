''' Table Printer practice project

Author: Cate Lukner
'''

COLUMN_WIDTH=25

def check_length(lst):
    ''' Check if length of each string is shorter than the set COLUMN_WIDTH'''
    for i in range(len(lst)):
        if len(lst[i]) > (COLUMN_WIDTH + 1):
            print(f"""
            Sorry, this table printer as of now cannot
            take strings longer than length {COLUMN_WIDTH}. Eventually Cate
            will be a good enough programmer to figure out how
            to do that, or perhaps have the time to figure it out
            without dance compositon assignments looming over her head. 
            Seperate the longer strings into lengths less than {COLUMN_WIDTH}
            and try again.
            """)
            return False
    return True
     
def convert_list(lst):
    '''convert the given list into a dictionary'''
    # ensure the length of the list is even
    if len(lst) % 2 == 1:
        lst.append(' ')
    # reconstruct the list into a dictionary
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def printTable(tableData):
    '''given list of strings, tableData, displays in a 
    well-organized table with each column right-justified'''
    # create table if strings' lengths appropriate
    if check_length(tableData):
        rec_data = convert_list(tableData)
        for k, v in rec_data.items():
            print(k.rjust(COLUMN_WIDTH) + v.rjust(COLUMN_WIDTH)) 
