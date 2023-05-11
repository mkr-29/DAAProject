import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import random

def BFS(start):
    queue = deque()  
    queue.append(start)
    visited[start] = True
    level[start] = 0
    
    while queue:
        u = queue.popleft()
        print(u, " -> ", end = "")
        for v in G.adj[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                level[v] = level[u] + 1

                
        DrawIteratedGraph(G, level)
        plt.title('From {}:'.format(u), loc='left')
        plt.title('Level {}:'.format(level[u]), loc='right')
        plt.show()
        
    print("End")

def DFS(start):
    stack = []  
    stack.append(start)
    visited[start] = True
    parent[start] = 0
    
    while stack:
        u = stack.pop()
        print(u, " -> ", end = "")
        
        if(not visited[u]):
            print(u, " -> ", end = "")
            visited[u] = True
        
        for v in G.adj[u]:
            if not visited[v]:
                stack.append(v)
                visited[v] = True
                parent[v] = parent[u]

                
        DrawIteratedGraph(G, parent)
        plt.title('From {}:'.format(u), loc='left')
        plt.title('Level {}:'.format(parent[u]), loc='right')
        plt.show()
        
    print("End")

def CreateGraph(node, edge):
    G = nx.Graph()

    for i in range(1, node+1):
        G.add_node(i)

    for i in range(1, edge+1):
        while True:
            u, v = random.randint(1, node), random.randint(1, node)
            if u != v and not G.has_edge(u, v):
                G.add_edge(u, v)
                break
    return G




def DrawGraph(G, color):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels = True, node_color = color, edge_color = 'black' ,width = 1, alpha = 0.7)  #with_labels=true is to show the node number in the output graph

def DrawIteratedGraph(G, col_val):
    pos = nx.spring_layout(G)
    color = ["green", "blue", "yellow", "pink", "red", "black", "gray", "brown", "orange", "plum"]
    random.shuffle(color)  # shuffle the list of colors randomly
    values = []
    for node in G.nodes():
        if node == 1:  # assign a fixed color to the first node
            values.append('green')
        else:
            values.append(color[col_val[node]])
    nx.draw(G, pos, with_labels=True, node_color=values, edge_color='black', width=1, alpha=0.7)






if __name__ == "__main__":
    
    print("Input node no: ", end = "")
    node = int(input())
    print("Input edge no: ", end = "")
    edge = int(input())
    
    G = CreateGraph(node, edge)
    print("Nodes: ", G.nodes)
    # print(list(G.edges))
    # print(list(G.adj))
    # print(list(G.degree))
    DrawGraph(G, "green")
    plt.show()
    
    visited = [False for i in range(node+1)]
    level = [0 for i in range(node+1)]
    parent = [0 for i in range(node+1)]
    components = 0
    
    for i in G.nodes:
        if(not visited[i]):
            print("Starting: ", i)
            DFS(i)
            # BFS(i)
            components += 1
    print("Total components: ", components)