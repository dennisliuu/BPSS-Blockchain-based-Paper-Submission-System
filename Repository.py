import hashlib
import pymongo
import RegularExpression as RE
import time

connect = pymongo.MongoClient("mongodb://localhost:8080")
db = connect.paper
download = db.blocks
update = db.repository

def Download():
    todayDate = '2019-07-12'  # todayDate = time.strftime("%Y-%m-%d", time.localtime())
    allPaper = download.find({"date": todayDate})
    data = [p for p in allPaper]
    paperQuantity = len(data)
    for i in range(paperQuantity):
        print('data{}: '.format(i), data[i])
    print('paperQuantity: ', paperQuantity)

def paperProcessing(path):
    #read file and splitted by Regular Expression
    f = open(path, "r")
    split_txt = RE.splitIntoSentences(f.read())
    name_build = f.name.split('D:\\BPSS\\public\\upload\\')
    del name_build[0]

    plagiarismCount = 0
    hash_append = []
    content_append = []
    sentenceNumber = len(split_txt)

    #hash, get plagiarism
    for data in split_txt:
        hash = hashlib.sha256(str(data).encode('utf-8')).hexdigest()
        content_append.append(data)
        hash_append.append(hash)
        print("Sentence: ", data)
        print("Hash: {}".format(hash))
        content_pointer = update.find_one({'Hash': hash})
        if content_pointer != None:
            content_pointer_hash = content_pointer.get('Hash')
            if content_pointer_hash == hash:
                print("WARNING!!! DATA ALREADY EXISTS!!!\n", content_pointer, "\n")
                plagiarismCount += 1
        else:
            print("Data doesn't exist!\n\n")

    #get allhash combination's hash
    allhash_combination = ''.join(hash_append)
    allhash_combination_hash = hashlib.sha256(str(allhash_combination).encode('utf-8')).hexdigest()
    hash_pointer = update.find_one({'Hash': allhash_combination_hash})

    threshold = 0.3
    repetitionRate = float(plagiarismCount / sentenceNumber)

    if (hash_pointer != None):
        hash_pointer_hash = hash_pointer.get('Hash')
        if (hash_pointer_hash == allhash_combination_hash):
            print("All Hash combination is %s" % (allhash_combination))
            print("Hash: {}".format(allhash_combination_hash))
            print("WARNING!!! THIS PAPER ALREADY EXISTS!!!\n", hash_pointer, "\n")
    else:
        print("All Hash combination is %s" % (allhash_combination))
        print("Hash: {}".format(allhash_combination_hash))
        print("Data doesn't exist!\n\n")
        print("There are %d sentences in %s" % (sentenceNumber, name_build))
        if repetitionRate < threshold:
            if plagiarismCount > 1:
                print("According to your paper, there are %d same sentences in Database." % plagiarismCount)
            elif plagiarismCount == 1:
                print("According to your paper, there is 1 same sentence in Database.")
            elif plagiarismCount == 0:
                print("According to your paper, there're not any same sentences in Database.")
            print("Repetition rate is %.3f. It is smaller than threshold =  %.2f. Successful processing!" % (repetitionRate, threshold))
            for i in range(sentenceNumber):
                date = time.strftime("%Y-%m-%d", time.localtime())
                daytime = time.strftime("%H:%M:%S", time.localtime())
                update.insert_one({'Date': date, 'Time': daytime, 'Title': name_build, 'Sentence': content_append[i], 'Hash': hash_append[i]})
            print("Paper doesn't exist! Successful processing!")
            date = time.strftime("%Y/%m/%d", time.localtime())
            daytime = time.strftime("%H:%M:%S", time.localtime())
            update.insert_one({'Date': date, 'Time': daytime, 'Title': name_build, 'Sentence': allhash_combination, 'Hash': allhash_combination_hash})
        else:
            print("According to your paper, there are %d same sentences in Database." % plagiarismCount)
            print("Repetition rate is %.3f. It is larger than threshold = %.2f. The process is rejected!\n" % (repetitionRate, threshold))