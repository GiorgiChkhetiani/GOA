# list =  [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
# იპოვეთ ყველაზე პატარა რიცხვი აქ
# min() ფუნქციის გამოყენების გარეშე


list =  [ 7, 5, 2, 7, 20, 652 ,6 , 3, 62, 9 ]
smallest  = list[0]

for num in list : 
   if num < smallest :
      smallest = num 
print (smallest)