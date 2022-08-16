from collections import defaultdict


def light_up(graph, light):
    max_lighthouse = 0
    for key in graph.keys():
        if len(graph[key]) > max_lighthouse and key not in light:
            max_lighthouse = len(graph[key])
            max_key = key
    light.append(max_key)
    light.extend(graph[max_key])
    return light


def check_safe(key_list, light):
    for key in key_list:
        if key not in light:
            return False
    return True


def solution(n, lighthouse):
    answer = 0
    light = []
    graph = defaultdict(list)

    for i in lighthouse:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    while not check_safe(graph.keys(), light):
        light = light_up(graph, light)
        answer += 1
    return answer
