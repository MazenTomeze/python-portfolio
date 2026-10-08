# type_check.py
# Output: <class 'int'> (عدد صحيح)
print(type(8080)) 
# Output: <class 'str'> (بسبب وجود الرقم بين علامات التنصيص "")
print(type("8080"))
# Output: <class 'float'> (بسبب وجود الفاصلة العشرية)
print(type(99.5))
# Output: <class 'str'>  (بسبب وجود الرقم بين علامات التنصيص "")
print(type("198.51.100.7"))
# Output: <class 'int'> (الرقم اذا فصله_ لا يوثر على نوعه فقط لتسهيل قرائة الرقم)
print(type(1_000))

# -----------------------------------------------------------------------------

val_int = int("443" ) 

val_str = str(8080)

val_float = float("2.5" )


print (
val_int , type(val_int) ,
val_str , type(val_str) ,
val_float , type(val_float)
)