

def run_quiz(questions):
    score = 0
    print("\n🎯 Welcome to the Python Quiz Game! 🎯")
    print("You’ll get 1 point for each correct answer.\n")
    
    for i, question in enumerate(questions, start=1):
        print(f"\nQ{i}. {question['question']}")
        for option in question['options']:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == question['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {question['answer']}")
    
    print("\n🎉 Quiz Completed!")
    print(f"Your final score: {score}/{len(questions)}")
    print("Thanks for playing!\n")

# List of questions
quiz_questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a mutable data type?",
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
