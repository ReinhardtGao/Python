guess_me = 7
start = 1
if guess_me < 7:
    print("Too low")
elif guess_me > 7:
    print("Too high")
else:
    print("Just right!")
while 1:
    start += 1
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("found it!")
    else:
        print("oops")
        break
################################
list_3 = [3, 2, 1, 0]
for value in list_3:
    print(value)
################################
list_4 = [number for number in range(10) if number % 2 == 0]
print(list_4)
################################
squares = {number: number * number for number in range(10)}
print(squares)
################################
odd = {number for number in range(10) if number % 2 == 1}
print(odd)
################################
list_7 = [number for number in range(10)]
for l in list_7:
    print("Got ", l)


################################
def good():
    list_8 = ['Harry', "Ron", "Hermione"]
    print(list_8)
    return 0


good()


################################
def get_odds():
    for number in range(10):
        if number % 2 == 1:
            yield number


for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("The third number is:", number)


################################
def test(func):
    def new_func():
        print("Start")
        output = func
        print("Stop")
        return output

    return new_func()


@test
def load():
    print("Load of the Ring!!!")


load()


#################################
class OopException(Exception):
    print("Oops!")


Series = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   #In order to make the program keep running, deleted '''-''' in front of 10
for s in Series:
    if s < 0:
        raise OopException(s)


#################################
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)