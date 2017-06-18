year_list = [1992, 1993, 1994, 1995, 1996, 1997]
print('''I was 3 years old in''',year_list[3])
print(year_list.pop(),'''is the oldest year''')
###################################################
things = ['mozzarella','cinderella','salmonella']
print(things)
THINGS = list(things)
THINGS[0] = THINGS[0].capitalize()
THINGS[1] = THINGS[1].capitalize()
THINGS[2] = THINGS[2].capitalize()
print(THINGS)
things[0] = things[0].upper()
print(THINGS)
things.remove('salmonella')
print(things)
###################################################
surprise = ['Groucho','Chico','Harpo']
surprise[2] = surprise[2].lower()
print(surprise)
temp = surprise[2]
pmet = temp[::-1]
surprise[2] = pmet
print(surprise)
##################################################
e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f.items())
f2e = {v:k for k,v in e2f.items()}
print(f2e.items())
print(f2e['chien'])
e = set(e2f)
print(e)
###################################################
cats = ['Henri', 'Grumpy', 'Lucy']
animals = {'cats':cats,'octopi':{},'emus':{}}
life = {
    'animals':animals,
    'plants':{},
    'others':{}
}
print(life.keys())
print(life['animals'].items())
print(life['animals']['cats'])