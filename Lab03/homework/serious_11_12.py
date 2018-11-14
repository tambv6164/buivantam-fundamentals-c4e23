def is_inside(a, b):
    return b[0] < a[0] < b[0] + b[2] and b[1] < a[1] < b[1] + b[3]


k = is_inside([100, 120], [140, 60, 100, 200])
if k == False:
    print("Your function is correct")
else:
    print("Oops, there's a bug")
