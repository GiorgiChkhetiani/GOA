
# rati murghulia მომხმარებელს შემოატანინეთ ორი სახელი და გვარი,და შეადარეთ ერთი მეორეს,დაითვალეთ a-ს რაოდენობა რომელ სახელში არის მეტი,და დაპრინტეთ მიღებული შედეგი/


full_name = input("enter your full name : ")# niki lauda 
full_name1 = input("enter your full name : ")# james hunt 

x_counter = 0
 
for char in full_name : 
        if char == "a" : 
            x_counter += 1
            
             
x_counter1 = 0
               
for char in full_name1 : 
        if char == "a"  : 
            x_counter1 += 1
            

if x_counter > x_counter1 : 
    print (full_name + " radgan masshi  a- s raodenoba aris " + str(x_counter) )  
elif full_name < full_name1 : 
    print(full_name1 +  " radgan masshi a - s raodenoba aris " +  str(x_counter1))              