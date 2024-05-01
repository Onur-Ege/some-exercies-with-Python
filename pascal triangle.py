def pascal(n):
    r = [1]
    print(r)

    for a in range(1,n+1):
        r = r + [0]
        tr = [0] + r
        nr = [ x + y for x , y in zip(r,tr)]
        print(nr)
        r = nr

n = int(input("enter number of rows displayed:"))

pascal(n)
