n=int(input("enter no of vertices:"))
e=int(input("enter no of edges:"))
inc=[[0]*e for i in range(n)]
for i in range(n):
    for j in range(e):
        x=input(f"vertex {i} linked with edge{j}:y/n?")
        if x=='y':
            inc[i][j]=1
    print("incidence matrix:")
    for i in range(n):
        print(*inc[i])
