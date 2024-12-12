# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 15:24:15 2023

@author: Administrator
"""
import graph
import numpy as np
import matplotlib.pyplot as plt
import collections

def entropy(f):
    s = 0
    for i in f:
        if i != 0:
            s += -i*np.log2(i)
    return s

def random_travel(random_path,m,G,p):
    delay = 0
    travel_list = []
    if random_path[0] == 0:
        loc = np.random.choice(range(m))
        travel_list.append('z'+str(loc+1))
    else:
        loc = random_path[0]+m-1
        travel_list.append('g'+str(random_path[0]))
    
    for i in random_path[1:]:
        if i == 0:
            nxt = np.random.choice(range(m),p=p[loc])
            travel_list.append('z'+str(nxt+1))
        else:
            nxt = i+m-1
            travel_list.append('g'+str(i))
        delay += G.adj[loc][nxt]
        loc = nxt
    return travel_list, delay

def fangzheng(random_path, m, G, p, draw=0):
    N = 1000000
    x = np.array([random_travel(random_path,m,G,p)[1] for i in range(N)])
    # print(x)
    p = collections.Counter(x)
    # print(p)
    # print(len(p))
    s = sum(p.values())
    for i in p:
        p[i]=p[i]/s
    p = [(i,p[i]) for i in p]
    p.sort(key=lambda x:x[0])
    d = [str(i[0]) for i in p]
    f = [i[1] for i in p]
    if draw:
        plt.bar(d,f)
        plt.ylim(0,0.03)
        plt.axis(False)
        plt.show()
    return entropy(f)

m = 3
g = 3
#先是中间节点，然后是组节点
G = graph.graph(m+g)
G.adj = [
    [0,1e5,1e4,1e6,1e9,1e3,1e16],
    [1e5,0,1e7,1e8,1e10,1e11,1e17],
    [1e4,1e7,0,1,1e12,1e15,1e18],
    [1e6,1e8,1,0,10,100,1e19],
    [1e9,1e10,1e12,10,0,1e14,1e20],
    [1e3,1e11,1e15,100,1e14,0,1e21],
    [1e16,1e17,1e18,1e19,1e20,1e21,0]
    ]

def strategy(p):
    q=(1-p)/2
    return np.array([
     [p,q,q],
     [q,p,q],
     [q,q,p],
     [1/3,1/3,1/3],
     [1/3,1/3,1/3],
     [1/3,1/3,1/3],
     [1/3,1/3,1/3],
     ])

print(fangzheng([1,0,0,0,2], 3, G, strategy(0.333), draw=0))

# p = np.linspace(0,1,100)
# data = []
# for i in range(len(p)):
#     data.append(fangzheng([1,0,0,0,2,0,0,0,3], 3, G, strategy(p[i]), draw=0))
#     print(i,p[i],data[-1])
    
# data = [6.83716909241282,
#   7.065904297724499,
#   7.20863316927369,
#   7.3277273565172765,
#   7.428953305507447,
#   7.516299224060843,
#   7.591762459258194,
#   7.658371250776106,
#   7.714385071315966,
#   7.772099475221703,
#   7.82188079885131,
#   7.8620507502696935,
#   7.8959554703068235,
#   7.928864598086587,
#   7.9619812376905585,
#   7.986742731410246,
#   8.006803110406112,
#   8.027318130365735,
#   8.041662822542095,
#   8.0552700284179,
#   8.066923899478102,
#   8.079135980913975,
#   8.086407419648287,
#   8.085052221380131,
#   8.087791979706612,
#   8.089055981668407,
#   8.093711807918144,
#   8.086421595201768,
#   8.078130879806418,
#   8.075713907506051,
#   8.063294509224836,
#   8.060869890785202,
#   8.053870919126677,
#   8.031724107719922,
#   8.021088507713468,
#   8.008956186733705,
#   7.988832284368297,
#   7.973251466851648,
#   7.948515518111572,
#   7.933265304686676,
#   7.908158763156528,
#   7.8911925450246985,
#   7.867255795835927,
#   7.843105790853604,
#   7.8131866042371945,
#   7.7848166862060415,
#   7.74803050996917,
#   7.721303613817677,
#   7.689003302347545,
#   7.659107841455111,
#   7.618941440487436,
#   7.584672196062966,
#   7.558060679500569,
#   7.50441495052314,
#   7.464262726261797,
#   7.42600964618561,
#   7.383000155587735,
#   7.349217351205887,
#   7.2990474967543895,
#   7.245812999247632,
#   7.215753290061836,
#   7.152711831269914,
#   7.102274857043084,
#   7.044163666818071,
#   7.005955400823735,
#   6.9516111532695755,
#   6.895492820580274,
#   6.829572657264026,
#   6.772844328670791,
#   6.713376565300817,
#   6.647078593367157,
#   6.576978561673693,
#   6.509025227763296,
#   6.43824882317158,
#   6.375085436793195,
#   6.298695567106463,
#   6.224453079864427,
#   6.142480509383897,
#   6.06945724108695,
#   5.975934182373788,
#   5.901382123995299,
#   5.7968184654411115,
#   5.70559185674787,
#   5.622496601516467,
#   5.52540258639859,
#   5.421671546435926,
#   5.311173416947987,
#   5.200857612293103,
#   5.09506773419584,
#   4.964043854017634,
#   4.8435120391559465,
#   4.703340482724569,
#   4.568782076199312,
#   4.4261356277721715,
#   4.272627997512541,
#   4.0968414613209365,
#   3.910910770470948,
#   3.7217476189423735,
#   3.4759299305354214,
#   3.169884942048686]

# plt.plot(p,data)
# plt.show()

# p1 = np.linspace(0.24,0.27,30)
# data1 = []
# for i in range(len(p1)):
#     data1.append(fangzheng([1,0,0,0,2,0,0,0,3], 3, G, strategy(p1[i]), draw=0))
#     print(i,p1[i],data1[-1])
