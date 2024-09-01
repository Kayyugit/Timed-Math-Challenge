import random
import time

# If you want the game to be more challenging, you can increase the range
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' + operator + ' ' + str(right)
    answer = eval(expr)
    return expr, answer

def get_total_problems():
    while True:
        try:
            total_problems = int(input("Enter the number of problems (1 - 20): "))
            print('----------------------------------')
            if 1 <= total_problems <= 20:
                return total_problems
            else:
                print("Out of range. Please enter a number between 1 and 20.")
                print('----------------------------------')
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 20.")
            print('----------------------------------')

wrong = 0
print("Welcome to this Timed Math Challenge")
print("Answer as quickly as possible. Goodluck!")
input('Press Enter to start!')
print('----------------------------------')
total_problems = get_total_problems()

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input(f'Problem #{i + 1}: {expr} = ')
        print('...............................')
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time)

print('Nice work! You finished', total_problems, 'problems in', total_time, 'seconds.' )
print(f'You answered {total_problems} problems with {wrong} wrong attempts.')
print('----------------------------------')
