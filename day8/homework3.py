# GOA ში ყოველ შემოყვანილ ადამიანზე გეძლევა 100ლ.
# მომხმარებელს შემოატანინეთ თუ რამდენი ადამიანი შემოიყვანა ხოლო თითო შემოყვანილ ადამიანზე დაერიცხოს 100ლ

# 1) რამდენი დაგერიცხება თუ შემოიყვან 10 ბავშვს?  15 ბავშცს?

# 2) რამდენი დაგერიცხება თუ შემოიყვან 100 ბავშვს გამოკლებული 37 დამატებული 13 გაყოფილი 10 და გამრავებული 264 ზე


quantity = int(input("How many people did you bring to Goa? : "))
Gift_per_person = 100

print ( " You will be charged  " +   str ( quantity * Gift_per_person) + " " + " gel")

print("You will be charged  " + str(quantity - 37 + 13 / 10  * 264 * Gift_per_person ) + " " + "gel" )
