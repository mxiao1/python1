import math
def quadratic(a,b,c):
    for i in [a,b,c]:
        if not isinstance(i,(int,float)):
            raise TypeError
    f=b*b-4*a*c
    if a==0 and b==0:
        raise ValueError
    if f<0:
        print('no answer')
    elif f>=0:
        print(-b+math.sqrt(f)/2*a,-b-math.sqrt(f)/2*a)

if __name__=='__main__':
    a=input('输入数字a:')
    b=input('输入数字b:')
    c=input('输入数字c:')
    quadratic(float(a),float(b),float(c))
