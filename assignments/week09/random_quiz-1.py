"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.
    
    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""
import random
test_random = random.randint(1,20)
print (" เกม ทาย ตัว เลข")
print (" ทาย จำ นวน เลข 1 - 20")
print (" คุณ มี โอ กาส 6 ครั้ง")
for i in range(6):
    print (F"ความพยายามครั้งที่{i+1}")
    guess_number = int(input("what is your number (1-20):"))
    if test_random == guess_number:
        print ("เก่งมากๆๆๆ ไออ้่วน")
        break
    elif test_random < guess_number:
        print ("น้อยไปนะเพิ่มอีกหน่อย")
    elif test_random > guess_number:
        print ("มากไปนะลดอีกนิด")
