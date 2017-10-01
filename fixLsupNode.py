"""Currently lsup.node is written incorrectly. Each line containing information
about a vertex is supposed to be written as '<vertex #> <x coord> <y coord>' but
our lsup.node is only written as '<x coord> <y coord>'"""

ifile = open('lsup.node', 'r')
ofile = open('lsup/lsup.node', 'w')
ofile.write(ifile.readline())
counter = 0
for line in ifile:
    ofile.write(str(counter) + ' ' + line)
    counter += 1

ifile.close()
ofile.close()
