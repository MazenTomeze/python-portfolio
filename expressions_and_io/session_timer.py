#session_timer.py
total_seconds = int(input("5Session Length in Seconds :"))

minutes_time = total_seconds // 60
remaining_seconds = total_seconds % 60
print (f"Session length : {minutes_time} minutes and {remaining_seconds} seconds")

# 905 : ==> 
#Session length in seconds:905
#Session length : 15 minutes  and 5 seconds

# 60  : ==>
#Session length in seconds:60
#Session length : 1 minutes and 0 seconds

# 59  : ==>
#Session length in seconds:59
#Session length : 0 minutes and 59 seconds