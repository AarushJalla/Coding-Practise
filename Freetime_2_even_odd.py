print("Even Or Odd")
print("")

a=int(input("Enter A Number:"))

if a < 0:
    print("Your Number Needs To be Positive To Be Classified As Even Or Odd.")
elif a % 2 == 0:
    print("Your Number Is Classified As Even.")
else:
    print("Your Number Is Classified As Odd.")