import sys

S = 0  # 공집합으로 초기화
ALL = (1 << 20) - 1  # 모든 비트가 1인 값 미리 계산

M = int(sys.stdin.readline())  # 연산의 수

for _ in range(M):
    command = sys.stdin.readline().strip().split()
    op = command[0]

    if op != 'all' and op != 'empty':
        x = int(command[1]) - 1

    if op == 'add':
        S |= (1 << x)
    elif op == 'remove':
        S &= ~(1 << x)
    elif op == 'check':
        sys.stdout.write('1\n' if S & (1 << x) else '0\n')
    elif op == 'toggle':
        S ^= (1 << x)
    elif op == 'all':
        S = ALL
    elif op == 'empty':
        S = 0
