#! Python 3.6.2
import os
from struct import unpack
import binascii
from binascii import b2a_hex
inFileName = r"fullyQualifiedFileName for infile"
dumpfileName = r"fullyQualifiedFileName for dump file"
infile = open(inFileName,"rb")
dumpfile = open(dumpfileName,"w")

while True:
    read_RL_RT = infile.read(8)
    if len(read_RL_RT)==0:
        break
    rl,rt = unpack(">II",read_RL_RT)
    dumpfile.write("{},{}".format(rl,rt))
    for index in range(int(rl/4)):
        hexVal = infile.read(4).hex()
        dumpfile.write(",0x"+ hexVal)        
    dumpfile.write("\n")
dumpfile.close()
