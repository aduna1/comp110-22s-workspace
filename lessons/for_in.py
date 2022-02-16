"""An example of for in syntax."""

names: list[str] = ["Adun", "Femi", "Ife", "Nerrissa"]

#  Example of interating through names using a while loop

i: int = 0
print("while output")
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for..in output")
#  The following for...in loop is the same as the while loop above
for name in names:
    print(name)