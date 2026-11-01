# fix_the_stats.py
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]
#Defining a variable inside a loop
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
#Print outside the loop so it only prints the final total once
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1
#Print outside the loop, and use '/' instead of '//' to output 30.0
print(f"Average session: {total / count} minutes")
# range(1, 4) is changed to range(1, 5) to not avoid printing level 4
for level in range(1, 5):
    print(f"Level {level}")