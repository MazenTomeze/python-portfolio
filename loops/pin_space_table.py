# pin_space_table.py 
GUESSES_PER_SECOND = 10

for i in range(4, 9):
    combinations = 10 ** i
    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = minutes // 1440
    print(f"{i} digits: {combinations} PINs, {minutes} minutes, {days} days")