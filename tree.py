height = int(raw_input("Please give the height of the Tree: "))

Th = int(raw_input("Please give the height of the trunk: "))

Tw = int(raw_input("Please give the width of the trunk: "))

i=0

while i < height:

 print((' '*(height-i))+('*'*(i*2+1))+(' '*(height-i)))

 i=i+1

 if(i == height):

  j = 0 

  while j < Th:

   print((' ' *height) + ('*'*Tw))

   j=j+1 