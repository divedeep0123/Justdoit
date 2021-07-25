import copy

a1=[1,2,3,4]
b1=copy.deepcopy(a1)
a1[0]="a"
print(a1)
print(b1)