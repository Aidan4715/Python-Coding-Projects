def sum(my_list):
    total = 0
    for i in my_list:
        total = total + my_list[i]
    return total

def average(my_list):
    total = 0
    count = 0
    for i in my_list:
        total = total + my_list[i]
        count = count + 1
    return total/count
