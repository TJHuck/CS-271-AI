import cv2
import networkx as nx #found on internet as recommended graph library
import math

## distance per pixel - see distanceMeasurement.py
yardPerPixel = 0.667

## load image
img = cv2.imread("collegemap.png")


## manually add to nodes. "P" for sidewalk intersections that arent buildings
nodes = [["Wesley Hall",400,200],["Goodrich Chapel",400,440],["P1",400,560],
         ["Observatory",380,580],["P2",340,635],["Stockwell/Mudd Library",280,635],
         ["Olin Hall",275,720],["P3",400,535],["P4",400,285],["P5",400,640],
         ["Kresge Gymnasium", 180, 680],["Tau Kappa Epsilon",750,850],
         ["Delta Sigma Phi",645,855],["Sigma Chi",650,920],["P6",417,730],
         ["P7",483,640],["P8",483,600],["P9",445,535],["P10",443,555],["P11",565,635],
         ["P12",565,725]]

for node in nodes:
    cv2.circle(img,(node[1],node[2]),6,(0,0,255),-1)

## manually add to edges. [index of point1 in nodes, index of point2 in nodes]
edges = [[0,8]]
for edge in edges:
    point1 = (nodes[edge[0]][1],nodes[edge[0]][2])
    point2 = (nodes[edge[1]][1],nodes[edge[1]][2])
    cv2.line(img,point1,point2,(255,0,0),3)
    ## calculate distance
    (x1,y1)=point1
    (x2,y2)=point2
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    edge.append(dist*yardPerPixel)
    
print(edges)
## show image
cv2.imshow('Map', img) ## <--- This is the way Nathan had to display the original image, below is just the way I'm scaling it to fit my screen
##resized = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
##cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

## make graph
graph = nx.Graph()

## add nodes from previous work to graph
for i,node in enumerate(nodes):
    graph.add_node(i,pos=(node[1],node[2]),name=node[0])

## add edges from previous work to graph
for edge in edges:
    graph.add_edge(edge[0],edge[1],weight=edge[2])
print(graph)