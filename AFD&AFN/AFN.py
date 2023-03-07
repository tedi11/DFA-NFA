import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:

    def __init__(self):
        self.visual = []
        
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)     

    def visualize(self):
        G = nx.MultiDiGraph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G, node_color='red', connectionstyle='arc3, rad = 0.1')
        plt.show()   

def func(position, w, sol):
    global ok
    if(len(w)==0):
        if destinations[position] == 1:
            print(*sol)
            ok = 1
            return
    l = w[0:1]
    for i in range(n):
        if m[position][i] != -1:
            if l in m[position][i]:
                sol.append(i)
                func(i, w[1:], sol)
                sol.pop(-1)

f = open("test1.txt")
n = int(f.readline())
destinations = [0 for x in range(n)]
m = [[-1 for x in range(n)] for k in range(n)]

for i in range(n):
    fin = int(f.readline())
    destinations[i] = fin
    v = int(f.readline())
    for j in range(v):
        line = f.readline()
        dest = int(line.split()[0])
        pas = (line.split()[1])
        try:
            m[i][dest].append(pas)
        except:
            m[i][dest] = [pas]

G = GraphVisualization()
for i in range(n):
    for j in range(n):
        if m[i][j] != -1:
            for element in m[i][j]:
                G.addEdge(i, j)            

while G.visualize():
    G.visualize()

sol = []
ok = 0
s = input("Word: ")
position = 0
#print(s[0])
func(position, s, sol)
if ok == 0:
    print("There is no solution!")
    