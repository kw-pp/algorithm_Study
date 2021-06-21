def solution(genres, plays): 
    answer = [] 
    genre_total_play = {} 
    genre_dic = {} 
    
    for i in range(len(genres)): 
        if genres[i] not in genre_dic.keys(): 
            genre_dic[genres[i]] = [(plays[i], i)] 
            genre_total_play[genres[i]] = plays[i] 
        else: 
            genre_dic[genres[i]].append((plays[i], i)) 
            genre_total_play[genres[i]] += plays[i] 
    # genre_dic = {"classic":[(500,0),(150,2),(800,3)], "pop":[(600,1),(2500,4)]}
    # genre_total_play = {"classic":1450, "pop":3100}
    
    sorted_total_play = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True) 
    # sorted_total_play = {("pop":3100), ("classic":1450)}
        
    for key in sorted_total_play: 
        play_list = genre_dic[key[0]] 
        # 장르 내 재생 횟수 많은 노래 순 정렬
        # 재생 횟수가 같은 노래는 고유 번호가 낮은 순
        play_list = sorted(play_list, key = lambda x : (-x[0], x[1])) 
        # play_list = [(2500,4), (600,1)]
            
        for i in range(len(play_list)): 
            if i == 2: 
                break 
            answer.append(play_list[i][1]) 
    return answer