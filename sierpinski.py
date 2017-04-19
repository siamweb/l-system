import lsystem as l

# SIERPINSKI
v1 = l.Variable("A", "+B-A-B+", 0, 10)
v2 = l.Variable("B", "-A+B+A-", 0, 10)
v3 = l.Variable("+", "+", 60, 0)
v4 = l.Variable("-", "-", -60, 0)

sierpinski = l.LSystem([v1, v2, v3, v4], "A", [])

n = 8

sierpinski.draw("sierpinski.ps", sierpinski.evolve(n), 0, [0, 0, 0.9], 5)


