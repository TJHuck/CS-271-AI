import cv2
import networkx as nx #found on internet as recommended graph library
import math

## distance per pixel - see distanceMeasurement.py
yardPerPixel = 0.667

## load image
img = cv2.imread("collegemap.png")


## manually add to nodes. "P" for sidewalk intersections that arent buildings
nodes = [["Wesley Hall",400,200],["Goodrich Chapel",400,440],["Observatory Crosswalk",400,560],
         ["Observatory",380,580],["Library Accessibility Ramp",340,635],["Stockwell/Mudd Library",280,635],
         ["Olin Hall",275,720],["Chapel Corner Crosswalk",400,535],["Wesley Chapel Side Crosswalk",400,285],
         ["Quad Streetlamp Intersection",400,640],["Wesley Hall Side Crosswalk",400,245],
         ["Kresge Gymnasium", 180, 680],["Tau Kappa Epsilon",750,850],
         ["Delta Sigma Phi",645,855],["Sigma Chi",650,920],["Ferguson Circular Intersection",417,730],
         ["The Rock",483,640],["Vulgamore Hall",483,600],["Fiske House Corner Crosswalk",445,535],
         ["Quad Fiske House Crosswalk",443,555],["Vulgamore Robinson Front Entrance Intersection",565,635],
         ["Robinson Kellog Front Entrance Intersection",565,725],["Alpha Tau Omega",745,920],["Sigma Nu",785,920],
         ["Delta Tau Delta",790,855],["Fraternity Alleyway",780,885],["Robinson Hall",565,680],["Kellog Center",550,755],["Ferguson",417,760],
         ["Library Sidewalk",240,640],["Center Of Quad",315,675],["Robinson Hall Back Entrance",483,685],["Science Complex Crosswalk",605,285],
         ["Sidewalk",605,440],["Science Complex",650,430],["Crosswalk",610,535]]





##comment out when all nodes and edges added
########################################
for i,node in enumerate(nodes):
    cv2.circle(img,(node[1],node[2]),6,(0,0,255),-1)
    cv2.putText(img,str(i), (node[1]+5,node[2]+5),1, 1.5, 255,2)
########################################


    
## manually add to edges. [index of point1 in nodes, index of point2 in nodes]
edges = [[0,10],[10,8],[8,1],[1,7],[2,7],[2,3],[3,4],[4,5],[7,18],[2,19],[18,19],[19,17],[17,16],[16,9],[9,2],[9,4],
         [4,30],[6,11],[29,5],[29,6],[29,11],[9,15],[15,28],[15,6],[15,21],[28,27],[30,6],[29,30],[15,30],[16,31],
         [31,15],[16,20],[20,26],[26,21],[21,27],[32,8],[32,33],[1,33],[33,34],[35,33]]



for edge in edges:
    point1 = (nodes[edge[0]][1],nodes[edge[0]][2])
    point2 = (nodes[edge[1]][1],nodes[edge[1]][2])
    cv2.line(img,point1,point2,(255,0,0),3) ## comment this line out when all nodes and edges are added
    (x1,y1)=point1
    (x2,y2)=point2
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    edge.append(dist*yardPerPixel)



##comment out when all nodes and edges added
########################################
## show image
resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
########################################




"""
## make graph
graph = nx.Graph()
img = cv2.imread("collegemap.png")
## add nodes from previous work to graph
for i,node in enumerate(nodes):
    graph.add_node(i,pos=(node[1],node[2]),name=node[0])

## add edges from previous work to graph
for edge in edges:
    graph.add_edge(edge[0],edge[1],weight=edge[2])




## begin user input
for node in graph.nodes:
    print(str(node)+": "+graph.nodes[node]['name'])
print("To select a location input the number before. Example: 0:Wesley Hall. ENTER 0")
start=int(input("Please enter your starting location number: "))
end=int(input("Please enter your final location number: "))

## A star algorithm
def heuristic(a,b):
    (x1,y1) = graph.nodes[a]["pos"]
    (x2,y2) = graph.nodes[b]["pos"]
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist*yardPerPixel

def astar(graph,start,end):
    ## looked up breath first search implementation from internet
    ## https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/
    nodes = graph.nodes
    if start ==end:
        return [start]

    ## we need [node,weight] where weight is weight up to this point. NOT HEURISTIC
    nodeQueue = [[start,0]]
    ## weight + heuristic => weight=0 for start so just heuristic
    weightQueue = [heuristic(start,end)]
    pathQueue = [[start]]
    visited = [False]*len(nodes)
    while nodeQueue:
        ## get best node
        bestIndex = weightQueue.index(min(weightQueue))
        node = nodeQueue.pop(bestIndex)
        weight = node[1]
        node = node[0]
        weightQueue.pop(bestIndex)
        path = pathQueue.pop(bestIndex)
        visited[node]=True
        if node == end:
            return path
        for children in graph.neighbors(node):
            if visited[children]:
                continue
            w = weight+graph[node][children]["weight"]
            nodeQueue.append([children,w])
            weightQueue.append(w+heuristic(node,children))
            pathPlus = path+[children]
            pathQueue.append(pathPlus)
            
        
        
        
    

## we probably cant use the built in astar but idk
##finalPath = nx.astar_path(graph,start,end,heuristic=heuristic,weight="weight")
finalPath = astar(graph,start,end)

cv2.circle(img,(nodes[finalPath[0]][1],nodes[finalPath[0]][2]),6,(0,0,255),-1)
for p in range(1,len(finalPath)):
    point1 = (nodes[finalPath[p-1]][1],nodes[finalPath[p-1]][2])
    point2 = (nodes[finalPath[p]][1],nodes[finalPath[p]][2])
    cv2.line(img,point1,point2,(255,0,0),3)
    cv2.circle(img,(nodes[finalPath[p]][1],nodes[finalPath[p]][2]),6,(0,0,255),-1)


resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
    
    
