#truth_research.py
#False -->  في بايثون النصوص الفارغة تعتبر False
print (bool(""))
#True --> أي نص غير فارغ في بايثون تعتبرTrue
print (bool("0"))
#False --> الرقم الصحيح 0 يعتبر False
print (bool(0))
#False --> الرقم العشري 0.0 يعتبر False
print (bool(0.0))
#True --> نص غير فارغ يحتوي على أحرف يعتبر True
print (bool("False"))


#Source : https://docs.python.org/3/builtins/stdtypes.html#truth-value-testing