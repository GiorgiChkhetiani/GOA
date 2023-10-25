# დაწერეთ პროგრამა, რომელშიც შექმნით ჩვენი ჯგუფელებისგან სიას.

# რენდომად გამოიძახებთ ერთ ჯგუფელს, თუ კითხვაზე უპასუხებს მოემატება 1 ქულა და გადავალთ შემდეგზე(ოღონდ ეს ვეღარ უპასუხებს იმ დღეს)( ანუ remove დაგჭირდებათ),
# answer = input("did the student answer correctly: ")
#     if answer == "yes":
#         ............ moematos 10 qula 
#         if answer == "no"
#                     daakldes 5 qula

import random 

group_members = [ "giorgi" , "nino" , "nini" , "luka" , "tekla" ] # შევქმენი სია და ელემენტებად დავამატე ჩემი ჯგუფის წევრების სახელები 
question = " ხაარ მზად დათმო შენი სურვილები , იმისთვის  რომ შექმნა შენი მომავალი ? " # კითხვა შემდეგში გამოძახებული სტუდენტისთვის 

for i in range(len(group_members)) : 
      summoned = random.choice(group_members)  

 # დავატრიალე ფორ ციკლი იმდენჯერ რამდენი ელემენტიც მაქვს სიაში და random ფუნქციით გამოვიძახე  ჩემი სიიდან სტუდენტი რენდომად 

print(summoned  , question ) # დავპრინტე სიიდან გამოძახებული ელემენტი და შეკითხვა 
group_members.remove(summoned) # remove  ფუნქციით სიიდან ამოვშალე გამოძახებული ელემენტი რათა შემდგომში აღარ იქნას გამოძახებული

answer = input( "did the student answer correctly : ") #input  ფუნქციით გამოძახებულ სტუდენტს შემოვატანიე პასუხი 

score = 0  # შევქმენი საიტერაციო ცვლადი 

if answer == "yes" :            # if - ით პროგრამას მივეცი direction  სწორი და არასწორი პასუხისთვის
        score += 10 
        if answer == "no" : 
               score -= 5 

print( summoned  ,  " you have " ,  score  , "point" )  # დავპრინტე გამოძახებული ელემენტი და მისი მოპოვებული ქულა 

            
               






