#!/usr/bin/python

#-- solve an equation ax + by + cz = d
#   with nominating x, y, or z as the unknown
#   and values of the rest given.

#--  {a,b,c,d} and two of {x,y,z} be given as a dict

def solvelineareq(abcd, xyz):
    #-- type check for input dicts should be here. --

    a = abcd['a']; b = abcd['b']; c = abcd['c']; d = abcd['d'];
    #-- check if there is x,y, or z in xyz --
    if not 'x' in xyz:
        xyz.update({'x': (d - b*xyz['y'] - c*xyz['z'])/a})
    if not 'y' in xyz:
        xyz.update({'y': (d - c*xyz['z'] - a*xyz['x'])/b})
    if not 'z' in xyz:
        xyz.update({'z': (d - a*xyz['x'] - b*xyz['y'])/c})

    return xyz

def calccrossingwithcube(abcd):

    #--- prepare fixed values for vertices of the cube ---
    fixedvars = [{   'x':float(i), 'y':float(j)} \
                     for i in range(2) for j in range(2)] + \
                     [{'y':float(i), 'z':float(j)} \
                          for i in range(2) for j in range(2)] + \
                          [{'z':float(i), 'x':float(j)} \
                               for i in range(2) for j in range(2)] 
    
    newvars  = map(lambda l: solvelineareq(adict, l), fixedvars)
    crossing = filter(lambda l: l['x'] >= 0.0 and l['x'] <= 1.0 and \
                          l['y']       >= 0.0 and l['y'] <= 1.0 and \
                          l['z']       >= 0.0 and l['z'] <= 1.0, newvars)

    return crossing

#---

if __name__ == "__main__": 
    
    adict     = {'a':1.0, 'b':1.0, 'c':1.0, 'd':1.4}
    clist = calccrossingwithcube(adict)
    
    #for c in clist:
    #    print c['x'],'\t',c['y'],'\t',c['z']

    #---- create pairs of crossing points to express lines 
    #     on the cut plane  --- 
    pairs = [[clist[i], clist[j]] \
                 for i,x in enumerate(clist) for j,x in enumerate(clist) \
                 if i < j]
    
    #-- see: 
    # http://stackoverflow.com/questions/10272898/multiple-if-conditions-in-a-python-list-comprehension 

    #----  filter lines on the outer surfaces of the cube ---
    #      check if a pair of points are on the same plane of 
    #      x=0,x=1,y=0,y=1,z=0, or z=1  
    outpairs = filter(lambda p:\
                          len([xyz for xyz in p[0] \
                                   if p[0][xyz] == p[1][xyz] and \
                                   (p[0][xyz] == 0.0 or p[0][xyz] == 1.0)\
                                   ]) == 1,\
                          pairs)

    for p in outpairs:
        print p[0]['x'],'\t',p[0]['y'],'\t',p[0]['z']
        print p[1]['x'],'\t',p[1]['y'],'\t',p[1]['z']
        print '\n'
        #print p
