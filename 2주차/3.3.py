import math

gwangju=[35.1768201,126.7735892]
busan=[35.1645701,129.0015892]
doublegang=[37.7637326,128.8824475]
seoul=[37.565289,126.8491259]

def distance(a,b):
    return 6370.01*math.acos(math.sin(math.radians(a[0]))*math.sin(math.radians(b[0]))
                    -math.cos(math.radians(a[1]))*math.cos(math.radians(b[1])))


g_b=distance(gwangju,busan)
b_d=distance(busan,doublegang)
d_s=distance(doublegang,seoul)
s_g=distance(seoul,gwangju)

def make_area(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5


total= make_area(g_b,b_d,d_s)+make_area(b_d,d_s,s_g)

print(total)