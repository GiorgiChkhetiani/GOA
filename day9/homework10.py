#nino goglichadze შემოიტანეთ სამი რიცხვი და დაპრინტეთ გამოვა თუ არა ამ რიცხვების საშუალებით სამკუთხედი, თუ გამოვა გამოთვალეთ პერიმეტრი და დაპრინტეთ "ამ სამკუტხედის პერიმეტრია: XX" თუ არ გამოდის მაშინ დაპრინტეთ „მსგავსი სამკუთხედი არ არსებობს“

num = int(input("enter number : "))
num1 = int(input("enter number : "))
num2 = int(input("enter number : "))


if num == num1 or num == num2 or num1 == num2  :
     print("samkutxedis perimetria "  +  str(num + num1 + num2 ))
else : 
     print("msgavsi samkutxedi ar arsebobs")