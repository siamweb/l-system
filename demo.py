import lsystem


# KOCH CURVE
v1 = lsystem.Variable("F", "F+F-F-F+F", 0, 1)
v2 = lsystem.Variable("+", "+", 90, 0)
v3 = lsystem.Variable("-", "-", -90, 0)

koch = lsystem.LSystem([v1, v2, v3], "F", []) 

koch.draw("koch.ps", koch.evolve(4), width=0.5)

# SIERPINSKI
v4 = lsystem.Variable("A", "+B-A-B+", 0, 1)
v5 = lsystem.Variable("B", "-A+B+A-", 0, 1)
v6 = lsystem.Variable("+", "+", 60, 0)
v7 = lsystem.Variable("-", "-", -60, 0)

sierpinski = lsystem.LSystem([v4, v5, v6, v7], "A", [])

sierpinski.draw("sierpinski.ps", sierpinski.evolve(6), color=[0,0,1], width=0.5)


# PYTHAGORAS TREE

v8 = lsystem.Variable("0", "1[0]0", 0, 1)
v9 = lsystem.Variable("1", "11", 0 , 2)
v10 = lsystem.Variable("[", "[", 45, 0)
v11 = lsystem.Variable("]", "]", -45, 0)

m1 = lsystem.Memory(v10, v11, True)


pyth = lsystem.LSystem([v8, v9, v10, v11], "0", [m1])


pyth.draw("pyth.ps", pyth.evolve(8), orientation=90, width=0.5)


# FRACTAL PLANT

v12 = lsystem.Variable("X" ,"F-[[X]+X]+F[+FX]-X", 0, 0)
v13 = lsystem.Variable("F" , "FF", 0, 1)
v14 = lsystem.Variable("-", "-", -25, 0)
v15 = lsystem.Variable("+", "+", 25, 0)
v16 = lsystem.Variable("[", "[", 0, 0)
v17 = lsystem.Variable("]", "]", 0, 0)

m2 = lsystem.Memory(v16, v17, True)

plant = lsystem.LSystem([v12, v13, v14, v15, v16, v17], "X", [m2])

plant.draw("plant.ps", plant.evolve(5), orientation=20, color=[0,0.5,0], width=0.5)



# FLOWSNAKE

f1 = lsystem.Variable("A", "A-B--B+A++AA+B-", 0, 1)
f2 = lsystem.Variable("B", "+A-BB--B-A++A+B", 0, 1)
f3 = lsystem.Variable("-", "-", -60, 0)
f4 = lsystem.Variable("+", "+", 60, 0)

flow = lsystem.LSystem([f1, f2, f3, f4], "A", [])

flow.draw("flow.ps", flow.evolve(4), orientation=45, width=0.5)
