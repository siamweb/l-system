import lsystem as l

# FLOWSNAKE

f1 = l.Variable("A", "A-B--B+A++AA+B-", 0, 10)
f2 = l.Variable("B", "+A-BB--B-A++A+B", 0, 10)
f3 = l.Variable("-", "-", -60, 0)
f4 = l.Variable("+", "+", 60, 0)

flow = l.LSystem([f1, f2, f3, f4], "A", [])

n = 4

flow.draw("flowsnake.ps", flow.evolve(n), 45, [0, 0, 1], 4)
