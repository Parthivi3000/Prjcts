a = (input("please select an option : 1.) square, 2.) rectangle, 3) circle, 4) triangle, 5) trapezium "))
l = "square"
m = "rectangle"
p = "circle"
f = "triangle"
o = "trapezium"
if a == l or a == m:
    sa = int(input("enter 1st value : "))
    ra = int(input("enter 2nd value : "))
    s = (sa*ra)
    print (s)
    exit
    
elif a == p :
    c = int(input("enter the radius : "))
    ac = (22/7*c*c)
    print (ac)
    exit
    
elif a == f :
    ta = int(input("enter the base : "))
    at = int(input("enter the height : "))
    t = (1/2*ta*at)
    print(t) 
    exit
    
elif a == o :
    tr = int(input("enter the 1st value : "))
    rt = int(input("enter the 2nd value : "))
    h = int(input("enter the height : "))
    z = (1/2*h*tr+rt)
    print(z)
    exit
    
else :
    print("invalid selection")