import turtle

diskNumber = int(input("How many disks would you like?")) # Set number of disks

class Game:
    def __init__(self):
        disks = [Disk(i, 0, diskNumber - 1 - i) for i in range(diskNumber - 1, -1, -1)] # Create the initial list of disks
        self.startCol = Column(0, disks) # Create a column, put initial disks on the first column
        self.midCol = Column(1, [])
        self.endCol = Column(2, [])
        self.moves = 0

    def updateScore(self):
        if self.moves > 1: # Just for grammar
            print(str(self.moves) + " moves made.")
        else:
            print(str(self.moves) + " move made.")

class Disk:

    def __init__(self, rank, column, y):
        # Create turtle
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(10) # highest speed possible

        self.rank = rank # Smaller rank indicates a smaller disk
        self.draw(column, False, "black", y)


    def draw(self, column, fillColor, penColor, y): # y is for the vertical position of the disk
        turtle.tracer(0, 0) # Turn off tracer
        screen.onclick(None) # Don't allow users to click when drawing, as the turtle will then begin to face the wrong direction
        width = (self.rank + 1) * 30 # Calculate width; the smallest disk will be 30 units wide
        height = 9 # Height set to be slightly less than 10
        if penColor == "lightblue": # To make sure erasing works properly. Because of aliasing, drawing in the same position won't actually cover up the old disk
          width += 15 # Increase width so that it covers the edges of the previosu disc
          height += 20
          self.rank += 0.1
          y -= 0.04 # Lower it slightly so that the bottom line is erased
          fillColor = "lightblue" # Fill it with the background color

        self.turtle.penup() # Don't start drawing
        self.turtle.setpos(column * 200 - self.rank * 15, y * 10) # Move turtle to correc starting point

        if fillColor:
            self.turtle.begin_fill() # Begin the fill process.
            self.turtle.fillcolor(fillColor)
        self.turtle.pencolor(penColor)

        # Draw the disk as a rectangle
        self.turtle.forward(width)
        self.turtle.pendown()
        self.turtle.left(90) # turtle is drawing counter clockwise, turns are measured in degrees
        self.turtle.forward(height) # Set to 9 so that lines aren't drawn over each other
        self.turtle.left(90)
        self.turtle.forward(width)
        self.turtle.left(90)
        self.turtle.forward(height)
        self.turtle.left(90)

        if fillColor:
            self.turtle.end_fill() # End fill process

        screen.onclick(click) # Allow clicks again
        turtle.update() #update screen

class Column:
    def __init__(self, columnNumber, disks):
        # Create turtle
        self.turtle = turtle.Turtle()
        self.turtle.speed(10)
        self.turtle.hideturtle()
        turtle.tracer(0, 0) # Turn off tracer

        # Draw platforms
        self.turtle.penup()
        self.turtle.setpos(columnNumber * 200 - 50, -5) # Get platform starting point
        self.columnNumber = columnNumber
        self.turtle.pencolor("white")
        self.turtle.pendown()
        self.turtle.forward(150) # Draw a line
        self.disks = disks

        self.highlighted = False # to mark if the top disc on a column is selected
        turtle.update()

    def highlight(self): # To highlight when a disc has been selected
        if self.disks: # You can't highlight a disc that doesn't exist
            if self.highlighted: # If it's already highlighted, then unhighlight it
                self.disks[-1].draw(self.columnNumber, "lightblue", "black", len(self.disks) - 1) # Draw a disk over the old disk to highlight.
                self.highlighted = False
            else:
                self.disks[-1].draw(self.columnNumber, "pink", "black", len(self.disks) - 1)
                self.highlighted = True

    def receiveDisk(self, previousColumn):
        if previousColumn.disks and (not self.disks or previousColumn.disks[-1].rank < self.disks[-1].rank): #  Make sure that the column giving disks has disks to give, and that it's smaller than the current highest disc if there is one
            diskRank = previousColumn.disks[-1].rank
            previousColumn.highlight() # This will unhighlight the previously selected column

            previousColumn.disks[-1].draw(previousColumn.columnNumber, "lightblue", "lightblue", len(previousColumn.disks) - 1)
            previousColumn.disks.pop(-1)
            self.disks.append(Disk(diskRank, self.columnNumber, len(self.disks)))
            game.moves += 1
            game.updateScore()
            return True
        return False

def click(x, y):
    if x >0 and x < 150: # If it's in the first column, check if another column is selected and the user is attempting a move. If a previous column is not selected, then they're trying to select or unselect the current one, and thus should highlight the seleced column.
        if game.midCol.highlighted:
            # When you add to add to a column, it'll return false should the move be illegal, and thus nothing will be added or removed.
            game.startCol.receiveDisk(game.midCol)
        elif game.endCol.highlighted:
            game.startCol.receiveDisk(game.endCol)
        else:
            game.startCol.highlight()
    elif x > 150 and x < 300: # If it's in the second column
        if game.startCol.highlighted:
            game.midCol.receiveDisk(game.startCol)
        elif game.endCol.highlighted:
            game.midCol.receiveDisk(game.endCol)
        else:
            game.midCol.highlight()
    elif x > 300 and x < 450: # If it's in the last column
        if game.midCol.highlighted:
            game.endCol.receiveDisk(game.midCol)
        elif game.startCol.highlighted:
            game.endCol.receiveDisk(game.startCol)
        else:
            game.endCol.highlight()

def hanoi(height, start, end, mid): # Recursive function to solve the puzzle
    if height >= 1:
        hanoi(height - 1, start, mid, end)
        end.receiveDisk(start)
        hanoi(height - 1, mid, end, start)

def solve():
    # Disable user input functions
    turtle.tracer(1, 1) # There is no sleep function when Skulpt is implemented, so instead you create a
    screen.onclick(None)
    screen.onkey(None, "s")
    hanoi(diskNumber, game.startCol, game.endCol, game.midCol)
    screen.onclick(click)
    screen.onkey(solve, "s")
    turtle.tracer(0, 0)

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Start game
game = Game()

screen.onclick(click)
screen.listen()
screen.onkey(solve, "s")
screen.listen()

screen.mainloop()
screen.listen()
