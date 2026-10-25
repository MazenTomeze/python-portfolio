#risk_score.py
score = 0
failed_attempts = int(input("Failed attempts in the last hour: "))
login_hours = int(input("Login hour (0-23): "))
new_device = input("New device (yes/no): ")

if failed_attempts >= 3:
    score += 40
if login_hours < 6:
   score += 30
if new_device == "yes":
    score += 30

if score >= 70:
    print(f"Risk score: {score} (HIGH)")
elif score >= 30:
    print(f"Risk score: {score} (MEDIUM)")
else:
    print(f"Risk score: {score} (LOW)")

# or I can determine the levels using conditional statements, and then print the level and the points on the final line.