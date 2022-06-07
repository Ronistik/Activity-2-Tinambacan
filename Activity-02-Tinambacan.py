

level = 90
power = 110
attack = 205
defense = 188
targets = 1
weather = 1
critical = 1
random = 0.93
stab = 1.5
type = 0.38

eq1 = (2 * level / 5 + 2)
eq2 = (power * attack / defense)
modifier = targets * weather * critical * random * stab * type 
damage = eq1 * eq2 / 50 + 2 * modifier
print(damage)




