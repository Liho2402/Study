def sort_films(dict):
    list = []
    for i in range(len(dict)):
        if dict[i]["imdb"] >= 5.5:
            list.append(dict[i]["name"])
    print(list)