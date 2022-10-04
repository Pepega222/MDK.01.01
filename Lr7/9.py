import sys
save_stdin = sys.stdin
sys.stdin = open("text1.txt")

N, P = input().split()
N, P = int(N), int(P)
cnt = [0] * (N-1)
for i in range(P):
    fam, name, pFrom, pTo = input().split()
    pFrom, pTo = int(pFrom), int(pTo)
    for p in range(pFrom, pTo):
        cnt[p-1] += 1

pMin = min(cnt)
for p in range(N-1):
    if cnt[p] == pMin:
        print("%d-%d" % (p+1, p+2))

sys.stdin = save_stdin