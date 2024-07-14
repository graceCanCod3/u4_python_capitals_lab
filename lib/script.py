import random
from capitals import states

correct_answers = 0
incorrect_answers = 0
total_questions = 0
play_again = True

def state_capitals_quiz():
    global correct_answers, incorrect_answers, total_questions
    
    # Welcome message
    print("Welcome to the State Capitals Quiz!")
    
    while True:
        # Shuffle the states to make the game more challenging
        random.shuffle(states)
        
        for state in states:
            # Prompt user for the capital of the state
            state_name = state["name"]
            correct_capital = state["capital"]
            
            # Create a shuffled list of capitals excluding the correct one
            all_capitals = [s["capital"] for s in states]
            all_capitals.remove(correct_capital)
            wrong_capitals = random.sample(all_capitals, 3)
            options = wrong_capitals + [correct_capital]
            random.shuffle(options)
            
            # Present the question
            print(f"What is the capital of {state_name}?")
            for idx, option in enumerate(options):
                print(f"{idx + 1}. {option}")
            
            # Get user's answer
            user_answer = input("Enter the number of your answer: ")
            user_answer = options[int(user_answer) - 1]  # Adjust for 0-based index
            
            # Check if the answer is correct
            if user_answer == correct_capital:
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Sorry, the correct answer is {correct_capital}.")
                incorrect_answers += 1
            
            total_questions += 1
            print(f"Score: {correct_answers}/{total_questions}")
            print()
        
        # After all questions are answered
        print("Quiz complete!")
        print(f"Final Score: {correct_answers}/{total_questions}")
        
        # Ask if the user wants to play again
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != "yes":
            print("Thank you for playing!")
            break  # Exit the while loop and end the game

# Start the game
state_capitals_quiz()
