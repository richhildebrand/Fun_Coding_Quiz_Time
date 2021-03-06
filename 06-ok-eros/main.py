import sys

def findIntersection(r1, r2):
    highestX = min(r1['left_x'] + r1['width'], r2['left_x'] + r2['width'])
    lowestX = max(r1['left_x'], r2['left_x'])
    highestY = min(r1['bottom_y'] + r1['height'], r2['bottom_y'] + r2['height'])
    lowestY = max(r1['bottom_y'], r2['bottom_y'])

    if highestX < lowestX: return {}
    if highestY < lowestY: return {}

    return {
        # Coordinates of bottom-left corner
        'left_x'   : lowestX,
        'bottom_y' : lowestY,

        # Width and height
        'width'    : highestX - lowestX,
        'height'   : highestY - lowestY,
    }