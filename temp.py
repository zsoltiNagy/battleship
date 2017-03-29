# for i in range(1, 10):  # we need a more elegant solution with rjust
#    print('  ', i, ' ', str_table_list[i - 1])
#print(' ', 10, ' ', str_table_list[9], '\n\n')


width = 80
for i in range(1, 10):
    print("{0:>{3}}{1:>{3}}{2:>{3}}".format(i, ' ', str_table_list[i - 1], width, '\n\n'))


#        if order == "count,asc":
#        for (i, j) in inventory_list:
#            print('{0:>{2}}{1:>{2}}'.format(j, i, width))
#    elif order == "count,desc":
#        for (i, j) in rev_inventory_list:
#            print('{0:>{2}}{1:>{2}}'.format(j, i, width))
#    else:
#        for item in inventory:
#            print('{0:>{2}}{1:>{2}}'.format(inventory[item], item, width))
