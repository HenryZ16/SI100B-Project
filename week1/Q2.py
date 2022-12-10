#Question 2
import math
grd = 0.0
loc = 0.0
si = 0.0 

for i in range(17):# sample average
    grd = float(input())
    loc = loc + grd / 17
print(loc)
for i in range(17):#sample standard deviation
    grd = float(input())
    si = si + (grd - loc)*(grd - loc) / 17
si = math.sqrt(si)
print(si)
l = loc - 1.96 * si 
r = loc + 1.96 * si
print("(",l,",",r,")")
#these are caculated by all datas(55) loc = 76         l r =( 51.2 , 100.7)
#when n = 6           loc = 80.83    l r = ( 64.8 , 96.7 )
#                     loc = 78.16    l r = ( 61.0 , 95.2 )
#                     loc = 73.00    l r = ( 46.4 , 99.5 )
#when n = 11          loc = 69.41    l r = ( 36.0 , 102.8 )
#                     loc = 77.66    l r = ( 58.7 , 96.5 )
#                     loc = 79.29    l r = ( 59.1 , 99.4 )
#when n = 17          loc = 78.29    l r = ( 57.7 , 98.7 )
#                     loc = 71.19    l r = ( 41.2 , 101.0 )
#                     loc = 78.32    l r = ( 56.7 , 99.9 )
#we can find that  loc is becoming closer to all datas    r - l is smaller 
#while n is becoming larger
