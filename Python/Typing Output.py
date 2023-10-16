import time
import random
import sys

Value = 3432

# Thank you KOTZ on Stackoverflow for the fake_type function.


def fake_type(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice(
            [0.3, 0.11, 0.08, 0.07, 0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(char)
        sys.stdout.flush(

        )
    time.sleep(1)


# for i in range(1, 10 + 1):
    # fake_type(f"This is test {i}.")
# fake_type("All tests are complete!")

fake_type("Write a statement that subtracts 3 from i and then multiplies by 2: ")
statement = input()
for i in range(20, 25):
    statement
    if i == 20 and eval(statement) == 34:
        fake_type("Test 1 passed.")
        Passed1 = True
    elif i == 20 and eval(statement) != 34:
        fake_type("Test 1 failed.")
        Passed1 = False
    elif i == 21 and eval(statement) == 36:
        fake_type("Test 2 passed.")
        Passed2 = True
    elif i == 21 and eval(statement) != 36:
        fake_type("Test 2 failed.")
        Passed2 = False
    elif i == 22 and eval(statement) == 38:
        fake_type("Test 3 passed.")
        Passed3 = True
    elif i == 22 and eval(statement) != 38:
        fake_type("Test 3 failed.")
        Passed3 = False
    elif i == 23 and eval(statement) == 40:
        fake_type("Test 4 passed.")
        Passed4 = True
    elif i == 23 and eval(statement) != 40:
        fake_type("Test 4 failed.")
        Passed4 = False
    elif i == 24 and eval(statement) == 42:
        fake_type("Test 5 passed.")
        Passed5 = True
    elif i == 24 and eval(statement) != 42:
        fake_type("Test 5 failed.")
        Passed5 = False
    else:
        fake_type("Error, try again.")
        continue


if Passed1 == True and Passed2 == True and Passed3 == True and Passed4 == True and Passed5 == True:
    fake_type("You passed all the tests.")
else:
    fake_type("One or more tests failed.")
