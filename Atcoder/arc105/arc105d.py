for T in range(int(input())) :
    n = int(input())
    a = list(map(int, input().split()))
    mp = {a[i] : 0 for i in range(n)}
    if n & 1 : 
        print("Second")
    else :
        for i in range(n) :
            mp[a[i]] ^= 1
        for i in range(n) :
            if mp[a[i]] :
                print("First")
                break
        else :
            print("Second")