def coins(one, two, five, goal):
    for i in range(one + 1):
        for j in range(two + 1):
            for k in range(five + 1):
                if i+j*2+k*5 == goal:
                    return True
    
    return False

print(coins(2,1,1,8))