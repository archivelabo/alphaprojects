import random # Library to generate random numbers
import urllib.request
import re
categories = ["All",
              "General Knowledge",
              "Entertainment: Books",
              "Entertainment: Film",
              "Entertainment: Music",
              "Entertainment: Musicals & Theatres",
              "Entertainment: Television",
              "Entertainment: Video Games",
              "Entertainment: Board Games",
              "Science & Nature",
              "Science: Computers",
              "Science: Mathematics",
              "Mythology",
              "Sports",
              "Geography",
              "History",
              "Politics",
              "Art",
              "Celebrities",
              "Animals",
              "Vehicles",
              "Entertainment: Comics",
              "Science: Gadgets",
              "Entertainment: Japanese Anime & Manga",
              "Entertainment: Cartoon & Animations"
            ] # These are the categories. Students can choose not to inclue them all.
difficulties = ["easy", "medium", "hard", "random"]
def html_decode(s):
    s = s.replace('&#039;', "'")
    s = s.replace('&quot;', '"')
    return s

def ask(q):
    # Print the question
    question = re.search(r'question":"(.*?)"', str(q)).group(0)[11:-1] if re.search(r'question":"(.*)"', str(q)) else ""
    print(html_decode(question))
    correctAnswer = html_decode(re.search(r'correct_answer":"(.*?)"', str(q)).group(0)[17:-1]) if re.search(r'correct_answer":"(.*)"', str(q)) else ""

    answerOptions = eval(html_decode(re.search(r'incorrect_answers":\[(.*?)\]', str(q)).group(0)[19:])) if re.search(r'incorrect_answers":\[(.*?)\]', str(q)) else ""

    answerOptions.append(correctAnswer)

    random.shuffle(answerOptions) # Make sure that the correct answer isn't always last or first or wherever the student places it in the answer options

    print("Your possible answers are:")

    for i in range(len(answerOptions)): # Loop through options
        print("  " + str(i + 1) + ". " + answerOptions[i]) # Don't forget to unescape!

    userAnswer = answerOptions[int(input("Input the correct answer number, or 0 for a new set of questions. ")) - 1] # Subtract one as arrays index at 0

    if userAnswer == correctAnswer:
        print("You got it right! Congratulations!")
        return True
    elif userAnswer == 0: # If they want a new set of questions
        return "restart"
    else:
        print("Oh no! The correct answer was " + correctAnswer + "\n") # If they got it wrong
        return False
#
def question(category, difficulty, data):
    score = 0 # Start keeping score
    res = ask(data) # res is for result
    if not res:
        print("Your score was " + str(score) + " in " + category + " with an " + difficulty + " difficulty.")
        return
    elif res == "restart":
        return
    else:
        score += 1

while True: # Game loop

    # Print category options
    print("Your categories options are:")
    for i in range(len(categories)):
        print("  " + str(i + 1) + ". " + categories[i])

    # Loop to ask for input
    while True: # Loop required to validate input
        category = int(input("Which category number do you want?"))-1
        if category > len(categories): # If input invalid
            print("Uh oh, please pick one of the valid options!")
        else: # If input valid
            category = categories[category]
            break


    # Loop to ask for input
    while True:
        difficulty = input("Do you want easy, medium or hard problems? Input \"random\" for a random difficulty.").lower()
        if difficulty not in difficulties:
            print("Uh oh, please pick one of the valid options!")
        else:
            break

    # Open file
    if category == 0 and difficulty == "random":
        url = 'https://opentdb.com/api.php?amount=1'
    elif category == 0:
        url = 'https://opentdb.com/api.php?amount=1&difficulty=' + difficulty
    elif difficulty == "random":
        url = 'https://opentdb.com/api.php?amount=1&category=' + str(categories.index(category) + 8)
    else:
        url = 'https://opentdb.com/api.php?amount=1&category=' + str(categories.index(category) + 8) + '&difficulty=' + difficulty
    question(category, difficulty, urllib.request.urlopen(url).read())
    print("Restarting!")
