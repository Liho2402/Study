def avarage_by_category(dict, type):
    avarage = 0
    cnt = 0
    for i in range(len(dict)):
        if dict[i]["category"] == type:
            cnt += 1
            avarage += dict[i]["imdb"]
    
    avarage /= cnt
    print(round(avarage, 2))