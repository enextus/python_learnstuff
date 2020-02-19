
glob_d = 3

def func(a,b,c):
 loc_d = a + b + c
 print(locals())
 print(globals())

func(1,2,3)
