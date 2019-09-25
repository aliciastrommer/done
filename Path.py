import json

# Loads a path from a file and converts it into a list of coordinates
class Path:

    def __init__(self, file_name):
        with open(file_name) as path_file:
            data = json.load(path_file)
        self.path = data
        
    def getPath(self):
        coorList = []
        for i in range (len(self.path)):
            coorList.append(self.path[i]['Pose']['Position'])
        coorList.reverse()
        return coorList        
