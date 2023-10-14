#მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you 

score = int(input("enter score : "))
score1 = int(input("enter score : "))
score2 = int (input("enter score : "))
score3 = int(input ( "enter score : "))
score4 = int(input ( "enter score : "))


arithmetic_average = (score + score1 + score2 + score3 + score4) / 4 

if arithmetic_average < 9 :
    print(" გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")

elif arithmetic_average  < 5 :
    print("გილოცავ გაექეცი მატრიცას")

if arithmetic_average > 5 : 
      
      if arithmetic_average < 9 :
       print("YOU ARE MID")
 

if  arithmetic_average > 10 :
    if arithmetic_average < 0 :
        print("there is something wrong with you ")
