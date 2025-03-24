# list of names to search within
name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# prompt user to enter a name
search_name = str(input("Enter the name: "))

# checks if the entered name (capitalized) is in the list
if search_name.capitalize() in name:
    print(f"{search_name} IS in the list")  # prints message if name is found
else:
    print(f"{search_name} is NOT in the list")  # prints message if name is not found