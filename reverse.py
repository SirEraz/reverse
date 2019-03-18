import math 

print("Welcome to the Reverse-a-tron.")
print("\n")

charList = []

while True:
   string = str(input("Enter a word: "))
   print("Your word is {}.".format(string))
   slength = len(string)
   print("It is {} letters long.".format(slength))
   print("...")
   
   for elem in reversed(string):
      charList.append(elem)
   
   rstring = str(''.join(string))
   print("Backwards, it is {}.".format(rstring))
   
   if string == rstring:
      print("It is a palindrome.")
   else:
      print("It is not a palindrome.")
   print("...")
   print("Would you like to try again? (Y/N)")
   
   menu = str(input("Enter Y/N: "))
   
   if menu == "Y":
      print("Ok, returning to start...")
      print("\n\n\n")
   elif menu == "y":
      print("Ok, returning to start...")
      print("\n\n\n")
   elif menu == "N":
      break
   elif menu == "n":
      break
   else:
      print("Unknown input. Returning to start...")
      print("\n\n\n")
