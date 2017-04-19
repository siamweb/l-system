import lsystem as l


# KOCH CURVE
v1 = l.Variable("F", "F+F-F-F+F", 0, 100)
v2 = l.Variable("+", "+", 90, 0)
v3 = l.Variable("-", "-", -90, 0)

koch = l.LSystem([v1, v2, v3], "F", []) 

koch.draw("koch.ps", koch.evolve(4), 0)


# SIERPINSKI
v4 = l.Variable("A", "+B-A-B+", 0, 100)
v5 = l.Variable("B", "-A+B+A-", 0, 100)
v6 = l.Variable("+", "+", 60, 0)
v7 = l.Variable("-", "-", -60, 0)

sierpinski = l.LSystem([v4, v5, v6, v7], "A", [])

sierpinski.draw("sierpinski.ps", sierpinski.evolve(6), 0)


# PYTHAGORAS TREE

v8 = l.Variable("0", "1[0]0", 0, 5)
v9 = l.Variable("1", "11", 0 , 10)
v10 = l.Variable("[", "[", 45, 0)
v11 = l.Variable("]", "]", -45, 0)

m1 = l.Memory(v10, v11, True)


pyth = l.LSystem([v8, v9, v10, v11], "0", [m1])


pyth.draw("pyth.ps", pyth.evolve(8), 90)


# FRACTAL PLANT

v12 = l.Variable("X" ,"F-[[X]+X]+F[+FX]-X", 0, 0)
v13 = l.Variable("F" , "FF", 0, 10)
v14 = l.Variable("-", "-", -25, 0)
v15 = l.Variable("+", "+", 25, 0)
v16 = l.Variable("[", "[", 0, 0)
v17 = l.Variable("]", "]", 0, 0)

m2 = l.Memory(v16, v17, True)

plant = l.LSystem([v12, v13, v14, v15, v16, v17], "X", [m2])

plant.draw("plant.ps", plant.evolve(6), 60)



# FLOWSNAKE

f1 = l.Variable("A", "A-B--B+A++AA+B-", 0, 10)
f2 = l.Variable("B", "+A-BB--B-A++A+B", 0, 10)
f3 = l.Variable("-", "-", -60, 0)
f4 = l.Variable("+", "+", 60, 0)

flow = l.LSystem([f1, f2, f3, f4], "A", [])

flow.draw("flow.ps", flow.evolve(4), 45)
