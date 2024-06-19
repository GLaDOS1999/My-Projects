# Test List
my_list = [1, 5, 2.3, 1, 1.1, 10, 3.14, 9, 11, 0, -1, -2.71]
# Actual Code
while not all(my_list[i] <= my_list[i + 1] for i in range(len(my_list) - 1)):
    for j in range(len(my_list)-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            break
# Display the Results
print(my_list)
        
