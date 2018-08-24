# coding=utf-8
B = ['x', 'y', 'z']
for i in B:
    for j in B:
        for k in B:
            if (i != j and i != k and j != k) and (i != 'x') and (k != 'x' and k != 'z') :
                print("a vs ", i, " b vs ", j, " c vs ", k)

