# 생각을 더해봅시다...(아직 푸는중)
bridge_length=2
weight=10
truck_weights=[7,4,5,6]

time = 0
complete = []
moving = []
m = len(truck_weights)

while len(complete) != m:

    if len(moving) != 0:
        w_sum = sum(moving)
    else:
        w_sum = 0

    if len(truck_weights) != 0:
        while sum(moving) < weight:
            x = truck_weights.pop(0)
            moving.append(x)

    y = moving.pop(0)
    complete.append(y)

    if len(moving) == 0:
        time += bridge_length
    else:
        time += 1

print(time)