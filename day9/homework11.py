# 11.beqa giorgobiani
# გვაქვს სია list=[21,-3,11,-31,7,-34]
# ამ სიაში დაამატეთ მეხუთე ინდექსად ინფუთით რიცხვი და დაპრინტეთ მხოლოდ დადებითი რიცხვების ჯამი


list = [ 21 , -3 , 11 , -31 , 7 , -34 ]
num = 22
list.insert(5,num)

print(list)

numbers = 0

for element in list  : 
    if element >= 0 :
        numbers += element 
print(numbers)
      