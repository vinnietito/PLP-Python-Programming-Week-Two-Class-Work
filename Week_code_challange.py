#Accepting user input to create a list of integers
numbers = input("Enter integers separated by spaces: ")
int_list = list(map(int, numbers.split()))

#Calculating the sum of the integers
total_sum = sum(int_list)
print("The sum of all integers is:", total_sum)