import sys
import math
import numpy
import graphmaker
import graphviz
import matplotlib
from collections import deque

class Searcher:
    global graph, search
    graph = []
    search = ""

    def __init__(self, file, search, h):
        self.file = file
        self.search = search
        with open(file) as f:
            for line in f:
                graph.append(tuple(line.rstrip().split()))  # rstrip() removes line breaks
        print(graph)
        if search == "BREADTH":
            self.search = "BREADTH"
        elif search == "DEPTH":
            self.search = "DEPTH"
        elif search == "BEST":
            self.search = "BEST"
        else:
            self.search = "A*"

        self.h = None
    def getG(self):
        print()
        self = graph
        return self

    def getL(self):
        print()
        self = search
        return self





class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return self.val




class SearchNode:
    def __init__(self, label):
        self.nodes = Searcher.getG(self)
        self.label = Searcher.getL(self)
        print("Here is init of SearchNode --> self.nodes")
        print(self.nodes)
        print()

    def setStartGoal(self, start, end):
        self.start = start
        self.end = end
        print("Start Node Set To : ", start)
        print("End Node Set To : ", end)

    def showOpen(self):
        return

    def bfs(self, start, end):
        self.graph = Searcher.getG(self)
        if not self.nodes:
            return []
        visited, queue, result = set([start]), deque([start]), []
        while queue:
            try:
                queue = []
                # push the first path into the queue
                queue.append([start])
                while queue:
                    # get the first path from the queue
                    path = queue.pop(0)
                    # get the last node from the path
                    node = path[-1]
                    # path found
                    if node == end:
                        return path
                    # enumerate all adjacent nodes, construct a
                    # new path and push it into the queue
                    for i in graph[path]:
                        if visited[i] == False:
                            queue.append(i)
                            visited[i] = True
            except ValueError:
                pass
        print(queue)
        return queue






if __name__ == '__main__':
    s = Searcher(file='tenNode.txt', search='BREADTH', h=None)
    g = Searcher.getG(self=Searcher)
    sn = SearchNode(label=s)
    sn.setStartGoal("A", "B")
    sn.bfs(start="C", end="D")


