#Date: 18/5/2021
#Author: or yanko

def lstToStr(list):
    s = ""
    for i in list:
        s += chr(i % 95 + 32)
    return s

def hash(some_text):
    #dont deal with new lines
    some_text = some_text.replace("\n", " ")

    #split the str to list of ascii values list from the str (every list length is 256 chars)
    strAsciiList = []
    listOfAsciiLists = []
    i = 0
    for ch in some_text:
        if i < 256:
            i += 1
            strAsciiList.append(ord(ch))
        else:
            listOfAsciiLists.append(strAsciiList)
            strAsciiList = []
            i = 0
    listOfAsciiLists.append(strAsciiList)

    #fill last list
    if len(listOfAsciiLists) == 1:
        i = 0
        while len(listOfAsciiLists[0]) != 256:
            listOfAsciiLists[0].append(listOfAsciiLists[0][i])
            i += 1
    elif len(listOfAsciiLists) != 0:
        while len(listOfAsciiLists[-1]) != 256:
            lst = listOfAsciiLists[len(listOfAsciiLists[-1])//i]
            listOfAsciiLists[-1].append(lst[len(listOfAsciiLists[-1])//3])
            i = len(strAsciiList)


    #merge all the lists to list of integers
    listOf265 = listOfAsciiLists[0]
    addList = listOfAsciiLists[0]

    if len(listOfAsciiLists) > 1:
        for i in range(1, len(listOfAsciiLists)):
            for n in range(0, 256):
                placeInFinal = n
                if i % 2 == 0:
                    placeInLstOfLst = 255 - n
                else:
                    placeInLstOfLst = n
                if i % 3 == 0:
                    listOf265[placeInFinal] = listOf265[placeInFinal] & (listOfAsciiLists[i])[placeInLstOfLst]
                elif i % 3 == 1:
                    listOf265[placeInFinal] = listOf265[placeInFinal] ^ (listOfAsciiLists[i])[placeInLstOfLst]
                else:
                    listOf265[placeInFinal] = listOf265[placeInFinal] | (listOfAsciiLists[i])[placeInLstOfLst]
                addList[placeInFinal] += (listOfAsciiLists[i])[placeInLstOfLst]
        for n in range(0, 256):
            if listOf265[n] % 4 == 0:
                listOf265[n] = (listOf265[n] + addList[255-n] ^ (listOfAsciiLists[1][addList[n] % 240])) % 150
            elif listOf265[n] % 4 == 1:
                listOf265[n] = (listOf265[n] ^ addList[255-n]) % 150
            elif listOf265[n] % 4 == 2:
                listOf265[n] = (listOf265[n] & addList[255-n]) % 150
            else:
                listOf265[n] = (listOf265[n] | addList[255-n]) % 150

    for i in range(0, 256):
        listOf265[i] = (listOf265[i] % 100) * (listOf265[listOf265[i*13 % 256] % 255] % 100 + listOf265[i]) % 231
    return lstToStr(listOf265)

print(hash("hello world!"))