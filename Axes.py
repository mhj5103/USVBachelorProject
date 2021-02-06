import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axisartist import SubplotZero
class Axes():
    
    def __init__(self, xlim=(-5,5), ylim=(-5,5), figsize=(12,5)):
        self.xlim = xlim
        self.ylim = ylim
        self.figsize  = figsize
        self.points   = []
        self.segments = []
        self.vectors  = []
        self.lines    = []
        self.scale_arrows()

    def __arrow__(self, x, y, dx, dy, width, length):
        plt.arrow(
            x, y, dx, dy, 
            color       = 'k',
            clip_on     = False, 
            head_width  = self.head_width, 
            head_length = self.head_length
        ) 
        
    def __drawAxis__(self):
        """
        Draws the 2D cartesian axis
        """
        # A subplot with two additional axis, "xzero" and "yzero"
        # corresponding to the cartesian axis
        ax = SubplotZero(self.fig, 1, 1, 1)
        self.fig.add_subplot(ax)
        
        # make xzero axis (horizontal axis line through y=0) visible.
        for axis in ["xzero","yzero"]:
            ax.axis[axis].set_visible(True)
        # make the other axis (left, bottom, top, right) invisible
        for n in ["left", "right", "bottom", "top"]:
            ax.axis[n].set_visible(False)
            
        # Plot limits
        plt.xlim(self.xlim)
        plt.ylim(self.ylim)

        # Draw the arrows
        self.__arrow__(self.xlim[1], 0, 0.01, 0, 0.3, 0.2) # x-axis arrow
        self.__arrow__(0, self.ylim[1], 0, 0.01, 0.2, 0.3) # y-axis arrow
        
        
    def scale_arrows(self):
        """ Make the arrows look good regardless of the axis limits """
        xrange = self.xlim[1] - self.xlim[0]
        yrange = self.ylim[1] - self.ylim[0]
        
        self.head_width  = min(xrange/30, 0.25)
        self.head_length = min(yrange/30, 0.3)
        
        
    def draw(self, image=None):
        self.scale_arrows()
        self.fig = plt.figure(figsize=self.figsize)
        # First draw the axis
        self.__drawAxis__()
        # Plot each point
        for point in self.points:
            point.draw()
        # Save the image?
        if image:
            plt.savefig(image)
        plt.ylabel('(m)')
        plt.xlabel('(m)')  
        plt.show()
        
    def addPoints(self, points):
        for p in points:
            self.addPoint(p)
            
    def addPoint(self, p):
        self.points.append(p)