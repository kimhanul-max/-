a = set(input().split())
b = set(input().split())
c = int(input("합집합:1 교집합:2 차집합:3\n"))
if c == 1:
        print(list(a | b))
elif c == 2:
        print(list(a & b))
elif c == 3:
        print(list(a - b))
