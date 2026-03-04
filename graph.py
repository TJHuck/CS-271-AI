#### MADE BY: TERRY HUCK, NATHAN PENFIELD, AND PACEY MINK

import cv2
import networkx as nx #found on internet as recommended graph library
import math

## distance per pixel - see distanceMeasurement.py
yardPerPixel = 0.667

## load image
img = cv2.imread("collegemap.png")

### Defined Functions ################################################################
def find_department(dept_name):
    for node in graph.nodes:
        if dept_name.lower() in [d.lower() for d in graph.nodes[node]["departments"]]:
            return node
    return None

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
######################################################################################

## manually add to nodes. "P" for sidewalk intersections that arent buildings
nodes = [["Wesley Hall",400,200,["Wesley Hall"]],["Goodrich Chapel",400,440,["Music Dept","Goodrich Chapel"]],["Observatory Crosswalk",400,560],
        ["Observatory",380,580,["Observatory"]],["Library Accessibility Ramp",340,635],["Stockwell/Mudd Library",280,635,["Cutler Center","Writing Center","Stockwell Library","Mudd Library"]],["Wesley Hall Sidewalk Intersection",400,240],
        ["Olin Hall",275,720,["Communications Dept", "Psychological Science Dept","Olin Hall"]],["Chapel Corner Crosswalk",400,535],
        ["Wesley Chapel Side Crosswalk",400,285],["Quad Streetlamp Intersection",400,640],["Wesley Hall Side Crosswalk",400,245],
        ["Kresge Gymnasium", 180, 680,["Kresge Gymnasium"]],["Tau Kappa Epsilon",750,850,["Tau Kappa Epsilon"]],["Delta Sigma Phi",645,855,["Delta Sigma Phi"]],["Sigma Chi",650,920,["Sigma Chi"]],["Ferguson Circular Intersection",417,730],
        ["The Rock",483,640,["The Rock"]],["Vulgamore Hall",483,600,["Philosophy Dept","Language and Culture Dept", "Political Science Dept", "Religious Studies Dept","Vulgamore Hall"]],["Fiske House Corner Crosswalk",445,535],
        ["Quad Fiske House Crosswalk",443,555],["Vulgamore Robinson Front Entrance Intersection",565,635],["Robinson Kellog Front Entrance Intersection",565,725],["Alpha Tau Omega",745,920,["Alpha Tau Omega"]],["Sigma Nu",785,920,["Sigma Nu"]],
        ["Delta Tau Delta",790,855,["Delta Tau Delta"]],["Fraternity Alleyway",780,885],["Robinson Hall",565,680,["Anthropology and Sociology Dept","Robinson Hall"]],["Kellogg Center",550,755,["Bookstore","Qdoba",
        "Office of Fraternity and Sorority Life", "Campus Post Office","Kellogg Center"]],["Ferguson",417,760,["IT Helpesk", "Registrar's Office","Academic Affairs Office","Financial Aid Office", "Title IX","Ferguson"]],
        ["Library Sidewalk",240,640],["Center Of Quad",315,675],["Robinson Hall Back Entrance",483,685],["Science Complex Crosswalk",605,285],
        ["Sidewalk",605,440],["Science Complex",650,430,["Math and Computer Science Dept", "Science Complex Front Office", "Norris","Palenske","Putnam","Kresge","Astronomy and Physics Department","Chemistry","Biology",
        "Earth and Environment Dept", "Kinesiology Dept","Science Complex"]],["Bobbit Visual Arts Corner Crosswalk",610,535],["Robinson Crosswalk", 605,680],["Baldwin Crosswalk", 635,680],
        ["Baldwin Front ENtrance", 665,675],["Vulgamore Front Entrance Circular Intersection",585,600],["Vulgamore Front Entrance Corner Crosswalk",610,556],
        ["Bobbit Visual Arts Center",530,535,["Art and Art History Dept","Bobbit Visual Arts Center"]],["Vulgarmore Side Crosswalk",530,557],["Seaton Hall Front Corner Crosswalk",635,556],
        ["Seaton Hall Front Entrance",715,556],["Mitchell Towers Circular Intersection",865,675],["Mitchell Towers Front Entrance", 925,675],
        ["Whitehouse Side Entrance",710,780,["Whitehouse Hall"]],["Whitehouse Side Entrance, Sidewalk Entrance",710,810],["Whitehouse Corner Sidewalk",635,810],
        ["Fraternity Row Corner Crosswalk",635,830],["Sigma Chi Corner Crosswalk",635,950],["Athletics Complex Crosswalk",635,1025],["Tennis Courts",710,1200],
        ["Athletics Complex Crosswalk Fork",710,1100],["Serra Fitness Center Parking",840,1110],["Serra Fitness Center Entrance",780,1150,["Field House","Theatre","Theatre Dept","Serra Fitness Center"]],
        ["Tennis Court Corner",710,1260],["Alumni Field",800,1260,["Football Field","Track and Field","Alumni Field"]],["Athletics Fields Fork",1000,1260],
        ["LAX Field",1110,1220,["Lacrosse Field"]],["Soccer Field",1110,1300,["Soccer Field"]],["Softball Field",1280,1300,["Softball Field"]],["Baseball Field",1280,1220,["Baseball Field"]],
        ["KC Parking Lot Sidewalk Intersection",540,835],["Front Frat Row Crosswalk",600,835],["KC Sidewalk Intersection Crosswalk",600,800],
        ["KC Intersection #2",525,795],["Mae Apartment Entrance 1",910,945,["Mae Apartments 1"]],["Mae Apartment Entrance 2",945,945,["Mae Apartments 2"]],["Mae Apartment Entrance 3",1000,945,["Mae Apartments 3"]],
        ["Whitehouse Back Corner Crosswalk",785,810],["Fraternity Alley Exit",780,840]]




