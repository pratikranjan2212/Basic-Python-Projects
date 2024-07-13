# This is a simple implementation of the game Kaun Banega Crorepati (KBC) in Python.

# The game has 16 questions with 4 options each. The player has to choose the correct option to win points.

# The player can quit the game at any time by pressing Q.

# Created a list of questions, options, answers, and levels.
questions=[
    "Which language was used to develop Facebook?",
    "What is the capital of France?",
    "Who is the CEO of Tesla?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?",
    "What is the largest ocean in the world?",
    "What is the national animal of Australia?",
    "What is the currency of Japan?",
    "What is the tallest mountain in the world?",
    "What is the largest mammal on Earth?",
    "Who wrote the play Romeo and Juliet?",
    "What is the largest desert in the world?",
    "What is the main component of air?",
    "What is the largest country in the world by land area?",
    "What is the highest-grossing film of all time?",
    "Who is the author of the Harry Potter series?"
]

options=[
    [
        "Python","JavaScript","PHP","SQL"
    ],
    [
        "London","Paris","Berlin","Rome"
    ],
    [
        "Elon Musk","Jeff Bezos","Mark Zuckerberg","Tim Cook"
    ],
    [
        "Jupiter","Saturn","Mars","Earth"
    ],
    [
        "Au","Ag","Fe","Hg"
    ],
    [
        "Pacific Ocean","Atlantic Ocean","Indian Ocean","Arctic Ocean"
    ],
    [
        "Kangaroo","Koala","Platypus","Emu"
    ],
    [
        "Yen","Dollar","Euro","Pound"
    ],
    [
        "Mount Everest","K2","Kangchenjunga","Makalu"
    ],
    [
        "Elephant","Blue Whale","Giraffe","Hippopotamus"
    ],
    [
        "William Shakespeare","Jane Austen","Charles Dickens","F. Scott Fitzgerald"
    ],
    [
        "Sahara Desert","Gobi Desert","Antarctic Desert","Arabian Desert"
    ],
    [
        "Nitrogen","Oxygen","Carbon Dioxide","Argon"
    ],
    [
        "Russia","Canada","China","United States"
    ],
    [
        "Avengers: Endgame","Avatar","Titanic","Star Wars: The Force Awakens"
    ],
    [
        "J.K. Rowling","Stephen King","George R.R. Martin","Dan Brown"
    ]
]

answers=[
    'b',
    'b',
    'a',
    'a',
    'a',
    'a',
    'a',
    'a',
    'a',
    'b',
    'a',
    'a',
    'b',
    'a',
    'a',
    'a'
]

levels=[
    1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000
]

points=0

# Loop through the questions
for i in range(0,len(questions)):
    ques=questions[i]
    print(f"Question for {levels[i]} points:", ques)
    print(f"a. {options[i][0]}             b. {options[i][1]}")
    print(f"c. {options[i][2]}             d. {options[i][3]}")
    reply=(input("Enter your answer (a,b,c,d) or Q to Quit:"))
    if reply==answers[i]:
        print("Correct answer")
        print("You have won",levels[i],"points")
        
        if i==4:
            points=levels[i]
        elif i==9:
            points=levels[i]
        elif i==14:
            points=levels[i]
        else:
            points=0
    
    elif reply=="Q":
        print("You have quit the game")
        print(f"Your takeaway points are {points}")
        break
    
    else:
        print("Wrong answer")
        print(f"Your takeaway points are {points}")
        break