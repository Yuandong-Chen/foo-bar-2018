import math

def commonFactor(x,y):
    if x == 0: return 'inf'
    if y == 0: return 0
    big = max(x,y)
    small = min(x,y)
    while(small!=0):
        r = small
        small = big % r
        big = r
    return abs(big)

def position(dimensions, captainPosition, badguyPosition,source):
    captains = []
    badguys = []
    width = dimensions[0]
    height = dimensions[1]
    cx = captainPosition[0]
    cy = captainPosition[1]
    gx = badguyPosition[0]
    gy = badguyPosition[1]
    for x,y in source[(0,0)]:
        captains.append((x,y))
        badguys.append((x+gx-cx,y+gy-cy))
    for x,y in source[(1,0)]:
        captains.append((x+width-2*cx,y))
        badguys.append((x+width-gx-cx,y+gy-cy))
    for x,y in source[(0,1)]:
        captains.append((x,y+height-2*cy))
        badguys.append((x+gx-cx,y+height-gy-cy))
    for x,y in source[(1,1)]:
        captains.append((x+width-2*cx,y + height-2*cy))
        badguys.append((x+width-gx-cx,y + height-gy-cy))
    return captains,badguys

def origin(dimensions, distance):
    sources = {}
    sources[(0,0)]=[]
    sources[(1,0)]=[]
    sources[(0,1)]=[]
    sources[(1,1)]=[]
    width = dimensions[0]
    height = dimensions[1]
    w = (distance/width) + 1
    h = (distance/height) + 1
    for x in range(-w,w+1):
        for y in range(-h,h+1):
            if x % 2 == y % 2:
                if x % 2 == 0:
                    sources[(0,0)].append((x*width,y*height))
                else:
                    sources[(1,1)].append((x*width,y*height))
            else:
                if x % 2 == 0:
                    sources[(0,1)].append((x*width,y*height))
                else:
                    sources[(1,0)].append((x*width,y*height))
    return sources

def countPossibilities(captain,badguy):
    global possibilities
    possibilities = {}
    for x,y in badguy:
        common = commonFactor(x,y)
        if common == 0:
            if (0 not in possibilities or possibilities[0]>abs(x)):
                possibilities[0]= abs(x)
        elif common == 'inf':
            if ('inf' not in possibilities or possibilities['inf']>abs(y)):
                possibilities['inf']= abs(y)
        elif (x/common,y/common) not in possibilities or possibilities[(x/common,y/common)]>math.sqrt(x**2+y**2):
            possibilities[(x/common,y/common)]= math.sqrt(x**2+y**2)
    for x,y in captain:
        common = commonFactor(x,y)
        if common == 0:
            if 0 in possibilities and possibilities[0]>abs(x):
                del possibilities[0]
        elif common == 'inf':
            if 'inf' in possibilities and possibilities['inf']>abs(y):
                del possibilities['inf']
        elif (x/common,y/common) in possibilities and possibilities[(x/common,y/common)]>math.sqrt(x**2+y**2):
            del possibilities[(x/common,y/common)]
    return possibilities

def answer(dimensions, captainPosition, badguyPosition, distance):
    origins = origin(dimensions, distance)
    captain,badguy = position(dimensions, captainPosition, badguyPosition,origins)
    captain = [x for x in captain if math.sqrt(x[0]**2+x[1]**2) <= distance and not (x[0]==x[1]==0)]
    badguy = [x for x in badguy if math.sqrt(x[0]**2+x[1]**2) <= distance and not (x[0]==x[1]==0)]
    possibilities = countPossibilities(captain,badguy)
    return len(possibilities)
