Dict = {'$INSERT':('$INCLUDE'),
'OPEN':('OPF'),
'READ':('F.READ','CACHE.READ'),
'F.READ':('CACHE.READ')
}

global s, w

def file_to_code_convertion():
    indexes = []
    with open('original_code.txt') as f:
        lines = f.readlines()

    for row, line in enumerate(lines, 1):
        print('Before', line)
        words = line.split(' ')
        for i in range(len(words)):
            if words[i] in Dict.keys():
                words[i] = Dict[words[i]]
                w = words[i]
                print('Changed:', words[i])
                #print('Line', line)
                if type(words[i]) == tuple:
                    print("Tuple",list(enumerate(words[i])))
                    value_to_insert = int(input("Enter the number to insert the value:"))
                    for value_to_insert, obj in enumerate(words[i]):
                        words[i] = obj
                        w = words[i]
                    #print('Line', line)



        s = ' '
        with open('converted_code.txt','a+') as F:
            sentence = s.join(words)
            F.write(sentence)
            print("Final", sentence)
            #print('Row', row)
            #print('String Start', sentence.find(w))
            #print('String End', int(sentence.find(w)) + len(w))
            if sentence.find(w) != -1:
                start = '{0}.{1}'.format(row, sentence.find(w))
                end = '{0}.{1}'.format(row, int(sentence.find(w)) + len(w))
                start_end_index = tuple([start, end])
                print(indexes.append(start_end_index))
            print('---------------------------')
    print("Final Changed Indexes:", indexes)
    return indexes




def new_code():
    with open('converted_code.txt','r') as read_code:
        code = read_code.read()
    return code
