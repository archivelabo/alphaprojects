class Mules:

  def __init__(self, n):
    self.scores = [0] * (n + 1)

  def A(self, n, x):
    if self.scores[x]!= None:
      self.scores[x] += n

  def Covfefe(self, x):
    self.scores[x] = None # Set to none to avoid covfefed mules from getting jelly beans

  def Q(self, x):
    if self.scores[x] == None:
      print(0)
    else:
      print(self.scores[x])

  def G(self, x):
    jellyBeans = 0
    for k in range(x + 1):
      if self.scores[k] != None:
        jellyBeans += self.scores[k]
    print(jellyBeans)

  def L(self, x):
    jellyBeans = 0
    for k in range(0, x + 1):
      if self.scores[-k] != None:
        jellyBeans += self.scores[-k]
    print(jellyBeans)

t = int(input()) # T is the number of weeks
for i in range(t):
  numberOfMules, commands = map(int, input().split())
  MulePopulation = Mules(numberOfMules)
  for j in range(commands):
    command = input().split() # Index 0 will be command type
    if command[0] == "A":
      MulePopulation.A(int(command[1]), int(command[2]))
    elif command[0] == "Covfefe":
      MulePopulation.Covfefe(int(command[1]))
    elif command[0] == "Q":
      MulePopulation.Q(int(command[1]))
    elif command[0] == "G":
      MulePopulation.G(int(command[1]))
    else:  # command is "L"
      MulePopulation.L(int(command[1]))