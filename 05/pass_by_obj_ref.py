#pass by obj ref

def f1(l,val):
    l[0] = "new"
    val = 100 #shadowing parametr
    pass
nums = [1,2,3,4,5]
a = 999

print(nums,a)
f1(nums,a)
print(nums,a)
