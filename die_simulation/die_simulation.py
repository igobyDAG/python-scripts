from die import Die

die = Die(10)
print('Die sides: ',die.sides[1:])

simulation = die.simulate(3000)
print(die.count_ocurrences(simulation))
die.graph_display(simulation)
