#!/usr/bin/env python

import math

from evert import Room, Source, Listener, Vector3, Matrix3, Polygon, PathSolution

def main():

    room = Room()
    
    # Define a simple cube (1000 x 1000 x 1000 mm) as room geometry
    face1poly = Polygon([Vector3(0,0,0), Vector3(0,1000,0), Vector3(1000,1000,0), Vector3(1000,0,0)])
    face2poly = Polygon([Vector3(0,0,0), Vector3(0,1000,0), Vector3(0,1000,1000), Vector3(0,0,1000)])
    face3poly = Polygon([Vector3(0,0,0), Vector3(1000,0,0), Vector3(1000,0,1000), Vector3(0,0,1000)])
    face4poly = Polygon([Vector3(0,0,1000), Vector3(0,1000,1000), Vector3(1000,1000,1000), Vector3(1000,0,1000)])
    face5poly = Polygon([Vector3(0,1000,1000), Vector3(0,1000,0), Vector3(1000,1000,0), Vector3(1000,1000,1000)])
    face6poly = Polygon([Vector3(1000,0,1000), Vector3(1000,1000,1000), Vector3(1000,1000,0), Vector3(1000,0,0)])
    polygons = [face1poly, face2poly, face3poly, face4poly, face5poly, face6poly]
    for poly in polygons:
        room.addPolygon(poly, color=Vector3(0.5,0.5,0.5))
    room.constructBSP()

    center = room.getCenter()
    print 'Room maximum length: ', room.getMaxLength()
    print 'Room center: x=%f, y=%f, z=%f' % (center.x, center.y, center.z)
    print 'Number of elements: ', room.numElements()
    print 'Number of convex elements: ', room.numConvexElements()
    
    # Create source localized in room
    src1 = Source()
    src1.setPosition(Vector3(750,750,750))
    src1.setOrientation(Matrix3(0,0,1,
                                1,0,0,
                                0,1,0))
    src1.setName('Src1')
    room.addSource(src1)
    print 'Number of sources: ', room.numSources()
    
    # Create listener localized in room
    list1 = Listener()
    list1.setPosition(Vector3(250, 250, 500))
    list1.setOrientation(Matrix3(0,0,-1,
                                 -1,0,0,
                                 0,1,0))
    list1.setName('Lst1')
    room.addListener(list1)
    
    list2 = Listener()
    list2.setPosition(Vector3(240, 240, 500))
    list2.setOrientation(Matrix3(0,0,-1,
                                 -1,0,0,
                                 0,1,0))
    list2.setName('Lst2')
    room.addListener(list2)
    print 'Number of listeners: ', room.numListeners()
    
    for s in range(room.numSources()):
        for l in range(room.numListeners()):
            src = room.getSource(s)
            lst = room.getListener(l)
    
            print '-----------------------------------'
            print 'From source %s to listener %s' % (src.getName(), lst.getName())
            print '-----------------------------------'
            
            # Calculate paths
            maximumOrder = 8
            solution = PathSolution(room, src, lst, maximumOrder)
            solution.update()
            print 'Number of paths calculated: ', solution.numPaths()
            
            # Analyze paths
            minPathLength = None
            maxPathLength = 0
            for i in range(solution.numPaths()):
                path = solution.getPath(i)
                
                # Calculate path length
                pathLength = 0.0
                lastPt = path.m_points[0]
                for pt in path.m_points[1:]:
                    pathLength += math.sqrt((lastPt.x - pt.x)**2 + 
                                            (lastPt.y - pt.y)**2 + 
                                            (lastPt.z - pt.z)**2)
                    lastPt = pt
                
                if pathLength > maxPathLength:
                    maxPathLength = pathLength
                if pathLength < minPathLength or minPathLength is None:
                    minPathLength = pathLength
                
            print 'Minimum path length: ', minPathLength
            print 'Maximum path length: ', maxPathLength
    
if __name__ == "__main__":
    main()