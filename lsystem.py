from collections import deque
import psturtle as t

class Variable:
    def __init__(self, name, rule, rotation, length):
        self.name = name
        self.rule = rule
        self.rotation = rotation
        self.length = length

    def draw(self):
        return self.rotation, self.length

class Memory:
    def __init__(self, saveV, retV, stack):
        self.saveVar = saveV
        self.retVar = retV
        self.useStack = stack

        if stack:
            self.mem = []
        else:
            self.mem = deque()


    def save(self, x, y, rot):
            return self.mem.append((x, y,rot))
        
    def retreive(self):
        if self.useStack:
            return self.mem.pop()
        else:
            return self.mem.popleft()



class LSystem:
    def __init__(self, var, init, mems):
        self.initState = init

        # Mapping from symbol to variable
        self.variables = dict([ (v.name, v) for v in var])

        # Mapping from variables to memory
        self.saveVars = dict([(m.saveVar, m) for m in mems])
        self.retVars = dict([(m.retVar, m) for m in mems])


    def nextState(self,state):        
        nextS = ""
        for c in state:
            #check if there is a rule for c
            if c in self.variables:
                v = self.variables[c]
                nextS += v.rule
            else:
                #If there is no rule for c just leave it
                nextS += c

        return nextS

    def evolve(self, n):
        state = self.initState
        for i in range(n):
            state = self.nextState(state)

        return state

    def draw(self, filename, state, orientation, color, penwidth):
        
        turtle = t.PSTurtle(0, 0, orientation)
        turtle.penColor = color
        turtle.penWidth = penwidth

        for c in state:
            #check if there is a draw rule for c
            if c in self.variables:
                v = self.variables[c]
    
                if v in self.saveVars:
                    m = self.saveVars[v]
                    m.save(turtle.xPos, turtle.yPos, turtle.orientation)

                if v in self.retVars:
                    x, y, o = m.retreive()
                    turtle.place(x, y, o)

                r, l = v.draw()
    
                if r != 0:
                    turtle.turn(r)
                if l != 0:
                    turtle.move(l)
    

        turtle.write(filename)

                    

