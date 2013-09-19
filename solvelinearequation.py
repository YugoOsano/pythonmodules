#!/c/Python27/python

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

#---

if __name__ == "__main__": 
    
    adict     = {'a':1.0, 'b':1.0, 'c':1.0, 'd':1.4}
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

    for c in crossing:
        print c['x'],'\t',c['y'],'\t',c['z']

