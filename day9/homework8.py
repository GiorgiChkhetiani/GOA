# nino solomonia შექმენით მეოთხე ჯგუფის წევრების სია .დაწერეთ კოდი ისე,რომ გაიგოთ ყველა სახელსა და გვარში ერთად რამდენი  ,,ი" და ,,ა"   იქნება.


group = [ "gabrieli" , "gurami" , "salome"  , "tekla" , "nino" , "giorgi"]
x_counter  = 0

for element  in group : 
    for char in element : 
      if (char== "a" or char == "i") : 
        x_counter += 1
print(x_counter)

