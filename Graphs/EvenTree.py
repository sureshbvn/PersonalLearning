__author__ = 'subvn'
import sys
class vertex:
    def __init__(self,id):
        self.__id=id
        self.adjacent={}
        self.distance=sys.maxint
        self.visited=False
        self.color='white'
        self.previous=None
        self.indegree=0
        self.outdegree=0
        self.childrencount=1
    def addneighbour(self,neighbour,weight=0):
        self.adjacent[neighbour]=weight
    def setprveious(self,previous):
        self.previous=previous
    def setweight(self,id,weight=0):
        self.adjacent[id]=weight
    def getprevious(self):
        return self.previous
    def getconnections(self):
        return list(self.adjacent.keys())
    def getweight(self,neig):
        return self.adjacent[neig]
    def getVertexid(self):
        return self.__id
    def setVisited(self):
        self.visited=True
    def setDistance(self,distance):
        self.distance=distance
    def getDistance(self):
        return self.distance
    def setPrevious(self,previous):
        self.previous=previous
    def getPrevious(self):
        return self.previous
    def setColor(self,color):
        self.color=color
    def getColor(self):
        return self.color
    def setchildCount(self,count):
        self.childrencount=count
    def incrementChildCount(self,count):
        self.childrencount+=1
    def getchildCount(self):
        return self.childrencount

    def setIndegree(self,deg):
        self.indegree=deg
    def getIndegree(self):
        return self.indegree
    def setOutdegree(self,deg):
        self.outdegree=deg
    def getOutdegree(self):
        return self.outdegree
    def __str__(self):
       return str(self.__id)+" Adjacent:"+str([x.__id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.__numvertices=0
        self.__vertdict={}
    def __iter__(self):
        return iter(self.__vertdict.values())
    def addVertex(self,vertex_id):
        v=vertex(vertex_id)
        self.__numvertices=self.__numvertices+1
        self.__vertdict[vertex_id]=v
    def addEdge(self,frm,to,cost=0):
        if frm not in self.__vertdict:
            self.addVertex(frm)
        if to not in self.__vertdict:
            self.addVertex(to)
        self.__vertdict[frm].addneighbour(self.__vertdict[to],cost)
        self.__vertdict[to].addneighbour(self.__vertdict[frm],cost)
        self.__vertdict[frm].setOutdegree(self.__vertdict[frm].getOutdegree()+1)
    def printvertices(self):
        for v in self.__vertdict.values():
            print v
    def getVertex(self,n):
        if n in self.__vertdict:
            return self.__vertdict[n]
        else:
            return None
    def getedges(self):
        edges=[]
        for v in self:
            for w in v.getconnections():
                vid=v.getVertexid()

                wid=w.getVertexid()

                edges.append((vid,wid,v.getweight(w)))
        return edges
    def getIndegrees(self):
        indegree_list=[]
        for v in self:
            indegree_list.append((v.getIndegree()))
        return indegree_list
    def getVertices(self):
        verticeslist=[]
        for v in self.__vertdict.values():
            verticeslist.append((v.getVertexid))
        return verticeslist



def BFSTraversal(graph,s):
    start=graph.getVertex(s)
    start.setDistance(0)
    start.setPrevious(None)
    finallist=[]
    queue=[]
    queue.insert(0,start)
    while(len(queue)>0):
        currentvert=queue.pop()
        finallist.append(currentvert)
        #print currentvert.getVertexid()
        for nbr in currentvert.getconnections():
            if(nbr.getColor() =='white'):
                nbr.setColor('gray')
                nbr.setDistance(currentvert.getDistance()+1)
                nbr.setPrevious(currentvert)
                queue.append(nbr)
            currentvert.setColor('black')


    return finallist

if __name__ == '__main__':

    N,M=raw_input().split()
    N,M=int(N),int(M)

    G=Graph()
    for i in range(0,M):
        u,v=raw_input().split()
        u,v=int(u),int(v)
        G.addEdge(u,v,0)

    bfs_list=BFSTraversal(G,1)

    for v in reversed(bfs_list):
        vertex=v.getPrevious()
        if vertex!=None:
             vertex.setchildCount(vertex.getchildCount()+v.getchildCount())
    count=0
    for v in G:
        if v.getchildCount()>0:
            if v.getchildCount()%2==0:
                count+=1
    print count-1










