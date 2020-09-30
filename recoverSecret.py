def recoverSecret(triplets):
    res = []
    while triplets:
        # print(triplets)
        not_firsts = [i for a in triplets for i in a[1:]]
        firsts = [a for a, *_ in triplets]
        print(not_firsts, firsts)
        for i in firsts:
            if i not in not_firsts:
                res.append(i)
                # print(i)
                for t in triplets:
                    if t[0] == i:
                        print(t)
                        t.pop(0)

                break

        triplets = [i for i in triplets if i]

    print("".join(res))


secret1 = "whatisup"
triplets1 = [
    ["t", "u", "p"],
    ["w", "h", "i"],
    ["t", "s", "u"],
    ["a", "t", "s"],
    ["h", "a", "p"],
    ["t", "i", "s"],
    ["w", "h", "s"],
]


recoverSecret(triplets1)
