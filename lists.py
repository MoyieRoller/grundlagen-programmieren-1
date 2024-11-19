my_list = [1, 3, 6, 8, 5, 4, 8, 0, 2]
print(my_list)

my_list[0] = "overwritten"

#override last 3 elements
my_list[-3:] = [41,42,43]
del my_list[1]
print(my_list)

#does not delete the whole list
while True:
    if len(my_list) > 0:
        del my_list[-1]
        print(my_list)
    else:
        break