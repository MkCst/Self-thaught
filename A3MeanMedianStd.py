import numpy as np

def format_list(lst, side_size):
    start = 0
    ft_lst = []
    for i in range(len(lst)+1):
        if i%side_size==0 and i>0:
            ft_lst.append(lst[start:i])
            start = i
    return ft_lst

def get_lists(lst, side_size):
    lst_rows= format_list(lst, side_size)
    lst_columns = []
    for i in range(side_size):
        for j in lst_rows:
            lst_columns.append(j[i])
    lst_columns = format_list(lst_columns, size)
    


