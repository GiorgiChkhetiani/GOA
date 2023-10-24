# luka siradze input ფუნქციით შემოატანინეთ წინადადება და შმოტანილ წინადედებაში პროგრამას დაათვლევინეთ თანხმოვნები


text = input("any text : ")
vowels = 0
cons= 0 

for i in text : 
   if (i == "a" or i=="e" or i=="i" or i=="o" or i=="u")   : 
     vowels += 1
   else : 
     cons += 1
print(cons)
