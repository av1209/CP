class Graph:
    def __init__(self,v):
        self.v=v
        self.g=[[0]*v for i in range(v)]
    def add_w(self, u, v, weight):
        self.g[u][v]=weight
        self.g[v][u]=weight
    def print_m(self):
        for row in self.g:
            print(" ".join(map(str,row)))

# driver code
v=int(input("no.of nodes: "))
obj=Graph(v)
obj.add_w(0,1,3)
obj.add_w(1,2,5)
obj.add_w(3,4,6)
obj.add_w(0,4,7)
obj.add_w(4,1,11)
obj.add_w(3,1,2)
obj.add_w(2,3,10)
obj.print_m()
