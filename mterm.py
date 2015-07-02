from base_class import BVar as B
import re


def checkIfValid(exp):
    a = re.search('[^x\d*+~-]|([^x]\d)',exp)
    if a:
        return False
    return True

def modify(exp):
    #a = re.search(r'x[^\d]',exp)
   
    exp = re.sub( r'x(?!\d)','x1',exp )
    return exp

def max_ind(exp):
    nums = re.findall(r'\d',exp)
    if not nums:
        return 0
    return int(max(nums))

def dec2bin(dec,n):
    l = []
    for i in range(n):
        l.append(dec%2)
        dec = dec/2
    l.reverse()
    return l

def bin2dec(bb):
    import copy
    b = copy.deepcopy(bb)
    b.reverse()
    sum = 0
    pro = 1
    for i in b:
        sum += i*pro
        pro *= 2
    
    return sum 

def fnc(exp):
    n = max_ind(exp)
    l = []
    ## create x1 to xn
    for i in range(n):
        exec('x%d=B()'%(i+1))
    for i in range(pow(2,n)):
        tmp = dec2bin(i,n)
        #tmp.reverse()   
        for j in range(n):
            exec('x%d.set(%d)'%(j+1,tmp[j]))
        exec('res = %s'%exp)
        if res==B(1):
            l.append(i)
    return l
            


def m(exp):
    if not checkIfValid(exp):
        from sys import stderr
        print >>stderr,'Invalid expression'
        return None
    exp = modify(exp)
    #mind = max_ind(exp)
    return fnc(exp)




def main():
    s = raw_input('provide the expression : \n')
    print 'm',m(s)

if __name__=='__main__':
    main()

