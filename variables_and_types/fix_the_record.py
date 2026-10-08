 # fix_the_record.py
 # This program prints a short record about a network device.
  
device_name = "edge-router"
# syntax error
second_ip = "192.0.2.1"
# syntax error
class_name = "router"
# runtime error
port = int("22") 
# runtime error
print("Device:", device_name)

print("Backup IP:", second_ip)

print("Type:", class_name)

print("Port:", port)



# Erorr 1
#File "c:\Users\mrmaz\Desktop\test.py", line 5
  #  2nd_ip = "192.0.2.1"
 #   ^
#SyntaxError: invalid decimal literal

#fix: variable names cannot start with a number. Change `2nd_ip` to `second_ip`.

#---------------------------------------------------------------------------------------------------------------------

#Error 2
#File "c:\Users\mrmaz\Desktop\test.py", line 6
#    class = "router"
#          ^
#SyntaxError: invalid syntax

#fix : The variable `class` is reserved in Python.

#---------------------------------------------------------------------------------------------------------------------

#Error 3
#File "c:\Users\mrmaz\Desktop\test.py", line 7, in <module>
#    port = int("twenty-two")
#ValueError: invalid literal for int() with base 10: 'twenty-two'

#fix: The string "twenty-two" cannot be converted to an integer. Use a numeric string like "22" instead.

#---------------------------------------------------------------------------------------------------------------------

#Error 4
#File "c:\Users\mrmaz\Desktop\test.py", line 8, in <module>
#    print("Device:", device_nam)
#                     ^^^^^^^^^^
#NameError: name 'device_nam' is not defined. Did you mean: 'device_name'?

#fix: The variable name `device_nam` is a typo. It should be `device_name`.



# ---------------------------------------------------------------------------------------------------------------------
#
# أي الأخطاء تظهرها بايثون أولاً، ولماذا؟
# الجواب:
#(Syntax Errors) تظهر أولاً.
#  السبب:
# لغة بايثون تفحص القواعد النحوية وتنسيق الكود كاملاً قبل البدء في تشغيله،
# فإذا وجدت أي خطأ قواعدي تتوقف فوراً ولا تنفذ البرنامج.
# أما أخطاء وقت التشغيل
#(Runtime Errors مثل كتابة أسماء خاطئة أو دوال غير معروفة)،
# فلا تكتشفها بايثون إلا عند الوصول إلى ذلك السطر وتشغيله فعلياً.
#
# ----------------------------------------------------------------------------------------------------------------------