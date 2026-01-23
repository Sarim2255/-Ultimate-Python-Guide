# Write code below 💖
Gryffinder=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0

q1 = int(input("Do you like Dawn or Dusk\n 1) Dawn\n 2) Dusk \n"))
if q1==1:
  Gryffinder+=1
  Ravenclaw+=1
elif q1==2:
  Hufflepuff+=1
  Slytherin+=1
else:
  print("Wrong Input.")

q2 = int(input("When I’m dead, I want people to remember me as:\n 1) The Good\n 2) The Great\n 3)The Wise\n 4)The Bold\n"))
if q2==1:
  Hufflepuff+=2
elif q2==2:
  Slytherin+=2
elif q2==3:
  Ravenclaw+=2
elif q2==4:
  Gryffinder+=2
else:
  print("Wrong Input.")

q3 = int(input("Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumpet\n 3)The piano\n 4)The drum\n"))
if q3==1:
  Slytherin+=4
elif q3==2:
  Hufflepuff+=4
elif q3==4:
  Ravenclaw+=4
elif q3==4:
  Gryffinder+=4
else:
  print("Wrong Input.")

print("Total scores of the houses.")
print("Hufflepuff: ",Hufflepuff)
print("Slytherin: ",Slytherin)
print("Ravenclaw: ",Ravenclaw)
print("Gryffindor: ",Gryffinder )