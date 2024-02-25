def solution(topping):
    start = 1
    end = len(topping) - 2
    min_temp = -1
    while start <= end:
        mid = (start + end) // 2
        left = len(set(topping[:mid+1]))
        right = len(set(topping[mid+1:]))
        if left == right:
            min_temp = mid
            end = mid - 1
        elif left < right:
            start = mid + 1
        else:
            end = mid - 1
            
    start = 1
    end = len(topping) - 2
    max_temp = -1
    while start <= end:
        mid = (start + end) // 2
        left = len(set(topping[:mid+1]))
        right = len(set(topping[mid+1:]))
        if left == right:
            max_temp = mid
            start = mid + 1
        elif left < right:
            start = mid + 1
        else:
            end = mid - 1
            
    if min_temp == -1 or max_temp == -1:
        return 0
    else:
        return max_temp - min_temp + 1

"""
def solution(topping):
    answer = 0
    topp_cnt = len(set(topping))
    chulsu_li = [[0 for x in range(topp_cnt)] for x in range(len(topping)-1)]
    bro_li = [[0 for x in range(topp_cnt)] for x in range(len(topping)-1)]
    
    for idx in range(len(topping)-1):
        chulsu_li[idx][topping[idx]-1] += 1
        if idx != 0:
            chulsu_li[idx] = [x + y for x, y in zip(chulsu_li[idx], chulsu_li[idx-1])]
            
    for bro_idx, topp_idx in zip(range(len(topping)-2, -1, -1), range(len(topping)-1, 0, -1)):
        bro_li[bro_idx][topping[topp_idx]-1] += 1
        if bro_idx != (len(topping)-2):
            bro_li[bro_idx] = [x + y for x, y in zip(bro_li[bro_idx], bro_li[bro_idx+1])]
            
    for chulsu, bro in zip(chulsu_li, bro_li):
      chulsu_cnt = 0
      bro_cnt = 0
      for e in chulsu:
        if e != 0:
          chulsu_cnt += 1
      for e in bro:
        if e != 0:
          bro_cnt += 1
      if chulsu_cnt == bro_cnt:
        answer += 1
        
    return answer
"""
