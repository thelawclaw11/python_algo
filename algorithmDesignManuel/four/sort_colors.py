def sort_colors(array):
    blues = []
    reds = []
    yellows = []

    for item in array:
        number, color = item
        if color == "blue":
            blues.append(item)
        elif color == "red":
            reds.append(item)
        elif color == "yellow":
            yellows.append(item)

    return reds + blues + yellows



print(sort_colors([(1,"blue"), (3,"red"), (4, "blue"), (6,"yellow"), (9, "red")]))