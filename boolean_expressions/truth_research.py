#truth_research.py
#False -->  In Python, empty text is considered False
print (bool(""))
#True --> Any not empty text in Python is considered True
print (bool("0"))
#False --> The number 0 is considered False
print (bool(0))
#False --> The decimal number 0.0 is considered False
print (bool(0.0))
#True --> Any text that is not empty in Python is considered True
print (bool("False"))


#Source : https://docs.python.org/3/builtins/stdtypes.html#truth-value-testing