##comment out when all nodes and edges added
"""
######################################## ALSO PURELY FOR TESTING AND WORKING PURPOSES. NOT NEEDED IN FINAL PRODUCT
for i,node in enumerate(nodes):
    cv2.circle(img,(node[1],node[2]),6,(0,0,255),-1)
    cv2.putText(img,str(i), (node[1]+5,node[2]+5),1, 1.5, 255,2)
########################################
"""


    
## manually add to edges. [index of point1 in nodes, index of point2 in nodes]
edges = [[0,10],[10,8],[8,1],[1,7],[2,7],[2,3],[3,4],[4,5],[7,18],[2,19],[18,19],[19,17],[17,16],[16,9],[9,2],[9,4],
         [4,30],[6,11],[29,5],[29,6],[29,11],[9,15],[15,28],[15,6],[15,21],[28,27],[30,6],[29,30],[15,30],[16,31],
         [31,15],[16,20],[20,26],[26,21],[21,27],[32,8],[32,33],[1,33],[33,34],[35,33],[26,36],[36,37],[37,38],[20,39],
         [39,40],[40,35],[18,41],[19,42],[41,35],[42,40],[41,42],[42,39],[40,43],[43,44],[38,45],[45,46],[28,67],[21,66],
         [27,66],[67,66],[64,67],[64,65],[65,66],[66,49],[65,50],[49,50],[49,48],[48,47],[48,71],[50,13],[50,14],[50,51],
         [51,14],[51,13],[51,52],[51,68],[68,69],[69,70],[52,54],[54,55],[54,56],[54,53],[53,57],[57,58],[58,59],[59,60],
         [59,61],[61,62],[62,63],[72,50],[22,25],[23,25],[25,72],[12,50],[24,72]]


## Creates Edges
for edge in edges:
    point1 = (nodes[edge[0]][1],nodes[edge[0]][2])
    point2 = (nodes[edge[1]][1],nodes[edge[1]][2])
    ##cv2.line(img,point1,point2,(255,0,0),3) ## comment this line out when all nodes and edges are added
    (x1,y1)=point1
    (x2,y2)=point2
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    edge.append(dist*yardPerPixel)


"""
##comment out when all nodes and edges added THIS SECTION IS PURELY FOR TESTING AND WORKING PURPOSES. IT IS NOT NEEDED IN THE FINAL PRODUCT
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
    departments = node[3] if len(node) > 3 else []
    graph.add_node(i,
                   pos=(node[1],node[2]),
                   name=node[0],
                   departments=departments) 
## add edges from previous work to graph
for edge in edges:
    graph.add_edge(edge[0],edge[1],weight=edge[2])



## begin user input
for node in graph.nodes:
    print(str(node)+": "+graph.nodes[node]['name'])
print("To select a location input the number before. Example: 0:Wesley Hall. ENTER 0")
start=int(input("Please enter your starting location number: "))

choice = input("Search by (1) Building Number or (2) Department? ")

if choice == "1":
    end=int(input("Please enter destination number:"))
    
elif choice == "2":
    dept_name = input("Please enter department name: ")
    end = find_department(dept_name)
    
    if end is None:
        print("Department not found.")
        exit()

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