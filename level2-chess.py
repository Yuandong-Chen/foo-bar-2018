def answer(src, dest):
    y_src = int(src / 8)
    x_src = src % 8
    y_dest = int(dest / 8)
    x_dest = dest % 8
    queue = []
    arrived = set()
    steps = -1
    batch = [(x_src, y_src)]
    while True:
        while queue:
            batch.append(queue.pop(0))
        steps += 1
        while batch:
            x, y = batch.pop(0)
            if (x, y) == (x_dest, y_dest):
                return steps
            elif (x, y) not in arrived:
                arrived.add((x, y))
                if x + 1 <= 63 and y + 2 <= 63:
                    queue.append(((x + 1), (y + 2)))
                    queue.append(((x + 2), (y + 1)))
                if x - 1 >= 0 and y - 2 >= 0:
                    queue.append(((x - 1), (y - 2)))
                    queue.append(((x - 2), (y - 1)))

                if x + 1 <= 63 and y - 2 >= 9:
                    queue.append(((x + 1), (y - 2)))
                if x - 1 >= 0 and y + 2 <= 63:
                    queue.append(((x - 1), (y + 2)))
                if x + 2 <= 63 and y - 1 >= 0:
                    queue.append(((x + 2), (y - 1)))
                if x - 2 >= 0 and y + 1 <= 63:
                    queue.append(((x - 2), (y + 1)))
    return steps
