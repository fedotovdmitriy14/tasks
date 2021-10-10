from itertools import permutations
import math


routes = [(2, 5), (5, 2), (6, 6), (8, 3)]

def postman_routes(routes):
    perm = permutations(routes)     # разбил список с координатами на все возможные вариации, чтобы потом пройтись по ним в цикле
    result = {}

    for route in list(perm):
        counter = 1
        total_length = 0
        i = 0
        current_route = ""
        while True:
            if counter == 1:
                length = math.sqrt((route[i][0] - 0) ** 2 + (route[i][1] - 2) ** 2)
                total_length += length
                current_route += f"(0, 1) -> {(route[i][0], route[i][1])}[{total_length}]"
                counter += 1
                i += 1
            elif i < len(route):
                length = math.sqrt((route[i][0] - route[i-1][0]) ** 2 + (route[i][1] - route[i-1][1]) ** 2)
                total_length += length
                current_route += f" -> {(route[i][0], route[i][1])}[{total_length}]"
                counter += 1
                i += 1
            else:
                i = len(route) - 1
                length = math.sqrt((0 - route[i][0]) ** 2 + (2 - route[i][1]) ** 2)
                total_length += length
                current_route += f" -> {(0, 1)}[{total_length}]"
                counter += 1
                break
        # print(current_route)
        result[total_length] = current_route


    min_key = min(result, key=int)


    return f"{result[min_key]} = {min_key}"

print(postman_routes(routes))