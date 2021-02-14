V, T, S, D = [int(_) for _ in input().split()]

print('No' if (D >= V * T and D <= V * S) else 'Yes')