import math

a, b, d = map(int, input().split())

a_1 = math.cos(math.radians(d)) * a - math.sin(math.radians(d)) * b
b_1 = math.sin(math.radians(d)) * a + math.cos(math.radians(d)) * b

print(f'{a_1} {b_1}')