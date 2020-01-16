def istap(tree):
    if len(tree) == 2:
        return type(tree[1]) == int
    return False

def helpercheck(tree,o):
    if tree == []:
        return False
    elif istap(tree) and tree[1] <= o:
        return True
    elif istap(tree):
        return False
    else:
        u = True
        if type(tree[0]) == str:
            for i in range(len(tree)-1):
                if istap(tree[i+1]) and tree[i+1][1] <= o:
                    continue
                elif istap(tree[i+1]):
                    u = False
                    break
                elif type(tree[i+1]) == list:
                    u = helpercheck(tree[i+1],o)
                    if u == False:
                        break
                else:
                    u = False
        else:
           return False
    return u

def helper(tree,o):
    if tree == []:
        return []
    else:
        if helpercheck(tree,o):
            return [tree[0]]
        else:
            if istap(tree):
                return []
            elif type(tree[0]) == str:
                return helper(tree[1:],o)
            else:
                return helper(tree[0],o) + helper(tree[1:],o)

def maxi(tree):
    if tree == []:
        return 0
    elif istap(tree):
        return tree[1]
    else:
        if type(tree[0]) == str:
            return maxi(tree[1:])
        else:
            return max(maxi(tree[0]),maxi(tree[1:]))

def c(tree,o,num):
    lst = []
    while o <= num:
        lst += [helper(tree,o)]
        o += 1
    while o > 2:
        for x in lst[o-3]:
            if x in lst[o-2]:
                lst[o-2].remove(x)
        o -= 1
    return lst

def chalchiuhtlicue(tree):
    num = maxi(tree)
    return c(tree,1,num)

