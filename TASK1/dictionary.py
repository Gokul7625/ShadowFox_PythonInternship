#TASK1_dictionary_FRIENDS
# friends = ["GOKUL", "MARAN", "KATHIR", "KARTHI", "VISHAL"]
# friends_with_length = [(name, len(name)) for name in friends]
# print(friends_with_length)

#TASK1_TRACKING EXPENSES

#Mine_expenses
Mine = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

# Partner's_expenses
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(Mine.values())
partner_total = sum(partner_expenses.values())

print(f"Mine_total: {your_total}")
print(f"Partner's_total : {partner_total}")


if your_total > partner_total:
    print("You spent more money overall.")
elif your_total < partner_total:
    print("Your partner spent more money overall.")
else:
    print("You both spent the same amount.")


significant_difference = {}
for category in Mine:
    difference = abs(Mine[category] - partner_expenses[category])
    if difference > 0:
        significant_difference[category] = difference

# Difference
if significant_difference:
    largest_category = max(significant_difference, key=significant_difference.get)
    print(f"The category with the most significant difference is '{largest_category}' with a difference of {significant_difference[largest_category]}.")

