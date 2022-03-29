import sys
def get_test_set(argv):
    fin = open(argv[1], 'r')
    fout = open(argv[2], 'w')
    line = fin.readline()
    while(line != ''):
        if(line.startswith("READ") or line.startswith('INSERT') or line.startswith('SCAN') or line.startswith('UPDATE')):
            fout.write(line)
        line = fin.readline()


if __name__ == '__main__':
    if(len(sys.argv)<3):
        print('Usage:')
        print('python GetTestSet.py input_file output_file')
        sys.exit()
    get_test_set(sys.argv) 