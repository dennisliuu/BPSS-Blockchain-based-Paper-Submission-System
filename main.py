import multifileReader
import pdfReader
import sendMail
import Blockchain

def main():
    pathCut, filepaths, emailAddress = multifileReader.reader()
    for i in range(len(filepaths)):
        data = pdfReader.pdfReader(path=filepaths[i])
        processResult, hashRecord, sentenceNumber = pdfReader.paperProcessing(path=filepaths[i], data=data, cut=pathCut[i])
        if processResult == 1:
            merkleRoots = Blockchain.merkleTree(data=data, sentenceNumber=sentenceNumber)
            Blockchain.test_code(merkleRoots)
            sendMail.sendMail_successfully(emailAddress[i])
        else:
            sendMail.sendMail_unsuccessfully(emailAddress[i])
main()