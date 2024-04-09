import heapq
def find_ksmall(arr,k):
    heapq.heapify(arr)
    while k>0:
        s=heapq.heappop(arr)
        k=k-1
    return s

arr=list(map(int,input("enter list: ").split()))
k=int(input("enter k: "))
ans=find_ksmall(arr,k)
print(ans)
