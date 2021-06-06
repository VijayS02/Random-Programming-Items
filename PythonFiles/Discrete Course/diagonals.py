def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


def extend(perm, n,x):
    if len(perm) == n:
        #print(perm)
        x +=1
        print(x)

    else:
        for k in range(n):
            if k not in perm:
                perm.append(k)

                if can_be_extended_to_solution(perm):
                      x = extend(perm, n,x)

                perm.pop()

    return x
extend([], 20, 0)