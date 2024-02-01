def category(dict, type):
    list = []
    for i in range(len(dict)):
        if dict[i]["category"] == type:
            list.append(dict[i]["name"])

    print(list)