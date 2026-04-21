#1 
'''Odd or Even Function
Fixed the comparison operator.
Initially used assignment operator = instead of comparison operator ==.
Corrected it to properly check if the number is divisible by 2.

👉 Final understanding:
Use == for comparison, not = (which is used for assignment).'''

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
#2
'''Leap Year Function
Corrected the condition based on leap year rules.
The value was mistakenly considered as 4000 instead of 400.
Fixed it to follow the correct rule:
Year divisible by 4 → leap year
Year divisible by 100 → not leap year
Year divisible by 400 → leap year

👉 Final understanding:
Leap year logic must strictly follow 400 (not 4000) condition.'''

  def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#3
'''FizzBuzz Function
Fixed logical operator mistake.
Initially used incorrect operator (or) instead of and.

Corrected to:

if number % 3 == 0 and number % 5 == 0
This ensures "FizzBuzz" is printed only when both conditions are true.

👉 Final understanding:
Use and when both conditions must be satisfied.'''

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
