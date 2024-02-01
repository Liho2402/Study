def imdb_sort(dict):
    # list = []
    for i in range(len(dict)):
        if dict[i]["imdb"] >= 5.5:
            # list.append("True")
            return True
        else:
            # list.append("False")
            return False
    # print(list)