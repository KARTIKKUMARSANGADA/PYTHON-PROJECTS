

def run_quiz(questions):
    score = 0
    print("\nWelcome to the Python Quiz Game!")
    print("You will get 1 point for each correct answer.\n")

    # Loop through all the questions
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)

        
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        # Check if answer is correct
        if answer == q['answer']:
            print("✅ Correct Answer!")
            score += 1
        else:
            print(f"❌ Oops! The correct answer was {q['answer']}")

    
    print("\n---------------------------------")
    print("🎉 Quiz Completed! 🎉")
    print(f"Your final score is: {score} / {len(questions)}")
    print("Thanks for playing!\n")
    print("---------------------------------")

# List of quiz questions
quiz_questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["A) Tuple", "B) String", "C) List", "D) Integer"],
        "answer": "C"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A) .pt", "B) .py", "C) .pyt", "D) .python"],
        "answer": "B"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A) input()", "B) scan()", "C) get()", "D) readline()"],
        "answer": "A"
    }
]

# Start the quiz
run_quiz(quiz_questions)
