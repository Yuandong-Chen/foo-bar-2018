def answer(maze):
    width = len(maze[0])
    height = len(maze)
    x_src = 0
    y_src = 0
    y_dest = height - 1
    x_dest = width - 1
    queue = []
    arrived = set()
    steps = 0
    batch = [(x_src, y_src, 0)]
    while True:
        while queue:
            batch.append(queue.pop(0))
        steps += 1
        while batch:
            x, y, wall = batch.pop(0)
            if (x, y) == (x_dest, y_dest):
                return steps
            elif (x, y, wall) not in arrived:
                arrived.add((x, y, wall))
                if y + 1 < height:
                    if not maze[y + 1][x]:
                        queue.append((x, (y + 1), wall))
                    elif wall == 0:
                        queue.append((x, (y + 1), wall + 1))
                if x + 1 < width:
                    if not maze[y][x + 1]:
                        queue.append(((x + 1), y, wall))
                    elif wall == 0:
                        queue.append(((x + 1), y, wall + 1))
                if y - 1 >= 0:
                    if not maze[y - 1][x]:
                        queue.append((x, (y - 1), wall))
                    elif wall == 0:
                        queue.append((x, (y - 1), wall + 1))
                if x - 1 >= 0:
                    if not maze[y][x - 1]:
                        queue.append(((x - 1), y, wall))
                    elif wall == 0:
                        queue.append(((x - 1), y, wall + 1))
    return steps
