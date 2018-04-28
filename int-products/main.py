def sequenceEqual(self, a, b):
    if len(a) != len(b): return False
    
    for index in range(0, len(a)):
        if a[index] != b[index]: return False

    return True