# მომხმარებელს კითხეთ თავისი და მამამისის ასაკი, 
# დაუპრინტეთ ყოველ წელს რამდენჯერ უფროსი იქნება მამამისი მასზე.


age = int(input("how old ar you : "))
age1 = int(input("how old is your father : "))
year = int(input("enter year : "))


for i in range(50) : 
    print("amdenjer uprosi qineba mamasheni  "  + str((age1 + 1 ) / (age + 1)) + str(year + 1) + "am wels "  )