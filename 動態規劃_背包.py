#設置
#因為座標(0,0)是空的所以[0]無用
w = [0, 1, 4, 3, 1]   #n個物體的重量(w[0]無用)
p = [0, 1500, 3000, 2000, 2000]   #n個物體的價值(p[0]無用)
n = len(w) - 1   #計算n的個數
m = 4   #背包的載重量

x = []   #裝入背包的物體，元素為True時，對應物體被裝入(x[0]無用)
v = 0
#optp[i][j]表示在前i個物體中，能夠裝入載重量為j的背包中的物體的最大價值
optp = [[0 for col in range(m + 1)] for raw in range(n + 1)]
#optp 相當於做了一個n*m的全零矩陣，n行為物件，m列為自背包載重量

def knapsack_dynamic(w, p, n, m, x):
    #計算optp[i][j]
    for i in range(1, n + 1):       # 物品一件件丟進來
        for j in range(1, m + 1):   # j為子背包的目前能裝的量，尋找能夠裝得下的包包
            if (j >= w[i]):         # 當物品的重量小於背包能夠承受的重量的時候，才考慮能不能放進去
                optp[i][j] = max(optp[i - 1][j], optp[i - 1][j - w[i]] + p[i])
                # optp[i - 1][j]是上一個單元的值， optp[i - 1][j - w[i]]為剩下空間的值
            else:
                optp[i][j] = optp[i - 1][j]

    #到推裝入背包裡的東西,尋找改變的地方，從最後結果開始逆推回來
    j = m
    for i in range(n, 0, -1):
        if optp[i][j] > optp[i - 1][j]:
            x.append(i)
            j = j - w[i]

    #將最大值丟回去，也就是表格最後一行一列的位置
    v = optp[n][m]
    return v

print ('最大值為：' + str(knapsack_dynamic(w, p, n, m, x)))
print ('物品的索引：',x)

#最大值為：4000
#物品的索引： [4, 3]
