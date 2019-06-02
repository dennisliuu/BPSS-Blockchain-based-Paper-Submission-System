import os
import time
import pymongo

connect = pymongo.MongoClient("mongodb://localhost:8080")
db = connect.paper
download = db.blocks

def reader():
    path = 'D:\\BPSS\\public\\upload\\'
    entries = os.listdir(path=path)
    cutPath = []
    pathRecord = []
    newpathRecord = []
    emailAddress = []
    for entry in entries:
        temp = []
        temp.append(path)
        temp.append(entry)
        newpath = ''.join(temp)
        pathRecord.append(newpath)
    for path in pathRecord:
        entries = os.listdir(path=path)
        for entry in entries:
            cutPath.append(path)
            temp = []
            temp.append(path)
            temp.append('\\')
            temp.append(entry)
            newpath = ''.join(temp)
            newpathRecord.append(newpath)
            todayDate = time.strftime("%Y-%m-%d", time.localtime())
            allPaper = download.find({"$and": [{"date": todayDate}, {"filename": entry}]})
            paper = [p for p in allPaper]
            paperQuantity = len(paper)
            for i in range(paperQuantity):
                emailAddress.append(paper[i]['email'])
    return cutPath, newpathRecord, emailAddress