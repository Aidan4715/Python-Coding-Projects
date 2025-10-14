def sum(my_list):
    total = 0
    for i in my_list:
        total = total + i
    return total

def average(my_list):
    average = sum(my_list)/len(my_list)
    return average
