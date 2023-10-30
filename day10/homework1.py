# # შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი, 
# 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#, 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347

# import random

# numbers = " 123456789" 
# a = "ajdsfuhwieufb"
# symbol = "@#$%^&*"
 
# password = (str(random.choice(numbers)) + random.choice(a) + random.choice(symbol) + str(random.choice(numbers)) + random.choice(a) + random.choice(symbol) + str(random.choice(numbers)) + str(random.choice(numbers)))


# print(password)

import random # gamovidzxe random funqcia
list = [ "12345678" , "cashfbjknf" , "!@#$%^&" ] # shevqmeni list romlis elementebsac mivaniche mnishvnelobad  ricxvi aso da simbolo
password = " "  # cariei cvladi string mnishvnelobit passwordistvis
for i in range(4):  # for cikli davatriale imdenjer ramdeni cipric mchirdeba passwordshi
    number = random.choice(list[0]) #shevqmeni cvladi romelshic sheva random funqciit gamotanili ciprebi list[0]  dan
    password += str(number) # passwords davamate ciprebi 

for i in range(2) : #cikli davatriale imdenjer ramdeni symbolo da asobgerac mchirdeba 
    a = random.choice(list[1]) #shevqmeni cvladi romelshic sheva random funqciit gamotanili asobgerebi  list[1] dan 
    symbol = random.choice(list[2]) #shevqmeni cvladi romelshic rendom funqciit gamotanili simboloebi list[2] dan
    password += a + symbol #passwords davamate asobgerebi da simboloebi 

print(password) #davprinte password

 
 