def isCovered(cp_bl, cp_tr, t1_bl, t1_tr, t2_bl, t2_tr):
    t1 = t1_bl + t1_tr
    t2 = t2_bl + t2_tr
    cp = cp_bl + cp_tr
    #to write less
    if((cp[0] >= t1[0] and cp[1] >= t1[1] and cp[2] <= t1[2] and cp[3] <= t1[3]) or (cp[0] >= t2[0] and cp[1] >= t2[1] and cp[2] <= t2[2] and cp[3] <= t2[3])):
        return "COMPLETELY COVERED"
    #this condition checks if one of them covers all cp by itself
    elif(cp[0] >= t1[0] and cp[1] >= t1[1] and cp[2] >= t1[2] and cp[3] <= t1[3]):
        original = cp[0]
        cp[0] = t1[2]
        if(cp[0] >= t2[0] and cp[1] >= t2[1] and cp[3] <= t2[3] and cp[2] <= t2[2]):
            return "COMPLETELY COVERED"
        cp[0] = original
        #this condition checks if t1 covers one part and t2 covers the rest
    elif(cp[0] >= t2[0] and cp[1] >= t2[1] and cp[3] <= t2[3] and cp[2] >= t2[2]):
        original = cp[0]
        cp[0] = t2[2]
        if(cp[0] >= t1[0] and cp[1] >= t1[1] and cp[3] <= t1[3] and cp[2] <= t1[2]):
            return "COMPLETELY COVERED"
        cp[0] = original   
        #since i didn't check which t is on the left t2 might cover the left part. This is the same code with the previous condition
    elif(cp[0] >= t1[0] and cp[1] >= t1[1] and cp[2] <= t1[2] and cp[3] >= t1[3]):
        original = cp[1]
        cp[1] = t1[3]
        if(cp[0] >= t2[0] and cp[1] >= t2[1] and cp[2] <= t2[2] and cp[3] <= t2[3]):
            return "COMPLETELY COVERED"
        cp[1] = original
        #this condition checks if t1 covers the bottom half and t2 covers the rest
    elif(cp[0] >= t2[0] and cp[1] >= t2[1] and cp[2] <= t2[2] and cp[3] <= t2[3]):
        original = cp[1]
        cp[1] = t2[3]
        if(cp[0] >= t1[0] and cp[1] >= t1[1] and cp[2] <= t1[2] and cp[3] <= t1[3]):
            return "COMPLETELY COVERED"
        #since i didn't check which t is at bottom i wrote the same code for t2
    else:
        return "NOT COMPLETELY COVERED"
    # there is no other condition for t1 and t2 to cover eveyrthing. So it returns not covered
