import random

def quiz_game():
    questions = [
        {"q": "What is 5 + 3?", "a": "8"},
        {"q": "What is the capital of France?", "a": "Paris"},
        {"q": "What color is the sky?", "a": "Blue"}
    ]
    
    score = 0
    random.shuffle(questions)
    
    for question in questions:
        answer = input(question["q"] + " ")
        if answer.lower() == question["a"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer was {question['a']}")
    
    print(f"Your score: {score}/{len(questions)}")

def number_game():
    number = random.randint(1, 10)
    attempts = 0
    
    while attempts < 3:
        guess = int(input("Guess a number between 1-10: "))
        attempts += 1
        
        if guess == number:
            print("You win!")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
    
    print(f"Game over! The number was {number}")

while True:
    print("\n1. Quiz Game")
    print("2. Number Game")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        quiz_game()
    elif choice == "2":
        number_game()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")