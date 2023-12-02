import re

#------Day 2 Part 1------

red = 12;
blue = 14;
green = 13;

f = open('day2.txt', 'r')
file = f.readlines()

gameidtotal = 0

for line in file:
  
  w=list() 
  x=list()
  y=list()
  z=list()

  gametrue = 0
  redtrue = 0
  bluetrue = 0
  greentrue = 0

  gameline = re.findall(r"Game (\d+)", line)
  redline = re.findall(r"(\d+) red", line)
  blueline = re.findall(r"(\d+) blue", line)
  greenline = re.findall(r"(\d+) green", line)

  w=w+gameline
  sumgame=0
  for i in w:
      sumgame=sumgame + int(i)
  # print("game:",sumgame)

  x=x+redline
  sumred=0
  for i in x:
     sumred=sumred + int(i)
     varX=int(i)
     if varX > red:
      redtrue = redtrue + 1
      gametrue = redtrue + gametrue
      #print("red not possible")
  #print("red:",sumred)

  y=y+blueline
  sumblue=0
  for i in y:
      sumblue=sumblue + int(i)
      #print("blue:",sumblue)
      varY=int(i)
      if varY > blue:
        bluetrue = bluetrue + 1
        gametrue = bluetrue + gametrue
        #print("blue not possible")

  z=z+greenline
  sumgreen=0
  for i in z:
      sumgreen=sumgreen + int(i)
      #print("green:",sumgreen)
      varZ=int(i)
      if varZ > green:
        greentrue = greentrue + 1
        gametrue = gametrue + greentrue
        #print("green not possible")

  if gametrue == 0:
    gameidtotal = gameidtotal + sumgame
  
print("Day 2 Part 1: ",gameidtotal)


#------Day 2 Part 2------

red = 12;
blue = 14;
green = 13;

f = open('day2.txt', 'r')
file = f.readlines()

gameidtotal = 0

for line in file:
  
  w=list() 
  x=list()
  y=list()
  z=list()

  gametrue = 0
  redtrue = 0
  bluetrue = 0
  greentrue = 0

  redlargest=0
  bluelargest=0
  greenlargest=0

  gameline = re.findall(r"Game (\d+)", line)
  redline = re.findall(r"(\d+) red", line)
  blueline = re.findall(r"(\d+) blue", line)
  greenline = re.findall(r"(\d+) green", line)

  w=w+gameline
  sumgame=0
  for i in w:
      sumgame=sumgame + int(i)
  # print("game:",sumgame)

  x=x+redline
  sumred=0
  for i in x:
     sumred=sumred + int(i)
     varX=int(i)
     if varX > redlargest:
      redlargest = varX

  y=y+blueline
  sumblue=0
  for i in y:
      sumblue=sumblue + int(i)
      varY=int(i)
      if varY > bluelargest:
        bluelargest = varY

  z=z+greenline
  sumgreen=0
  for i in z:
      sumgreen=sumgreen + int(i)
      #print("green:",sumgreen)
      varZ=int(i)
      if varZ > greenlargest:
        greenlargest = varZ
  gameidtotal = gameidtotal + (redlargest * bluelargest * greenlargest)
print("Day 2 Part 2: ",gameidtotal)