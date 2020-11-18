#from dataclasses import dataclass
#from dataclasses import field


#@dataclass
class Object:
    r"""Defines an object with some of its properties. 
    
    An object can be an obstacle, free space or food etc. It can also have properties like impassable, positions.
    
    """
    def __init__(self, name, value, rgb, impassable, positions):
        self.name = name
        self.value = value
        self.rgb = rgb
        self.impassable = impassable
        self.positions = positions
