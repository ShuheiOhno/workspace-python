data = [1, 2, 3, 4, 5]
m, n, *o = data
print(m)
print(n)
print(o) #[3,4,5]

r, *s, t = data
print(r)
print(s) #[2, 3,4]
print(t)