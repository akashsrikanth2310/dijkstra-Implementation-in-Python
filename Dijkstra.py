#DO NOT CHANGE ANY EXISTING CODE IN THIS FILE
import sys
from collections import defaultdict as dd

class Heap():
    def __init__(self):
        self.location = []
        self.datastruct = []
        self.size = 0

    def createNode(self, vertex, distance):
        locnode = [vertex, distance]
        return locnode

    def replaceNode(self, one, two):
        self.datastruct[one], self.datastruct[two] = self.datastruct[two], self.datastruct[one]

    def heapification(self, y):
        least = y
        r_right = 2*y + 2
        l_left = 2*y + 1

        if l_left < self.size and self.datastruct[l_left][1] < self.datastruct[least][1]:
            least = l_left

        if r_right < self.size and self.datastruct[r_right][1] < self.datastruct[least][1]:
            least = r_right

        if least != y:
            self.location[self.datastruct[y][0]] = least
            self.location[self.datastruct[least][0]] = y
            self.replaceNode(least, y)
            self.heapification(least)

    def figured(self):
        if self.size == 0:
            return

        least = self.datastruct[0]
        lastNode = self.datastruct[self.size - 1]
        self.datastruct[0] = lastNode
        self.location[lastNode[0]] = 0
        self.location[least[0]] = self.size - 1
        self.size = self.size - 1
        self.heapification(0)

        return least

    def decreaseKey(self, vertex, distance):
        slno = self.location[vertex]
        self.datastruct[slno][1] = distance

        while slno > 0 and self.datastruct[slno][1] < self.datastruct[(slno-1)// 2][1]:
            self.location[ self.datastruct[(slno-1)//2][0] ] = slno
            self.location[ self.datastruct[slno][0] ] = (slno-1)//2
            self.replaceNode(slno, (slno-1)//2)

            slno = (slno - 1)//2

    def insideHeap(self, vertex):
        if self.location[vertex] < self.size:
            return True
        return False




class Dijkstra():

    def Dijkstra_alg(self, n, e, mat, s):
         #Write your code here to calculate shortest paths and usp values from source to all vertices
		 #This method will have four inputs (Please see testcase file)
		 #This method should return one two dimensional datastruct as output (Please see testcase file
         adjacentmat = dd(list)
         for link in mat:
             adjacentmat[link[0]-1].insert(0,[link[1] - 1, link[2]])
             adjacentmat[link[1]-1].insert(0,[link[0] - 1, link[2]])
         print(adjacentmat)
         distance = []
         pair = Heap()

         for vertex in range(n):
             distance.append([sys.maxsize, 1])
             pair.datastruct.append(pair.createNode(vertex, distance[vertex][0]))
             pair.location.append(vertex)

         pair.location[s-1] = s-1
         distance[s-1][0] = 0
         pair.decreaseKey(s-1, distance[s-1][0])
         pair.size = n

         while pair.size != 0:
             createdHeapNode = pair.figured()
             united = createdHeapNode[0]
             for lV in adjacentmat[united]:
                 vertex = lV[0]
                 print(lV)
                 print(pair.insideHeap(vertex))
                 if pair.insideHeap(vertex) and distance[united][0] != sys.maxsize:
                     if (lV[1] + distance[united][0] < distance[vertex][0]):
                         distance[vertex][0] = lV[1] + distance[united][0]
                         distance[vertex][1] = distance[united][1]
                         pair.decreaseKey(vertex, distance[vertex][0])
                     elif (lV[1] + distance[united][0] == distance[vertex][0]):
                         distance[vertex][1] = 0

         return distance
