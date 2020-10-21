def sumIntervals(intervals):
    dif = 0
    valores = []
    for interval in intervals:
        dif += (interval[1] - interval[0])
        for border in range(interval[0], interval[1]):
            if border in valores:
                dif -= 1
            else:
                valores.append(border)
    print(dif, valores)


intervals=([
    [1, 2],
    [6, 10],
    [11, 15]
])
# // = > 9

sumIntervals([
    [1, 4],
    [7, 10],
    [3, 5]
])
# // = > 7

sumIntervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]
])
# // = > 19
