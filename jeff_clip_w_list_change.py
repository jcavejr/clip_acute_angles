import mock
import math


newPointList = []
def clipAngle(vertex0, vertex1, vertex2, vertexlist):
    SHORTEST = findShortestDistance(vertexlist[vertex1], vertexlist)
    #Vertex1 is the acute angle, vertex1 and vertex2 are the surrounding vertices.
    #Discover the x y coords of the new non-acute vertices.  This is done courtesy of Andre's trig knowledge
    #First, do some data collecting.  Collect the x y points to make vectors.
    p0X = vertexlist[vertex0][0]
    p0Y = vertexlist[vertex0][1]
    p1X = vertexlist[vertex1][0]
    p1Y = vertexlist[vertex1][1]
    p2X = vertexlist[vertex2][0]
    p2Y = vertexlist[vertex2][1]
    #print(p0X, p0Y, p1X, p1Y, p2X, p2Y)

    #v0 is the vector from p0 to p1. v2 is the vector from p1 to p2.
    v0X = p1X - p0X
    v0Y = p1Y - p0Y
    v2X = p1X - p2X
    v2Y = p1Y - p2Y
    #print(v0X, v0Y, v2X, v2Y)

    #Find the length of each vector.  L1 is 3/4 the length of the shortest length
    lengthV0 = math.sqrt(v0X**2+v0Y**2)
    lengthV2 = math.sqrt(v2X**2+v2Y**2)
    L1 = SHORTEST *.75
    #print(lengthV0, lengthV2, L1)

    #Multiply each vertex by ((lengthV0 - L1)/lengthV0)
    v0XPrime = v0X*((lengthV0 - L1)/lengthV0)
    v0YPrime = v0Y*((lengthV0 - L1)/lengthV0)
    v2XPrime = v2X*((lengthV2 - L1)/lengthV2)
    v2YPrime = v2Y*((lengthV2 - L1)/lengthV2)
    #print(v0XPrime, v0YPrime, v2XPrime, v2YPrime)

    #Now V0Prime and add p0.
    newPointX = v0XPrime + p0X
    newPointY = v0YPrime + p0Y
    newPoint2X = v2XPrime + p2X
    newPoint2Y = v2YPrime + p2Y
    #print(newPointX, newPointY, newPoint2X, newPoint2Y)

    #At this point, we need to see the order of the points for the order of edges.
    distance = math.sqrt((newPointX-p0X)**2+(newPointY-p0Y)**2)
    distance2 = math.sqrt((newPoint2X-p0X)**2+(newPoint2Y-p0Y)**2)
    #print(distance)
    #print(distance2)

    if distance <= distance2:
        #print("THE FIRST POINT ADDED IS: (", newPointX,",",newPointY,")")
        #print("THE SECOND POINT ADDED IS: (", newPoint2X,",", newPoint2Y,")")
        newPointList.append([newPointX,newPointY])
        newPointList.append([newPoint2X,newPoint2Y])
    else:
        #print("THE FIRST POINT ADDED IS: (", newPoint2X,",",newPoint2Y,")")
        #print("THE SECOND POINT ADDED IS: (", newPointX,",", newPointY,")")
        newPointList.append([newPoint2X,newPoint2Y])
        newPointList.append([newPointX,newPointY])

    #print("---------------------------------------------------------------------------------")


def findShortestDistance(vertex, vertexlist):
    """find the shortest distance between a vertex and all other vertices"""
    shortest = float('inf')
    for v in vertexlist:
        distance = (((vertex[0]-v[0])**2)+((vertex[1]-v[1])**2))**(1/2)
        if not distance == 0 and distance < shortest:
            shortest = distance
    return shortest

def findShortestDistanceInPoly(vertexlist):
    """"find the shortest distance between any 2 vertices"""
    shortest = float('inf')
    for v in vertexlist:
        for v1 in vertexlist:
            if not v == v1:
                distance = (((v1[0]-v[0])**2)+((v1[1]-v[1])**2))**(1/2)
                if distance < shortest:
                    shortest = distance
    return shortest

def runClipping(polyobj, acutelist):
    """runs each acute angle through clipAngle"""
    for acute in acutelist:
        #find which chain the acute angle is in
        for i in range(len(polyobj.polychains)):
            if acute in polyobj.polychains[i] and i == 0:#outer boundary
                #find if the angle is the first or last vertex in the chain
                if acute == polyobj.polychains[i][0]:
                    clipAngle(polyobj.polychains[i][-1], acute, acute+1, polyobj.vertexlist)
                elif acute == polyobj.polychains[i][-1]:
                    clipAngle(acute-1, acute, polyobj.polychains[i][0], polyobj.vertexlist)
                else:
                    clipAngle(acute-1, acute, acute+1, polyobj.vertexlist)
            elif acute in polyobj.polychains[i]:#hole
                if acute == polyobj.polychains[i][0]:
                    clipAngle(acute+1, acute, polyobj.polychains[i][-1], polyobj.vertexlist)
                elif acute == polyobj.polychains[i][-1]:
                    clipAngle(polyobj.polychains[i][0], acute, acute-1, polyobj.vertexlist)
                else:
                    clipAngle(acute+1, acute, acute-1, polyobj.vertexlist)

    setVertexEdge(polyobj.vertexlist, mock.edgelists)

def setVertexEdge(vertexlist, edgelists):
    #Creates new vertex and edgelists
    newMockVertexList = []
    newMockEdgeLists = []

    #print(mock.vertexlist)
    #print(mock.acutelist)
    #print(mock.edgelists)
    #print(newPointList)

    #Run through each vertex in the vertexlist.  If a point is to be changed, change as you loop through each vertex
    for i in range(len(mock.vertexlist)):
        if i in mock.acutelist:
            #Adds the two new points
            newMockVertexList.append(newPointList[0])
            newMockVertexList.append(newPointList[1])
            del newPointList[0]
            del newPointList[0]
        else:
            #Puts in the old points
            newMockVertexList.append(mock.vertexlist[i])

    print(newMockVertexList)

    #Run through the edge list.  Now that there are more points, we have to change how many vertices are in each edge
    start = 0
    end = 0
    for i in range(len(mock.edgelists)):
        for j in range(len(mock.edgelists[i])):
            lengthEdge = len(mock.edgelists[i])
            if j in mock.acutelist:
                lengthEdge = lengthEdge + 1
        end = lengthEdge + start
        newMockEdgeLists.append(list(range(start,end+1)))
        start = lengthEdge + 1

    print(newMockEdgeLists)

if __name__ == "__main__":
    PND = mock.MockPolyNodeData(mock.edgelists)
    clipped = runClipping(PND, mock.acutelist)
