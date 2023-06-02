def F(n:int) -> int :
    if n in (0,1) :
        return 1
    else :
        return F(n-1) + F(n-2)
    
print("Good Use", F(8))
print("Bad Use", F(355/113))
