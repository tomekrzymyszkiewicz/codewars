def move(m, pos):
    if m[pos[0]][pos[1]] == 'f':
        return True, pos
    elif m[pos[0]][pos[1]] == 'r':
        pos[1] += 1
    elif m[pos[0]][pos[1]] == 'l':
        pos[1] -= 1
    elif m[pos[0]][pos[1]] == 'd':
        pos[0] += 1
    elif m[pos[0]][pos[1]] == 'u':
        pos[0] -= 1
    pos[0] %= len(m)
    if len(m) != 0:
        pos[1] %= len(m[pos[0]])
    return False, [pos[0],pos[1]]


def path_counter(m):
    paths = [[0 for col in row] for row in m]
    for row in range(len(paths)):
        for col in range(len(paths[row])):
            if paths[row][col] == 0:
                current_pos = [row, col]
                visited = []
                while current_pos[0] < len(paths) and current_pos[1] < len(paths[row]) and len(current_pos) == 2:
                    move_res = move(m, current_pos)
                    if move_res[0]:
                        paths[row][col] = len(visited)
                        for i, visited_point in enumerate(visited, 1):
                            paths[visited_point[0]][visited_point[1]] = len(
                                visited)-i
                        break
                    elif move_res[1] in visited:
                        paths[row][col] = -1
                        for visited_point in visited:
                            paths[visited_point[0]][visited_point[1]] = -1
                        break
                    else:
                        visited.append(current_pos.copy())
                        current_pos = move_res[1]
    return paths
