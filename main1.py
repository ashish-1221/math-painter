import numpy as np
from PIL import Image
import os

class Canvas:
    """
    Creates a canvas where all shapes are drawn
    """
    def __init__(self,height,width,color) -> None:
        self.color = color
        self.height = height
        self.width = width
    
        # create a 3D numpy array of zeros
        self.data = np.zeros((self.height,self.width,3),dtype=np.uint8)
        # Change the [0,0,0] with color values
        self.data[:] = self.color
    
    def make(self,imagepath):
        """
        converts the current array into an image file
        Args:
            imagepath (string): path where mage file is going to be stored
        """
        img = Image.fromarray(self.data,"RGB")
        img.save(imagepath)

class Rectangle:
    """
    Creates an instance of type Rectangle
    """
    def __init__(self,x,y,width,height,color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self,canvas):
        canvas.data[self.x:self.x+self.width,self.y:self.y + self.height] = self.color
        

class Square:
    """
    Creates an instance of type square
    """
    def __init__(self,x,y,side,color) -> None:
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self,canvas):
        canvas.data[self.x:self.x+self.side,self.y:self.y + self.side] = self.color

canvas = Canvas(height = 100, width= 200, color=(255,255,255))
rec1 = Rectangle(x=20,y=30,width=30,height=20,color=(255,230,100))
rec1.draw(canvas)
canvas.make('canvas.png')
         
