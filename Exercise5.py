#defining a dic as key and values key is the number of the month and the values are the days
month_days = {
    "1": "31",
    "2": "28", 
    "3": "31",
    "4": "30",
    "5": "31",
    "6": "30",
    "7": "31",
    "8": "31",
    "9": "30",
    "10": "31",
    "11": "30",
    "12": "31",
}
#initializing a var which asks for user input 
search = input("Enter the number of the month: ").strip() #.strip is used to remove spacexs before or after user input 

#checkes if input is a valid values existing in the dic
if search in month_days:
    print(f"Month {search} has {month_days[search]} days") 
else:
    print("Invalid number. Please use a number between 1 to 12") #feedback message