#conditional_tests.py
user = "analyst"
role = "viewer"
failed = 3
port = 22
print ("Is port == 22 ? I predict True.")
print (port == 22 )  #--> true
print ("\nIs port > failed ? I predict True.")
print (port > failed)#--> true
print ("\nIs failed <= 3 ? I predict True.")
print (failed <= 3)# --> true
print ("\nIs failed >= 3 ? I predict True.")
print (failed >= 3)# --> true
print ("\nIs failed < port ? I predict True.")
print (failed < port) # --> true
print ("\nIs failed > 3 and port == 22 ? I predict False.")
print (failed > 3 and port == 22) # --> false
print ("\nIs failed == port or failed == 2 ? I predict False.")
print (failed == port or failed == 2) # --> false
print ("\nIs failed != 3 ? I predict False.")
print (failed != 3) #--> false
print ("\nIs port == 3 and failed != 22 ? I predict False.")
print (port == 3 and failed != 22) # --> false
print ("\nIs not failed == 3 ? I predict False.")
print (not failed == 3) # --> false