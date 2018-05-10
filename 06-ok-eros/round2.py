def findIntersection(rect1, rect2):
    xMin = max(rect1['left_x'], rect2['left_x'])
    xMax = min(rect1['left_x'] + rect1['width'], rect2['left_x'] + rect2['width'])

    yMin = max(rect1['bottom_y'], rect2['bottom_y'])
    yMax = min(rect1['bottom_y'] + rect1['height'], rect2['bottom_y'] + rect2['height'])

    if xMin > xMax or yMin > yMax: return {}

    return {
        'left_x'   : xMin,
        'bottom_y' : yMin,

        'width'    : xMax - xMin,
        'height'   : yMax - yMin,
    }