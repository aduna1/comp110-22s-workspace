phrase: str = "the brown, lazy dog!"
print(str(phrase[0] + phrase[12] + phrase[5]))


a: str = "a"
b: str = "a" + "c"
print(b + a)
b = b + "b"
a = a + b[len(a) + 1]
print(a[0])
print(a[1])
print(a)