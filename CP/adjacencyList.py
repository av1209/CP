class Graph:
    def __init__(self,v):
        self.v=v
        self.adj_list = {i:[] for i in range(v)}

    def add_w(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # If it's an undirected graph

    def print_list(self):
        for i in self.adj_list:
            print(item,'->','->'.join(map(str,self.addlist[i])))

v=int(input("no.of nodes: "))
obj=Graph()
obj.add_w(0,1,3)
obj.add_w(1,2,5)
obj.add_w(3,4,6)
obj.add_w(0,4,7)
obj.add_w(4,1,11)
obj.add_w(3,1,2)
obj.add_w(2,3,10)
obj.print_l()
