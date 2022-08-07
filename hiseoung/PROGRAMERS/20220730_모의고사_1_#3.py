def solution(order):
    sub_list = []
    result = []
    obj_list = sorted([i for i in range(1, len(order) + 1)], reverse=True)
    idx = 0
    check = 0

    while obj_list or sub_list:

        # 컨테이너 벨트와 일치 여부 확인
        if obj_list:
            if obj_list[-1] == order[idx]:
                result.append(obj_list.pop())
                idx += 1

                if sub_list:
                    if 0 <= idx < len(order):
                        if obj_list and sub_list:
                            if obj_list[-1] != order[idx] and sub_list[-1] != order[idx]:
                                break

            else:
                sub_list.append(obj_list.pop())

        if sub_list:
            if sub_list[-1] == order[idx]:
                result.append(sub_list.pop())
                idx += 1

                if sub_list:
                    if 0 <= idx < len(order):
                        if obj_list and sub_list:
                            if obj_list[-1] != order[idx] and sub_list[-1] != order[idx]:
                                break
    return len(result)