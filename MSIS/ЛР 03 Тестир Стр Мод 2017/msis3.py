import csv

def one(A, B, C, D):
    conds = ""
    path = ""

    path += "B1"
    X = Y = Z = R = 12

    path += "-L1"
    if B < 4:
        conds += "B < 4, "
        path += "-L3"
        if B > 3:
            conds += "B > 3, "
        else:
            conds += "B <= 3, "
            path += "-B3"
            X = Y * Z
    else:
        conds += "B >= 4, "
        path += "-L2"
        if A == 4:
            conds += "A == 4, "
        else: 
            conds += "A != 4"
            path += "-B2"
            R = Y + Z

    path += "-L4"
    if D < 11:
        conds += "D < 11, "
    else:
        conds += "D >= 11, "
        path += "-L5"
        if A >= 3:
            conds += "A >= 3, "
            path += "-B4"
            Y *= 2
        else:
            conds += "A < 3, "
            path += "-L6"
            if C <= 1:
                conds += "C <= 1, "
            else:
                conds += "C > 1, "
                Z = X

    path += "-L7"
    if C < 4:
        conds += "C < 4, "
        path += "-B7"
        R = 5
    else:
        conds += "C >= 4, "
        path += "-B6"
        Z = 0

    return X, Y, Z, R, conds, path


def two(A, B, C, D):
    conds = ""
    path = ""

    path += "B1"
    X = Y = Z = R = 12

    path += "-L1"
    if C < 8:
        conds += "C < 8, "
        path += "-B3"
        Z += 2
    else:
        conds += " C>=8, "
        path += "-L2"
        if A < 5:
            conds += "A < 5, "
            path += "-B2"
            Z *= 2
        else:
            conds += "A>=5, "
            path += "-L3"
            if D > 1:
                conds += "D>1"
            else:
                conds += "D<=1, "
                path += "-B4"
                X = 5
    path += "-L4"
    if B<4:
        conds += "B<4, "
        path += "-B5"
        Y = 5
    else:
        conds += "B>=4, "
        path += "-L5"
        if B>5:
            conds += "B>5, "
        else:
            conds += "B<=5, "
            path += "-L6"
            if D<5:
                conds += "D<5, "
            else:
                conds += "D>=5, "
                path += "-B6"
                Z = 0
    path += "-L7"
    if A>7:
        conds += "A<7, "
        path += "-B7"
        R = -3
    else:
        conds += "A>=7"
    return X, Y, Z, R, conds, path


def test():
    result = {}
    for A in range(0, 20):
        for B in range(0, 20):
            for C in range(0, 20):
                for D in range(0, 20):
                    # try:
                    result[two(A, B, C, D)] = [A, B, C, D]
                    # except:
                    #     pass

    with open("a.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i, r in enumerate(result.keys()):
            writer.writerow([*result[r], *r, i + 1])

    
test()
    
