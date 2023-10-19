a = [0,2,1,0,1,2]
notordered = list(set(a))
ordered = []
for i in range(a):
    if i not in ordered:
        ordered.append(i)
print(sorted(a+b))  ``