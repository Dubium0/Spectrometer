# -*- coding: utf-8 -*-
"""

Created on Tue Feb  1 12:42:35 2022

@author: LENOPC

"""

import cv2 as cv

import numpy as np

class Converter:
    def __init__(self):
        self.colors = {"red": 0,"orange": 0,"yellow": 0,"green": 0,"cyan": 0,"blue": 0,"violet": 0,"magenta": 0}

        self.colorSet = set()

    def bgr2hsv(self,b,g,r):
        """
        This converts given BGR values to HSV format(0-360,0-100,0-100)
    
        Parameters
        ----------
        b : blue value between 0-255
        g : green value between 0-255
        r : red value between 0-255
    
        Returns
        -------
        H : hue value between 0-360
        S : saturation value between 0-100
        V : value value between 0-100
    
        """
        R  = r/255
        G =  g /255
        B =  b/255
        Cmax = max(R,G,B)
        Cmin = min(R,G,B)
        
        delta = Cmax - Cmin
        
        # Hue calculation
        
        if delta == 0:
            H = 0
        elif Cmax == R:
            #degre
            H = 60 * (((G-B)/delta) % 6)
        elif Cmax == G:
            H = 60 * (((B-R)/delta) +2)
        elif Cmax == B:
            H = 60 * (((R-G)/delta) +4)
            
        
        # Saturation calculation
        
        if Cmax ==0:
            S = 0
        else:
            S = delta / Cmax
            
        # Value calculation
        
        V =  Cmax
        
        S*=100
        V*=100
        return H,S,V
    
    
    def hueDetector(self,H):
        if H >=345:
            self.colors["red"] +=1
        elif H >=0 and H <30:
            self.colors["red"] +=1
        elif H >=30 and H <45:
            self.colors["orange"] +=1
        elif H >=45 and H <90:
            self.colors["yellow"] +=1
        elif H >=90 and H <150:
            self.colors["green"] +=1
        elif H >=150 and H <225:
            self.colors["cyan"] +=1
        elif H >=225 and H <270:
            self.colors["blue"] +=1
        elif H >=270 and H <285:
            self.colors["violet"] +=1
        elif H >=285 and H <345:
            self.colors["magenta"] +=1
        else:
            print("wattaFak")
            
    def convertAllImage(self,image):
        x,y = 0,0

        while x < len(image):
            B  = image[x][y][0]
            G  = image[x][y][1]
            R  = image[x][y][2]
            H,S,V = self.bgr2hsv(B,G,R)
            if S > 20 and V>20:
                self.hueDetector(H)
                self.colorSet.add((H,S,V))
            if y < image.shape[1]-1:
                y+=1
            else:
                y=0
                x+=1
            

class Spektrometer:
    #add 
    """
        make graph in ColorSpectrumCreator
        
    
    """
    def __init__(self,testName):
        self.test = cv.imread(testName)
        self.converter = Converter()
        self.colors = None
        self.colorSet = None
        
    def ColorSpectrumCreator(self): # take colors at particular ranges
        
        self.converter.convertAllImage(self.test)
        self.colors = self.converter.colors
        self.colorSet= self.converter.colorSet
        
            
    def showImage(self): # show test image
        cv.imshow("test",self.test)
        
        cv.waitKey(0)
        
        cv.destroyAllWindows()
        
    
    

"""

obj = Spektrometer("hidrojen spektrum.png")

obj.ColorSpectrumCreator()

print(obj.colors)

print(obj.colorSet)


"""


























