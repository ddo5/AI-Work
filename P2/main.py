import sys
import math
import numpy
import graphmaker
import graphviz
import matplotlib


class Searcher:
    def __init__(self, file, search, h):
        self.file = self.loadfile(file)
        if search == "BREADTH":
            self.search = "BREADTH"
        elif search == "DEPTH":
            self.search = "DEPTH"
        elif search == "BEST":
            self.search = "BEST"
        else:
            self.search = "A*"

        self.h = None

    def loadfile(self, fname):
        map = []
        with open(fname) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            for line in content:
                map.append(line.split())
        print("Content as List of Lists: \n")
        print(map)
        '''
        print()
        print()
        print("Content as Dictionary: \n")
        res = dict()
        for sub in map:
            res[tuple(sub[:2])] = tuple(sub[2:])
        print(res)
        return res
        '''
        return map


graph = Searcher.loadfile


class SearchNode:
    global graph

    def __init__(self, label, value):
        self.label = None
        self.value = 0
        print(self.label)
        print(self.value)

    def setStartGoal(self, start, end):
        self.start = start.make
        self.end = end
        print("Start Node Set To : ", start)
        print("End Node Set To : ", end)

    # def showOpen(self):
    # print tuple of lable and value

    def breadth_first_search(self, graph):
        graph = graph
        print(graph)



'''
Function: loadfile()
The foal here is to take in ANY file and convert it to a list of lists.
After this i then parse the values to generate a dictionary. 

EX)
[["('C',", "'I',", '67,', '[138,', '1],', '[131,', '80])']

turns into

{("('C',", "'I',"): ('67,', '[138,', '1],', '[131,', '80])')

def loadfile(fname):
    map = []
    with open (fname) as f:
        content=f.readlines()
        content=[x.strip() for x in content]
        for line in content:
            map.append(line.split())
    print("Content as List of Lists: \n")
    print(map)
    print()
    print()
    print("Content as Dictionary: \n")
    res = dict()
    for sub in map:
        res[tuple(sub[:2])] = tuple(sub[2:])
    print(res)
    return res
'''
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = Searcher(file='tenNode.txt', search='BREADTH', h=0)
    sn = SearchNode(label="BREADTH", value=0)
    sn.setStartGoal("A", "B")
    sn.breadth_first_search(graph)
