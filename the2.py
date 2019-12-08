def isCovered(cp_bl, cp_tr, t1_bl, t1_tr, t2_bl, t2_tr):
    t1 = t1_bl + t1_tr
    t2 = t2_bl + t2_tr
    cp = cp_bl + cp_tr
    if((cp[0] >= t1[0] and cp[1] >= t1[1] and cp[2] <= t1[2] and cp[3] <= t1[3]) or (cp[0] >= t2[0] and cp[1] >= t2[1] and cp[2] <= t2[2] and cp[3] <= t2[3])):
        return "completely covered"
    elif(cp[0] >= t1[0] and cp[1] >= t1[1] and cp[3] <= t1[3] and cp[0] <= t1[2]):
        original = cp[0]
        cp[0] = t1[2]
        if(cp[0] >= t2[0] and cp[1] >= t2[1] and cp[3] <= t2[3] and cp[0] <= t2[2]):
            return "completely covered"
        cp[0] = original
    elif(cp[0] >= t2[0] and cp[1] >= t2[1] and cp[3] <= t2[3] and cp[0] <= t2[2]):
        original = cp[0]
        cp[0] = t2[2]
        if(cp[0] >= t1[0] and cp[1] >= t1[1] and cp[3] <= t1[3] and cp[0] <= t1[2]):
            return "completely covered"
        cp[0] = original   
    elif(cp[0] >= t1[0] and cp[1] >= t1[1] and cp[2] <= t1[2] and cp[3] >= t1[3]):
        original = cp[1]
        cp[1] = t1[2]
        if(cp[0] >= t2[0] and cp[1] >= t2[1] and cp[2] <= t2[2] and cp[3] >= t2[3]):
            return "completely covered"
        cp[1] = original
    elif(cp[0] >= t2[0] and cp[1] >= t2[1] and cp[2] <= t2[2] and cp[3] >= t2[3]):
        original = cp[1]
        cp[1] = t1[2]
        if(cp[0] >= t1[0] and cp[1] >= t1[1] and cp[2] <= t1[2] and cp[3] >= t1[3]):
            return "completely covered"
    else:
        return "not completely covered"
