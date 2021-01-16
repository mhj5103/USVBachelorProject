import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero
#https://naysan.ca/2020/09/16/python-plot-cartesian-coordinate-systems-with-points/
class Point():
    
    def __init__(self, x, y, color='#4ca3dd', size=50, add_coordinates=True):
        self.x = x
        self.y = y
        self.color = color
        self.size  = size
        self.add_coordinates = add_coordinates
        self.y_offset = 0.2
        self.items = np.array([x,y])
        self.len = 2
        
    def __getitem__(self, index):
        return self.items[index]
    
    def __str__(self):
        return "Point(%.2f,%.2f)" % (self.x, self.y)
    
    def __repr__(self):
        return "Point(%.2f,%.2f)" % (self.x, self.y)
    
    def __len__(self):
        return self.len
    
    def draw(self):
        plt.scatter([self.x], [self.y], color=self.color, s=self.size)
        
        # Add the coordinates if asked by user
        