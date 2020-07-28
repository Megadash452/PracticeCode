# --- Await, Async, Ascio ---
import time
import asyncio

def is_prime(num):
    return not any(num//i == num/i for i in range(num - 1, 1, -1))

async def highest_prime_below(num):
    for y in range(num - 1, 0, -1):
        if is_prime(y):
            print('Highest prime below ' + str(num) + ' is: \t ' + str(y))
            return y
        await asyncio.sleep(0.01)
    return none
async def main():
    t0 = time.time()

    await asyncio.wait([
        highest_prime_below(10000),
        highest_prime_below(1000),
        highest_prime_below(100),
        highest_prime_below(5)
    ])

    t1 = time.time()
    print('Took ' + str((100 * t1-t0)) + 'ms??')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# --- ---


# --- Decorators --
# --- ---

var = True


def func():
    var2 = False
    return var2


var = func()
print(var)

# --- Class and Objects ---
class Student:
    def __init__(self, name, id, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade


s1 = Student('Guacamole', 123456789, 16, 65)
s2 = Student('Sauce', 234142156, 16, 95)
s3 = Student('Pepe', 161686816, 69, 45)


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)

        else:
            print('No more students can be added')

    def course_average(self):
        value = 0
        for student in self.students:
            value += student.grade
        return value / len(self.students)


c1 = Course('Meth', 2)
c1.add_student(s1)
print(c1.students[0].name)
print(c1.course_average())
# --- --
sec = input('continue')

# --- Creating or overwriting files ---
will_write = input('want to create or overwrite something_else.txt?')
if will_write == str(1) or 'yes':
    something_else_write = open('something_else.txt', 'w')
    something_else_write.write('this is a new file. it has been created')
    something_else_write.close()
# --- ---
sec = input('continue')

# --- Writing to files ---
will_append = input('want to append to file something.txt?')
if will_append == str(1) or 'yes':
    something_append = open('something.txt', 'a')
    something_append.write('\nThis file has been appended')
    something_append.close()
# --- ---
sec = input('continue')

# --- For Loop
list1 = [1, 2, 2, 3, 4, 7, 8, 6, 9, 5, 7]

for each_num in list1:
    print(each_num)

for each_num in range(1, 11):
    print('number ' + str(each_num))
# --- ---
sec = input('Continue?')

# --- Open ---
something = open('something.txt', 'r')
print(something.readlines()[1])
something.close()
# --- ---
sec = input('Continue?')

# --- Try Except ---
try:
    numb = float(input('Enter a number:  '))
    print(numb)
except ValueError:
    print('Invalid')
# --- ---
sec = input('Continue?')


# --- Translator ---
def translate(phrase):
    translation = ''
    for space in phrase:
        if space in ' ':
            translation += ' pfft '
        else:
            translation += space
    return translation


print(translate(input('enter a word pls:  ')))
# --- ---
sec = input('Continue?')

# --- 2D Lists ---
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(str(number_grid[1][2]) + str(number_grid[2][2]))
# --- ---


# --- Nested FOR LOOP ---
for row in number_grid:
    for col in row:
        print(col)
# --- ---
sec = input('Continue?')

# --- For Loops ---
computer_parts = ['Central Processing Unit (CPU)', 'CPU Cooler', 'Mother Board (MB)', 'Random Access Memory (RAM)',
                  'Storage Drives', 'Graphics Processing Unit (GPU)', 'Power Supply Unit (PSU)', 'Case']
for part in computer_parts:
    print(part)
# --- ---
sec = input('Continue?')

# --- Guess Game ---
word = 'CBT'
guess = ''
tries = 0
out_of_tries = False

while guess != word and not out_of_tries:
    if tries < 3:
        guess = input('Say the the words...  ')
        tries += 1
    else:
        print('Badd')
        out_of_tries = True

if guess == 'CBT':
    print('YES!!!')

# --- ---
sec = input('Continue?')

# --- Dictionaries ---
month_conversions = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}
# --- ---
sec = input('Continue?')

# --- Calculator ---
print(' ---- Calculator ---- ')
num1 = float(input('Enter the FIRST number.  '))
operand = input('Enter the OPERATION you want to use.  ')
num2 = float(input('Enter the SECOND number.  '))

if operand == '+':
    print(num1 + num2)
elif operand == '-':
    print(num1 - num2)
elif operand == '*':
    print(num1 * num2)
elif operand == '/':
    print(num1 / num2)
elif operand == '^':
    print(num1 ** num2)
else:
    print('Sorry I\'m not that advanced.')
# --- ---
sec = input('Continue?')

# --- Characters ---
first_name = ['John', 'Barack', 'Julius']
last_name = ['Doe', 'Obama', 'Caesar']
age = [27, 58, 2119]
gender = ['Male', 'Male', 'Male']
dead = [True, False, True]


# --- ---


def oldest(comp1, comp2, comp3):
    if comp1 >= comp2 and comp1 >= comp3:
        return comp1
    elif comp2 >= comp1 and comp2 >= comp3:
        return comp2
    else:
        return comp3


print(oldest(age[0], age[1], age[2]))

print(month_conversions.get(5))
