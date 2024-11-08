# 1. Program to Create a List of Integers and Compute Their Sum
#Accepting user input to create a list of integers
# numbers = input("Enter integers separated by spaces: ")
# int_list = list(map(int, numbers.split()))

# #Calculating the sum of the integers
# total_sum = sum(int_list)
# print("The sum of all integers is:", total_sum)



# 2.  Program to Create a Tuple of Favorite Books and Print Each Book Name
#Creating a tuple containing favourite book names
# favourite_books = ("1994", "To Kill a Mockngbird", "Pride and Prejudice", "The Great Gatsby", "Moby-Dick")

# #Printing each book name on a separate line
# for book in favourite_books:
#     print(book)



# 3. Program to Store Information About a Person in a Dictionary
#Creating a dictionary to store personal information
# person_info = {}

# #Asking the user for input
# person_info['name'] = input("Enter your name: ")
# person_info['age'] = int(input("Enter your age: "))
# person_info['favourite_color'] = input("Enter your favourite color: ")

# #Printing the dictionary
# print("Person Information: ", person_info)



# 4. Program to Create Two Sets and Find Common Elements
#Accepting user input to create two sets of integers
set1 = set(map(int, input("Enter integers for the first set, separated by spaces: ").split()))
set2 = set(map(int, input("Enter integers for the second set, separated by spaces: ").split()))

#Creating a new set containing elements to both sets
common_elements = set1.intersection(set2)

print("Common elements in both sets:", common_elements)



# Program to Filter Words with Odd Number of Characters Using List Comprehension
