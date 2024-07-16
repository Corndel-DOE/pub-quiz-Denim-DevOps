# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "B"
    },

    {
        "question": "What is 5 + 3?",
        "options": ["A) 8", "B) 2", "C) 1", "D) 23"],
        "answer": "A"
    },

    {
        "question": "The capital of England is London. True or False?",
        "options": ["True", "False"],
        "answer": "True"
    },
    # Learners can add more questions here following the same structure
]

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    if question == "The capital of England is London. True or False?":
        user_answer = input("Your answer (True, False): ").strip().upper()
    else: 
        user_answer = input("Your answer: ").strip().upper()
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print("Thanks for playing the Pub Quiz!")
