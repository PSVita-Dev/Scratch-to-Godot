import json
import sys
import names
import random
from cairosvg import svg2png

class ScratchParser:
    def __init__(self, path = "project.json"):
        try:
            self.project = json.load(open(path, "r"))
        except Exception as ex:
            print("Could not read project ("+str(ex)+")")
            sys.exit(-1)
        
        #"name" contains the actual name of the specifc costume
        #"x" contains the actual x coordinate of the sprite in the window (center adjusted)
        #"y" contains the actual y coordinate of the sprite in the window (center adjusted)
        #"defaultCostume" contains index of the initial costume
        #"layer" contains the drawing layer of the sprite (e.g. 0 first, 10 last)
        #"costumes" contains all costumes needed for this sprite
        self.parsedSprites = []
        
        #"name" contains the actual name of the specifc costume
        #"filename" contains the name of the image (with extension)
        #"centerX" contains the x center (starting at x 0)
        #"centerY" contains the y center (starting at y 0)
        #"spriteIndex" contains the associated sprite index (one sprite can have multiple costumes).
        self.parsedCostumes = []
        
        #"name" contains the actual name of the specifc costume
        #"filename" contains the name of the image (with extension)
        self.parsedStages = []
    
    #Maybe I could "merge" those two functions into one and save some time there ~ Done
    def parseSprites(self):
        temp_costumes = [] #basically the same as parsedCostumes, but temporary for each sprite
        spriteidx = -1
        for target in self.project["targets"]: #Go through all objects
            if target["isStage"] == False:
                temp_costumes = [] #Reset it
                spriteidx += 1 #Count the sprite that was associated with it
                for costume in target["costumes"]:
                    temp_costumes.append({"name": costume["name"],
                                            "filename": costume["assetId"] + ".png", 
                                            "centerX": costume["rotationCenterX"], 
                                            "centerY": costume["rotationCenterY"], 
                                            "spriteIndex": spriteidx})
                    self.parsedCostumes.append(temp_costumes[-1])
                    
                self.parsedSprites.append({"name": target["name"],
                                            "x": int(240+target["x"]-temp_costumes[target["currentCostume"]]["centerX"]), #Calculate "real" x coordinate
                                            "y": int(180-(target["y"]+temp_costumes[target["currentCostume"]]["centerY"])), #Calculate "real" y coordinate
                                            "defaultCostume": target["currentCostume"], 
                                            "layer": target["layerOrder"],
                                            "cotumes": temp_costumes})
                
    def parseStages(self):
        for target in self.project["targets"]: #Go through all objects
            if target["isStage"] == True:
                for stage in target["costumes"]:
                    self.parsedStages.append({"name": stage["name"],
                                                "filename": stage["assetId"] + ".png"})
        
                    
    
if __name__ == "__main__":
    parser = ScratchParser()
    # parser.parseCostumes()
    parser.parseSprites()
    parser.parseStages()
    print(parser.parsedStages)
