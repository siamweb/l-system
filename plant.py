import lsystem as l

delta = 20

# Branch
v1 = l.Variable("X" ,"F-[[X]+X]+F[+FX]-X", 0, 0)
v2 = l.Variable("F" , "FF", 0, 5)


# Symmetric
#v1 = l.Variable("X" ,"F[+X][-X]FX", 0, 0)
#v2 = l.Variable("F" , "FF", 0, 5)

# Bush
#v1 = l.Variable("F", "F[+F]F[-F][F]", 0, 10)

minus = l.Variable("-", "-", -25.7, 0)
plus  = l.Variable("+", "+", 25.7, 0)
s1 = l.Variable("[", "[", 0, 0)
s2 = l.Variable("]", "]", 0, 0)

m = l.Memory(s1, s2, True)


plant = l.LSystem([v1, v2, minus, plus, s1, s2], "X", [m])
#plant = l.LSystem([v1, minus, plus, s2, s1], "F", [m])

n = 8

plant.draw("plant.eps", plant.evolve(n), 0, [0.3, 0.7, 0.3], 3)



