from collections import deque
import psturtle

class Variable:
    """
    Symbol in the alphabet
    """
    def __init__(self, name, rule, rotation=0, length=1):
        """ Constructor
        input:
            name : symbol name (string)
            rule : production rule (string)
            rotation : rotation applied when rendering (float)
            length : length of line when rendering (float)
        """
        self.name = name
        self.rule = rule
        self.rotation = rotation
        self.length = length

    def draw(self):
        """ Draw the variable
            output:
                rotation
                length
        """
        return self.rotation, self.length

class Memory:
    """
    Memory variable in the alphabet
    """
    def __init__(self, saveV, retV, stack):
        """Constructor
        input: 
            saveV : symbol indicating when to start saving (string)
            retV : symbol indicating when to retrieve a state stored in the memory (string)
            stack : store the variables in a stack otherwise use a queue (bool)
        """
        self.saveVar = saveV
        self.retVar = retV
        self.useStack = stack

        if stack:
            self.mem = []
        else:
            self.mem = deque()


    def save(self, x, y, rot):
            """ Save state of turtle
                input :
                    x : x position 
                    y : y position
                    rot : rotation
            """
            return self.mem.append((x, y,rot))
        
    def retreive(self):
        """ Retrieve a state
        """
        if self.useStack:
            return self.mem.pop()
        else:
            return self.mem.popleft()



class LSystem:
    """ L-system
    """

    def __init__(self, var, init, mems):
        """ Constructor
        input:
            var : variables (list of Variable)
            init : initialization string (string)
            mems : memory variables
        """
        self.initState = init

        # Mapping from symbol to variable
        self.variables = dict([ (v.name, v) for v in var])

        # Mapping from variables to memory
        self.saveVars = dict([(m.saveVar, m) for m in mems])
        self.retVars = dict([(m.retVar, m) for m in mems])


    def nextState(self,state):        
        """ get the next state of the system by applying the production rule
        input:
            state : current state
        output:
            nextS : next state
        """
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
        """ Evolve the system for n steps
        input:
            n : number of steps (int)
        output:
            state : evolved state of the system
        """
        state = self.initState
        for i in range(n):
            state = self.nextState(state)

        return state

    def draw(self, filename, state, orientation=0, color=[0,0,0], width=1):
        """ Render state of L-System to PostScript 
        """
        
        turtle = psturtle.PSTurtle(0, 0, orientation)
        turtle.penColor = color
        turtle.penWidth = width

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

                    

