marks = [88, 45, 92, 67,30 , 75]
passed = 0
for mark in marks:
    if mark >= 50:
        passed += 1
average = sum(marks)/len(marks)
highest = max(marks)
lowest = min(marks)
print("passed:", passed)
print(f"average:{average:.1f}")
print("Highest:",highest, "Lowest",lowest )
