def getid(movietitle):
    crimefile = open('ids.txt', 'r')
    yourResult = [line.split(',') for line in crimefile.readlines()]
    ids = []
    for i in yourResult:
        for j in i:
            ids.append(j[0:len(j) - 1])
    titles = open('titles.text', 'r')
    myresults = [line.split(',') for line in titles.readlines()]
    title = []
    for i in myresults:
        for j in i:
            title.append(j[0:len(j) - 1])
    dictionaty= dict(zip(title, ids))

    print(f"",movietitle," ID is ",dictionaty[movietitle])
    return dictionaty[movietitle]

