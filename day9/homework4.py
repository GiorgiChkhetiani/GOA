# 4.Guri Jishkariani 
# შევქმნათ ორი List-ი. ერთში გოგონების სახელები ჩავწეროთ მეორეში ბიჭების. დავპრინტოთ დაწყვილებულად   😄 აი დააკომენტარეთ და დაგაწყვილებთო რო იცოდნენ ფბზე ეგრე დაახლოებით  


girls_names = [ " salome - " , " mariami - " , " tekla - ",  " nino - "]
boys_names = [ " nika" , " gabrieli " , " giorgi " , " saba " ] 

lenboys_names = len(boys_names)

paired = [ ]

for i  in  range  (  lenboys_names  ) :  
    paired =  girls_names [i] +  boys_names[i]
    #paired.append(girls_names [ i] + boys_names [ i ])
    print(paired)

         