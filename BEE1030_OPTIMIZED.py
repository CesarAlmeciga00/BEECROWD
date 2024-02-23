import sys
sys.setrecursionlimit(10000)
def find_survivor(n, k):
    if n == 1:
        return 1
    else:
        return (find_survivor(n - 1, k) + k - 1) % n + 1

if __name__ == '__main__':
    cases = int(input())
    for i in range(cases):
        a, b = map(int, input().split())
        survivor = find_survivor(a, b)
        print(f"Case {i + 1}: {survivor}")