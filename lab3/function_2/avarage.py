def overall_avarage_imdb(dict):
    avarage = 0
    for i in range(len(dict)):
        avarage += dict[i]["imdb"]
    
    avarage /= len(dict)
    print(round(avarage, 2))