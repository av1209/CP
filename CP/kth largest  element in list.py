import heapq
def find_klargest(arr,k):
    arr=[-item for item in arr]
    heapq.heapify(arr)
    while k>0:
        s=heapq.heappop(arr)
        k=k-1
    return s*-1

arr=list(map(int,input("enter list: ").split()))
k=int(input("enter k: "))
ans=find_klargest(arr,k)
print(ans)
