# 14.Merab Tsitskhvaia  
# User-ს შემოატანინეთ თავისი სიმაღლე. მიეცით საშუალება მომხმარებელს აირჩიოს ის, თუ რომელ სიდიდეში სურს გაიგოს თავისი სიმაღლე, სანტიმეტრებში თუ ფუნტებში...(თუ შემოიტანს 180-ს და აირჩევს ფუტებში გადაყვანას თავისი წონის, დაუპრინტეთ რამდენი ფუტია ის


user = int(input("enter your height in cm  : "))


ft =  user  * 0.032808
print("this is your height in ft " + str(ft ))

user1 = float(input("enter your height in ft : "))
cm = user1 / 0.032808
print("this is your height in cm " + str(cm ))