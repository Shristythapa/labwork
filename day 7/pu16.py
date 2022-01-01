#function using lambda keyword
add_sub=lambda x,y : (x+y,x-y)
a,b=add_sub(10,20)
print(a)
print(b)

a=[1,2,3]
b=[3,4,5]
abc=list(map(lambda x,y:x+y,a,b))   
print(abc)

a=[12,1,3,4,5,6,865,4,6,45,6,1,4,23]
var=list(filter(lambda i: i%2==0,a))
print(var)


