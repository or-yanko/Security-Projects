lst =[1,3,45,6,8,9,65,3,2]
print(len(lst))

while True:
    if len(lst) == 0:
        print('bye')
        break
    print('num=',lst[0])
    print('len=',len(lst))
    print(lst)
    print()
    lst.remove(lst[0])