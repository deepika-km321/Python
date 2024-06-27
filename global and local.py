# global_var=20
#
# def fun():
#     local_var=10
#     print(local_var)
#     print(global_var)
# fun()
# #print(local_var)#unable to declare the local variable outside the fnction
# print(global_var)


# xy=100
# def fun():
#     xy=200
#     print(xy)
# fun()

xy=100
def fun():
    global xy
    xy=200
    print(xy)
fun()
print(xy)








