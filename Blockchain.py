from datetime import datetime
import hashlib
import pymongo

connect = pymongo.MongoClient("mongodb://localhost:8080")
db = connect.paper
collection = db.blockchain

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return 'Block #{}'.format(self.index)

    def hash_block(self):
        sha = hashlib.sha256()
        seq = (str(x) for x in (
               self.index, self.timestamp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()

def make_genesis_block():
    """Make the first block in a block-chain."""
    block = Block(index=0,
                  timestamp=datetime.now(),
                  data="Genesis Block",
                  previous_hash="0")
    return block

def next_block(last_block, data=''):
    """Return next block in a block chain."""
    idx = last_block.index + 1
    block = Block(index=idx,
                  timestamp=datetime.now(),
                  data='{}{}'.format(data, idx),
                  previous_hash=last_block.hash)
    return block

def merkleTree(data, sentenceNumber):
    blockNumber = sentenceNumber // 8
    if blockNumber == 0:
        blockNumber += 1
    remain = sentenceNumber % 8
    firstState = []
    secondState = []
    thirdState = []
    forthState = []
    temp = []
    merkleRoots = []
    if remain == 0:
        for root in range(blockNumber):
            for firstleave in range(8):
                hash = hashlib.sha256(str(data[root*8+firstleave]).encode('utf-8')).hexdigest()
                firstState.append(hash)
            for secondleave in range(0, 7, 2):
                temp.append(firstState[secondleave])
                temp.append(firstState[secondleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                secondState.append(hash)
            for thirdleave in range(0, 4, 2):
                temp.append(secondState[thirdleave])
                temp.append(secondState[thirdleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                thirdState.append(hash)
            for forthleave in range(0, 2, 2):
                temp.append(thirdState[forthleave])
                temp.append(thirdState[forthleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                forthState.append(hash)
            merkleRoots.append(forthState)
    elif remain == 1:
        for root in range(blockNumber):
            for firstleave in range(remain):
                hash = hashlib.sha256(str(data[root * 8 + firstleave]).encode('utf-8')).hexdigest()
                firstState.append(hash)
            merkleRoots.append(firstState)
    elif remain == 2:
        for root in range(blockNumber):
            for firstleave in range(remain):
                hash = hashlib.sha256(str(data[root * 8 + firstleave]).encode('utf-8')).hexdigest()
                firstState.append(hash)
            for secondleave in range(1):
                temp.append(firstState[secondleave])
                temp.append(firstState[secondleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                secondState.append(hash)
            merkleRoots.append(secondState)
    elif remain == 3:
        for root in range(blockNumber):
            for firstleave in range(remain):
                hash = hashlib.sha256(str(data[root * 8 + firstleave]).encode('utf-8')).hexdigest()
                firstState.append(hash)
            for secondleave in range(1):
                temp.append(firstState[secondleave])
                temp.append(firstState[secondleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                secondState.append(hash)
            hashprime = hashlib.sha256(str(firstState[2]).encode('utf-8')).hexdigest()
            secondState.append(hashprime)
            for thirdleave in range(1):
                temp.append(secondState[thirdleave])
                temp.append(secondState[thirdleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                thirdState.append(hash)
            merkleRoots.append(thirdState)
    elif remain == 4:
        for root in range(blockNumber):
            for firstleave in range(remain):
                hash = hashlib.sha256(str(data[root * 8 + firstleave]).encode('utf-8')).hexdigest()
                firstState.append(hash)
            for secondleave in range(0, 3, 2):
                temp.append(firstState[secondleave])
                temp.append(firstState[secondleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                secondState.append(hash)
            for thirdleave in range(1):
                temp.append(secondState[thirdleave])
                temp.append(secondState[thirdleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                thirdState.append(hash)
            merkleRoots.append(thirdState)
    elif remain == 5:
        for root in range(blockNumber):
            for firstleave in range(remain):
                hash = hashlib.sha256(str(data[root * 8 + firstleave]).encode('utf-8')).hexdigest()
                firstState.append(hash)
            for secondleave in range(0, 3, 2):
                temp.append(firstState[secondleave])
                temp.append(firstState[secondleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                secondState.append(hash)
            hashprime = hashlib.sha256(str(firstState[4]).encode('utf-8')).hexdigest()
            secondState.append(hashprime)
            for thirdleave in range(1):
                temp.append(secondState[thirdleave])
                temp.append(secondState[thirdleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                thirdState.append(hash)
            hashprime = hashlib.sha256(str(secondState[2]).encode('utf-8')).hexdigest()
            thirdState.append(hashprime)
            for forthleave in range(0, 2, 2):
                temp.append(thirdState[forthleave])
                temp.append(thirdState[forthleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                forthState.append(hash)
            merkleRoots.append(forthState)
    elif remain == 6:
        for root in range(blockNumber):
            for firstleave in range(remain):
                hash = hashlib.sha256(str(data[root * 8 + firstleave]).encode('utf-8')).hexdigest()
                firstState.append(hash)
            for secondleave in range(0, 5, 2):
                temp.append(firstState[secondleave])
                temp.append(firstState[secondleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                secondState.append(hash)
            for thirdleave in range(1):
                temp.append(secondState[thirdleave])
                temp.append(secondState[thirdleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                thirdState.append(hash)
            hashprime = hashlib.sha256(str(secondState[2]).encode('utf-8')).hexdigest()
            thirdState.append(hashprime)
            for forthleave in range(0, 2, 2):
                temp.append(thirdState[forthleave])
                temp.append(thirdState[forthleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                forthState.append(hash)
            merkleRoots.append(forthState)
    elif remain == 7:
        for root in range(blockNumber):
            for firstleave in range(remain):
                hash = hashlib.sha256(str(data[root * 8 + firstleave]).encode('utf-8')).hexdigest()
                firstState.append(hash)
            for secondleave in range(0, 5, 2):
                temp.append(firstState[secondleave])
                temp.append(firstState[secondleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                secondState.append(hash)
            hashprime = hashlib.sha256(str(firstState[6]).encode('utf-8')).hexdigest()
            secondState.append(hashprime)
            for thirdleave in range(0, 4, 2):
                temp.append(secondState[thirdleave])
                temp.append(secondState[thirdleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                thirdState.append(hash)
            for forthleave in range(0, 2, 2):
                temp.append(thirdState[forthleave])
                temp.append(thirdState[forthleave + 1])
                record = ''.join(temp)
                temp = []
                hash = hashlib.sha256(str(record).encode('utf-8')).hexdigest()
                forthState.append(hash)
            merkleRoots.append(forthState)
    return merkleRoots

def getBlockNumber():
    sortedData = collection.find().sort("_id", pymongo.DESCENDING)
    data = [b for b in sortedData]
    blockNumber = len(data)
    return blockNumber

def getPreviousBlock(blockNumber):
    pre = []
    pre.append('D:\\BPSS\\blockchain\\')
    pre.append('Block #')
    pre.append(str(blockNumber))
    pre.append('.txt')
    openfile = ''.join(pre)
    file = open(openfile)
    preprime = []
    previousData = []
    for data in file:
        preprime.append(data)
    previousData.append(preprime[0][0:9])
    previousData.append(preprime[1][6:70])
    previousData.append(preprime[2][11:])
    preprevious = []
    preprevious.append('D:\\BPSS\\blockchain\\')
    preprevious.append('Block #')
    preprevious.append(str(blockNumber - 1))
    preprevious.append('.txt')
    openfile = ''.join(preprevious)
    file = open(openfile)
    prepreprime = []
    prepreviousData = []
    for data in file:
        prepreprime.append(data)
    prepreviousData.append(prepreprime[0][0:9])
    prepreviousData.append(prepreprime[1][6:70])
    prepreviousData.append(prepreprime[2][11:])
    return blockNumber, previousData[2], previousData[1], prepreviousData[1]

def test_code(data):
    blockNumber = getBlockNumber()
    if blockNumber == 0:
        blockchain = [make_genesis_block()]
        prev_block = blockchain[0]
        for i in data:
            block = next_block(prev_block, data=i)
            blockchain.append(block)
            prev_block = block
            collection.insert_one({'id': format(block), 'Timestamp': datetime.now(), 'Hash': format(block.hash)})
            file = open('D:\\BPSS\\blockchain\\{}.txt'.format(block), 'x')
            file = open('D:\\BPSS\\blockchain\\{}.txt'.format(block), 'w')
            file.writelines(['{}'.format(block), '\n', 'Hash: {}'.format(block.hash), '\n', 'Timestamp: {}'.format(datetime.now())])
            print('{} added to blockchain'.format(block))
            print('Hash: {}'.format(block.hash))
            print('Timestamp: {}\n'.format(datetime.now()))
    else:
        index, timeStamp, preData, previousHash = getPreviousBlock(blockNumber)
        blockchain = [Block(index=index, timestamp=timeStamp, data=preData, previous_hash=previousHash)]
        prev_block = blockchain[0]
        for i in data:
            block = next_block(prev_block, data=i)
            blockchain.append(block)
            prev_block = block
            collection.insert_one({'id': format(block), 'Timestamp': datetime.now(), 'Hash': format(block.hash)})
            file = open('D:\\BPSS\\blockchain\\{}.txt'.format(block), 'x')
            file = open('D:\\BPSS\\blockchain\\{}.txt'.format(block), 'w')
            file.writelines(['{}'.format(block), '\n', 'Hash: {}'.format(block.hash), '\n', 'Timestamp: {}'.format(datetime.now())])
            print('{} added to blockchain'.format(block))
            print('Hash: {}'.format(block.hash))
            print('Timestamp: {}\n'.format(datetime.now()))