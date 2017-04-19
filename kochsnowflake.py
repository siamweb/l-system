import lsystem as l

v1 = l.Variable("F", "F-F++F-F", 0, 2)
v2 = l.Variable("+", "+", 60, 0)
v3 = l.Variable("-", "-", -60, 0)


snowflake = l.LSystem([v1, v2, v3], "F++F++F", [])

n = 4

snowflake.draw("snowflake.ps", snowflake.evolve(n), 0, [0, 0, 1], 1)
