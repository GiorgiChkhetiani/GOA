# შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი, 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#, 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347

import random

numbers = " 123456789" 
a = "ajdsfuhwieufb"
symbol = "@#$%^&*"
 
password = str(random.choice(numbers)) + random.choice(a) + random.choice(symbol) +str(random.choice(numbers)) + random.choice(a) + random.choice(symbol) + str(random.choice(numbers)) + str(random.choice(numbers))


print(password)