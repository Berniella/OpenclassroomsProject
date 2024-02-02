class ToolBox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):

        self.tools.append(tool)

    def remove_tool(self, tool):

        index = self.tools.index(tool)
        del self.tools[index]
#Tool1= ToolBox()
#Tool1.add_tool("Marteau")
#Tool1.add_tool("Cloux")
#Tool1.remove_tool("Cloux")
#print(Tool1.tools)

class Screwdriver:
    def __init__(self, size=3):
        self.size = size
    def tighten(self, screw):
        screw.tighten()
    def loosen(self, screw):
        screw.loosen()
    def __repr__(self):
        return f"Marteau de couleur {self.color}"

class Hammer:
    def __init__(self, color="red"):
        self.color = color
    def paint(selfself, color):
        self.color = color
    def hammer_in(self, nail):
        nail.nail_in()
    def remove(self, nail):
        nail.remove()
    def __repr__(self):
        return f"Marteau de couleur {self.color}"
class Screw:
    MAX_TIGHTNESS = 5

    def __init__(self):
        self.tightness = 0
    def loosen(self):
        if self.tightness > 0:
        self.tightness -= 1
    def tighten(self):
        if self.tightness < self.MAX_TIGHTNESS:
        self.tightness += 1
    def __str__(self):
        return "Vis avec un serrage de {}".format(self.tightness)

class Nail:
    def __init__(self):
        self.in_wall = False
    def nail_in(self):
        if not self.in_wall:
        self.in_wall = True
    def remove(self):
        if self.in_wall:
        self.in_wall = False
    def __str__(self):
        wall_state = "dans le mur" if self.in_wall else "hor du mur"
        return f"Clou{wall_state}"

Box1 = ToolBox()
Tournevis1 = Screwdriver(2)
Marteau1 = Hammer(blue)

Box1.add_tool("Tournevis1")
Box1.add_tool("Marteau")

Vis1 = Screw()
print(Vis1)
Tournevis1.tighten(Vis1)
print(Vis1)

Clou1 = Nail()
print(Clou1)
Hammer.hammer_in(Marteau1,Clou1)
print(Clou1)