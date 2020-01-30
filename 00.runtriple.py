ARR = [int(x) for x in input()]

ch = 0
for i1 in range(3):
    for i2 in range(3):
        if i2 != i1 :
            for i3 in range(3):
                if i3 != i1 and i3 != i2 :
                    if ARR[i1] + 1 == ARR[i2] and ARR[i2] + 1 == ARR[i3]:
                        print("run")
                        ch = 1
                        break
                    if ARR[i1]==ARR[i2] and ARR[i2]==ARR[i3]:
                        print("triple")
                        ch = 1
                        break
                    else:
                        print("just number")
                        break
        if ch==1:
            break
    if ch==1:
        break