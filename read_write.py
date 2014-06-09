import sys
from datetime import datetime
from time import sleep

# exit if no args are given
if (len(sys.argv) != 2):
    print 'Usage: python %s filename' % __file__
    sys.exit()
filename = sys.argv[1]

# write datetime
with open(filename, 'w') as f:
    for i in range(3):
        data = 'Write: ' + str(datetime.now())
        f.write(data + '\n')
        sleep(0.1)

# read recorded datetime
with open(filename, 'r') as f:
    for line in f:
        # remove white spaces and newlines at the beginning and end
        data = line.strip()
        # extract a substring from position 7
        data = data[7:]
        print data
