# Incomplete

import turtle
tina = turtle.Turtle()
def drawGrid(size, strokeWidth):
  offset = 220
  tina.hideturtle()
  tina.tracer(0, 0)
  tina.speed(10)
  tina.penup()
  for i in range(0, size + 1):
      tina.setpos(0 - offset, i * 50 - offset)
      tina.pensize(1)
      if i % 3 == 0:
        tina.pensize(strokeWidth)
      tina.pendown()
      tina.forward(size * 50)
      tina.penup()
  tina.left(90)
  for i in range(0, size + 1):
      tina.setpos(i * 50 - offset, 0 - offset)
      tina.pensize(1)
      if i % 3 == 0:
        tina.pensize(5)
      tina.pendown()
      tina.forward(size * 50)
      tina.penup()
  tina.update()

class Box:

    def __init__(self):
        # Create turtle
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(10)
        self.value = 0 # To store numbers
        self.highlighted = False
    # def draw(self, pencolor, )
    def draw(self, x, y, fillColor, penColor):
        screen.onclick(None)
        if fillColor:
            self.turtle.begin_fill() # Begin the fill process.
            self.turtle.fillcolor(fillColor)
        self.turtle.penup()
        self.turtle.setpos(x * 50 - 219, y * 50 - 219)
        self.turtle.pencolor(penColor)
        self.turtle.forward(48)
        self.turtle.left(90)
        self.turtle.forward(48)
        self.turtle.left(90)
        self.turtle.forward(48)
        self.turtle.left(90)
        self.turtle.forward(48)
        self.turtle.left(90)
        if fillColor:
          self.turtle.end_fill()
        self.turtle.update()
        screen.onclick(click)
        return True

    def write(self, x, y, num):
        self.turtle.color("black")
        self.turtle.setpos(y * 50 + 15 - 220, (x * 50) + 15 - 220)
        self.turtle.write(str(num), font=("Arial", 20, "normal"))
        game.grid[x][y].value = num
        self.turtle.update()

    def highlight(self, x, y):
        if self.highlighted:
            self.draw(x, y, "lightblue", "black")
            self.highlighted = False
            if not game.grid[y][x].value == 0:
              self.write(y, x, game.grid[y][x].value)
        elif game.highlighted == False:
            self.draw(x, y, "pink", "black")
            self.highlighted = True
            if not game.grid[y][x].value == 0:
                self.write(y, x, game.grid[y][x].value)
            return True

class Game:
    def __init__(self):
        # Create turtle
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(10)
        self.grid = [[0] * 9 for _ in range(9)]
        for i in range(9):
          for j in range(9):
            self.grid[i][j] = Box()
        drawGrid(9, 5)
        self.highlighted = False


def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i/3), 3 *(j/3)
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

def space():
    solve_grid = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
      for j in range(9):
          solve_grid[i][j] = game.grid[i][j].value
    if solveSudoku(solve_grid):
        for i in range(9):
            for j in range(9):
                game.grid[i][j].turtle.penup()
                game.highlighted = [i, j]
                keypress(solve_grid[i][j])

    else:
        print("Can't solve :()")

def click(x, y):
  if x > -220 and y > -220: # If on sudoku
    i = int((y + 220) // 50)
    j = int((x + 220) // 50)
    if game.grid[i][j].highlight(j, i):
        game.highlighted = [i, j]
    else:
        game.highlighted = False


def keypress(num):

  if game.highlighted:
    if num == 0:
      game.grid[game.highlighted[0]][game.highlighted[1]].value = 0
      game.grid[game.highlighted[0]][game.highlighted[1]].draw(x, y, "lightblue", "black")
      game.grid[game.highlighted[0]][game.highlighted[1]].highlight(game.highlighted[1], game.highlighted[0])
    else:
      game.grid[game.highlighted[0]][game.highlighted[1]].write(game.highlighted[0], game.highlighted[1], num)
      game.grid[game.highlighted[0]][game.highlighted[1]].highlight(game.highlighted[1], game.highlighted[0])
# Start game
screen = turtle.Screen()
screen.bgcolor("lightblue")

game = Game()
# Write text

screen.onkey(space, "space")
screen.onkey(lambda: keypress(1), "1")
screen.onkey(lambda: keypress(2), "2")
screen.onkey(lambda: keypress(3), "3")
screen.onkey(lambda: keypress(4), "4")
screen.onkey(lambda: keypress(5), "5")
screen.onkey(lambda: keypress(6), "6")
screen.onkey(lambda: keypress(7), "7")
screen.onkey(lambda: keypress(8), "8")
screen.onkey(lambda: keypress(9), "9")
screen.onclick(click)
screen.listen()


screen.mainloop()
