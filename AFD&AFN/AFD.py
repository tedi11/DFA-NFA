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

f = open("test2.txt")
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
ok = 1
s = input("Word: ")
position = 0
for way in s:
    for i in range(n):
        if m[position][i] != -1:
            if way in m[position][i]:
                position = i
                sol.append(i)
                break 
    else:
        print("Not accepted!")
        ok = 0
        break
if destinations[position] == 1:
    print("This word is accepted!")
    print("The solution is:")
    print(*sol)
elif ok == 1:           
    print("Not accepted!")



