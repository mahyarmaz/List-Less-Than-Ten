#Gets a list of numbers and returns those less than 10
list_name = []
list_name = (input('Please enter a list of numbers separated by space: '))
list = list_name.split()
new_list = []
for i in list:
    if int(i) < 10:
        new_list.append(i)
print(f'Your list of numbers below 10 are : {new_list}')


