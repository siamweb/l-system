import math

class PSTurtle:

    colorline = ("\n/colorline {\n"
            "newpath\n"
            "setlinewidth\n"
            "setrgbcolor\n"
            "moveto\n"
            "lineto\n"
            "stroke\n"
            "} def")


    def __init__(self, x, y, o):

        # turtle state
        self.xPos = x
        self.yPos = y
        self.orientation = o

        # pen state
        self.penWidth = 2
        self.pen = True
        self.penColor = (1, 0, 1)

        # image parameters
        self.xMin = x
        self.xMax = x
        self.yMin = y
        self.yMax = y

        # postscript string
        self.ps = ""

    def updateBoundaries(self):
        if self.xPos < self.xMin:
            self.xMin = self.xPos

        if self.xPos > self.xMax:
            self.xMax = self.xPos

        if self.yPos < self.yMin:
            self.yMin = self.yPos

        if self.yPos > self.yMax:
            self.yMax = self.yPos

    def place(self, x, y, o):

        if self.ps != "":
            self.ps += "\nstroke"
        
        self.ps += "\nnewpath\n" + str(x) + " " + str(y) + " moveto"

        self.xPos = x
        self.yPos = y
        self.orientation = o

    def turn(self, o):
        self.orientation += o

    def move(self, l):
        o = self.orientation * math.pi / 180

        newXPos = self.xPos + l * math.cos(o)
        newYPos = self.yPos + l * math.sin(o)

        if self.ps == "":
            self.place(self.xPos, self.yPos, self.orientation)

        self.ps += "\n"
        self.ps += str(newXPos) + " " + str(newYPos) + " lineto"

        self.xPos = newXPos
        self.yPos = newYPos

        self.updateBoundaries()


    def write(self, filename):
        f = open(filename, 'w')
        f.write("%!PS-Adobe-3.0 EPSF-3.0")

        bound = "\n%%BoundingBox:" 
        bound += " " + str(self.xMin) + " " + str(self.yMin)
        bound += " " + str(self.xMax) + " " + str(self.yMax)
        f.write(bound)

        f.write( "\n0 setlinejoin\n" + 
                str(self.penWidth) + " setlinewidth\n" + 
                str(self.penColor[0]) + " " + str(self.penColor[1]) + 
                " " + str(self.penColor[2]) + " setrgbcolor")

        f.write(self.ps)

        f.write("\nstroke")




