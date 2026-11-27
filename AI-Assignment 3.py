customers = [
    "Ahmed", "Sara", "Omar", "Mona",
    "Ali", "Nour", "Youssef", "Hana",
    "Khaled", "Mariam", "Hassan", "Laila"
]

scores = [91, 45, 78, 66, 88, 30, 72, 95, 51, 60, 84, 39]

risk_levels = []

for score in scores:
    if score >= 85:
        risk_levels.append("High")
    elif score >= 60:
        risk_levels.append("Medium")
    else:
        risk_levels.append("Low")

high_count = 0
medium_count = 0
low_count = 0
total = 0

for score, risk in zip(scores, risk_levels):
    total += score

    if risk == "High":
        high_count += 1
    elif risk == "Medium":
        medium_count += 1
    else:
        low_count += 1

average = total / len(scores) if scores else 0

if scores:
    lowest_score_index = scores.index(min(scores))
    highest_score_index = scores.index(max(scores))

    lowest_score_name = customers[lowest_score_index]
    lowest_score = scores[lowest_score_index]

    highest_score_name = customers[highest_score_index]
    highest_score = scores[highest_score_index]

while True:
    print("\n========== MENU ==========")
    print("1. Show All Customers")
    print("2. Search for a Customer")
    print("0. Exit")
    print("==========================")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        print("\n========== CUSTOMER RISK REPORT ==========\n")
        print(f"{'Name':<11}{'Score':<9}Risk")
        print("-" * 30)

        for name, score, risk in zip(customers, scores, risk_levels):
            print(f"{name:<11}{score:<9}{risk}")

        print("\n=============== SUMMARY ================\n")
        print(f"High Risk:   {high_count}")
        print(f"Medium Risk: {medium_count}")
        print(f"Low Risk:    {low_count}")
        print(f"Average Score: {average:.2f}")

        if scores:
            print(f"\nLowest Score:  {lowest_score_name} ({lowest_score})")
            print(f"Highest Score: {highest_score_name} ({highest_score})")
        else:
            print("\nNo customer data available.")

    elif choice == "2":
        search = input("Enter customer name: ").strip().lower()

        for name, score, risk in zip(customers, scores, risk_levels):
            if name.lower() == search:
                print(f"Name: {name}")
                print(f"Score: {score}")
                print(f"Risk: {risk}")
                break
        else:
            print("Customer not found!")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")