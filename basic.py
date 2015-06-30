def And(x,y):
    if x==1 and y==1:
        return 1
    return 0

def Or(x,y):
    if x==0 and y==0:
        return 0
    return 1

def Not(x):
    if x==0:return 1
    return 0
    
