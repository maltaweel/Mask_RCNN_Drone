'''
Created on Jul 20, 2021

@author: maltaweel
'''

from gui.gui import Gui



class TrainGUI (Gui):
    
    def makeTrainingButtons(self):
        
        widgets=['Training Library','Weight File']
        self.makeWidgetPushButton(widgets)
        
        