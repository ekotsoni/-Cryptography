def reverse_element(element,alphabet):

    for x in range(alphabet):
        if (((element*x)%alphabet) == (1%alphabet)): elementT = x
    return elementT

def decode():

    englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
    max_element = sorted(englishLetterFreq, key=lambda k: englishLetterFreq[k], reverse=True)

    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    text = open('1st_msg.txt','r')

    dictionary = {}
    c = []
    for i in text.read():
        c.append(i)
        if ((i != '\n') & (i != ' ') & (i != '.' ) & (i != '\'') & (i != ',')):
            dictionary[i] = dictionary.get(i,0) + 1
    #for k,v in dictionary.items():
    #    print("{}: {}".format(k,v))

    classification = sorted(dictionary, key=lambda k: dictionary[k], reverse=True)

    for index,i in enumerate(alphabet):
        if max_element[0] == i:
            p1 = index
        if max_element[1] == i:
            p2 = index
        if classification[0] == i:
            c1 = index
        if classification[1] == i:
            c2 = index

    D = p1-p2
    if D < 0: D = (len(alphabet)+D) % len(alphabet)
    DT = reverse_element(D,len(alphabet))

    a = DT*(c1-c2) % len(alphabet)
    b = (c1-a*p1) % len(alphabet)
    print 'Key is (', a, ',', b, ').'

    aT = reverse_element(a,len(alphabet))

    text = open('1st_msg.txt','r')
    p = []
    for i in text.read():
        if i in dictionary.keys():
            for index,j in enumerate(alphabet):
                if (i == j):
                    cryptogramma = index
                    break
            msg = (aT*(cryptogramma-b)) % len(alphabet)
            for index,k in enumerate(alphabet):
                if (msg == index):
                    message = index
        else:
            message = i
        p.append(message)

    letteroftext = []
    for index1,i in enumerate(p):
        if ((i != '\n') & (i != ' ') & (i != '.' ) & (i != '\'') & (i != ',')):
            for index2,j in enumerate(alphabet):
                if (index2 == i):
                    lt = j
                    break
        else:
            lt = i
        letteroftext.append(lt)

    text_file = open('decryption1.txt','w')
    for index,i in enumerate(letteroftext):
        text_file.write(i)
    text_file.close()

if __name__ == '__main__':
    decode()
