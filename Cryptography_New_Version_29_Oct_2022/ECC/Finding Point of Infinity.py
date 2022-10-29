
# given a coordinate P(5,1)

P = [5,1]
a = 2
b = 2


s = ((3*(P[0]**2) + a)/(2*P[1])) % 17

print(s)

x = (s**2 - P[0] - P[0]) % 17

print(x)

y = (s*(P[0] - x) - P[1]) % 17

print(x,y)


