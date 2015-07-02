from mterm import dec2bin,bin2dec
from math import log,ceil

def listin(a,b):
    '''
    check if every elements of a is in b
    '''
    for i in a:
        if not i in b:
            return False
    return True

def rev(el):
    if el==0:return 1
    if el==1:return 0
    if el==-1:return -1

def fnc(tmp,n,mt):
    import copy
    ntmp = copy.deepcopy(tmp)
    for el in ntmp:
        el[n]=rev(el[n])
    if listin(ntmp,mt):
        tmp.extend(ntmp)
    return tmp


def get_form(tmp):

    n = len(tmp[0])
    l = len(tmp)
    s = ''
    for i in range(n):
        eq = True
        first = tmp[0][i]
        for j in range(1,l):
            if tmp[j][i]!=first:
                eq = False
                break
        if eq:
            if first == 1:
                s += 'x%d*'%(i+1)
            else:
                s += '~x%d*'%(i+1)
    return s[:-1]




def pos(mt):
    n = int(ceil(log(max(mt),2)))
    if n==0:n=1
    mt = [dec2bin(i,n) for i in mt] # convert to binary list
    visited = set()
    
    st = ''
    
    for node in mt:
        if bin2dec(node) in visited:
            continue
        tmp = [node]
        visited.add(bin2dec(node))
        for i in range(n):
            tmp = fnc(tmp,i,mt)
        for k in tmp:
            visited.add(bin2dec(k))
        st += '%s+'%get_form(tmp)
    return st[:-1]
            

def main():
    
    print pos([2,3,9,10,11,13])
                  

if __name__=='__main__':
    main()
