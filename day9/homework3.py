
# 3.Luka Kechexmadze
# ნივთმა დაიკლო ფასში 10% ით,საიდანაც გამყიდველმა აიღო 8% მოგება, რამდენ % იან მოგებას აიღებდა ის ფასის დაკლებამდე?ჩაწერეთ ეს ყველა მონაცემი პითონში და დაათვლევინეთ მას. 


price = int(input("enter  the price of the item : "))
discount = price/100 * 10  
profit = (price - discount )/ 100 * 8 


print(str( price) + " " + "lari aris tavdapirveli girebuleba ")
print (str(discount) + " " +  "lari daaklda nivts ")
print ( str(profit) + " " +  "lari mougo nivst gamyidvelma")

print (  " gamyidveli fasdaklebamde aigebda "  +  "  " +  "discount + profit"  + "  " + " mogebas "  )