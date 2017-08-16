s, k, i = map(int, input().split())
class Line:
  def __init__(self): # Get input of the line to initialize
    self.people = list(map(int, input().split()))

  def length(self): # get length of the line line = Line()
    return len(self.people)

  def obtainRental(self): # Person in line has gotten rental
    self.people.pop(0)

  def tick(self):# Tick causes one second to pass
    # They should just use an if statement to check the length
    try:
      self.people[0] -= 1
    except:
      pass

  def moveSkier(self, shortest): # Get input of the line to initialize
    if shortest == 1:
      one.people.append(self.people.pop())
    elif shortest == 2:
      two.people.append(self.people.pop())
    else:
      three.people.append(self.people.pop())

# Create lines
one = Line()
two = Line()
three = Line()

# Start timer
timer = 0

if one.people[0] == 0:
  one.obtainRental()
if two.people[0] == 0:
  two.obtainRental()
if three.people[0] == 0:
  three.obtainRental()

while True:
  one.tick()
  two.tick()
  three.tick()
  if one.people and one.people[0] < 1:
    print(one.people)
    one.obtainRental()
  if two.people and two.people[0] < 1:
    two.obtainRental()
  if three.people and three.people[0] < 1:
    three.obtainRental()
  timer += 1
  if not one.people and not two.people and not three.people:
    break
  if timer != 0 and timer % 30  == 0: #If people should be looking for a new line
    if one.length() > two.length() and one.length() > three.length():
      if two.length() > three.length():
        one.moveSkier(3)
      elif three.length() > two.length():
        one.moveSkier(2)
    elif two.length() > one.length() and two.length() > three.length():
      if one.length() > three.length():
        two.moveSkier(3)
      elif three.length() > one.length():
        two.moveSkier(1)
    elif three.length() > two.length() and three.length() > one.length():
      if one.length() > two.length():
        three.moveSkier(2)
      elif two.length() > one.length():
        three.moveSkier(1)

print(timer)
