ys = [1,2,3,4,5]
xs = [1,2,3,4,5]

out = []
for x in xs:
    for y in ys:
        if (x * y) % 6 == 1:
            out.append({"x": x,"y": y})
print(out)

