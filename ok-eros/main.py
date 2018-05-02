import sys

def findIntersection(r1, r2):
    lowestX = sys.maxsize
    highestX = -sys.maxsize-1
    lowestY = sys.maxsize
    highestY = -sys.maxsize-1

    for x in range(r1['left_x'], r1['left_x'] + r1['width'] + 1):
        if r2['left_x'] <= x <= (r2['left_x'] + r2['width']):
            print("x inside: " + str(x))
            lowestX = min(lowestX, x)
            highestX = max(highestX, x)
        
    for y in range(r1['bottom_y'], r1['bottom_y'] + r1['height'] + 1):
        if r2['bottom_y'] <= y <= (r2['bottom_y'] + r2['height']):
            print("y inside: " + str(y))
            lowestY = min(lowestY, y)
            highestY = max(highestY, y)

    return {
        # Coordinates of bottom-left corner
        'left_x'   : lowestX,
        'bottom_y' : lowestY,

        # Width and height
        'width'    : highestX - lowestX,
        'height'   : highestY - lowestY,
    }