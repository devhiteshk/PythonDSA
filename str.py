from collections import OrderedDict


def merge_the_tools(string, k):
    R = []
    # your code goes here
    d = int(len(string) / k)
    L = [string[i:k + i] for i in range(0, len(string), k)]

    for i in range(len(L)):
        R.append("".join(OrderedDict.fromkeys(L[i])))

    for i in range(len(R)):
        print(R[i])

merge_the_tools("ABCDEFGHIJKLNFWWIANAEFNJVNDFJVHJRBVB",4)