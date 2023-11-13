import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within the specified range.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generates a random operator from '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])
    


def calculate_result(num1, num2, operator):
    """
    Calculates the result of an arithmetic operation and returns the problem and correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer



def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, correct_answer = calculate_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")
   

    try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")
        
    print(f"\nQuiz completed. Your final score is {score}/{total_questions}.")



if __name__ == "__main__":
    math_quiz()
