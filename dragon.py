import lsystem as l


v1 = l.Variable("X", "X+YF+", 0, 0)
v2 = l.Variable("Y", "-FX-Y", 0, 0)

v3 = l.Variable("+", "+", -90, 0)
v4 = l.Variable("-", "-", 90, 0)

v5 = l.Variable("F", "F", 0, 10)


dragon = l.LSystem([v1, v2, v3, v4, v5], "FX", [])

n = 14

dragon.draw("dragon.ps", dragon.evolve(n), 45, [0, 0, 0.5], 1)

