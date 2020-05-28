import math

xi = []
i = 0
while i <= math.pi/2:
    xi.append(i)
    i += 0.1
yi = [math.sin(i) for i in xi]
