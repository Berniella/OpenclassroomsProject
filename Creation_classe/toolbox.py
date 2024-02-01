class ToolBox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):

        self.tools.append(tool)

    def remove_tool(self, tool):

        index = self.tools.index(tool)
        del self.tools[index]

Tool1= ToolBox()
Tool1.add_tool("Marteau")
Tool1.add_tool("Cloux")
Tool1.remove_tool("Cloux")
print(Tool1.tools)

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



