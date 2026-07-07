# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#1. Use the "for" loop with the range function to iterate through the list. 
for day in range(len(weekdays)):
    weekday = weekdays [day]
    promotion = daily_promotions[day]
    print(f"{weekday.upper()}: Promotion on {promotion}")
 