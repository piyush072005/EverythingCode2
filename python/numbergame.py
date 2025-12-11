def guess_number():
    import random
    secret = random.randint(1, 100)
    tries = 0
    while True:
        guess = int(input("Guess a number (1-100): "))
        tries += 1
        if guess == secret:
            print(f"Correct! You got it in {tries} tries.")
            break
        print("Too high!" if guess > secret else "Too low!")

def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)

if __name__ == "__main__":
    print(f"Sum of digits (12345): {sum_of_digits(12345)}")
    print(f"Is 153 Armstrong? {is_armstrong(153)}")
    guess_number()