import socket
import random
import time
import sys
from daqhats import hat_list, HatIDs, mcc118
def read_value():
    board_list = hat_list(filter_by_id = HatIDs.ANY)
    if not board_list:
        print("No boards found")
        sys.exit()
    for entry in board_list:
        if entry.id == HatIDs.MCC_118:
            print("Board {}: MCC 118".format(entry.address))
            board = mcc118(entry.address)
            for channel in range(board.info().NUM_AI_CHANNELS):
                value = board.a_in_read(channel)
                #print("Ch {0}: {1:.3f}".format(channel, value))
                if channel is 0:
                    return value
# while True :
#     print(read_value())
#     num=random.uniform(0,10)
#     round(num,3)
#     print(":",round(num,3))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("192.168.137.1", 8888))
    i=0
    while True:
        i += 1
        num = read_value()
#         num=random.uniform(0,100)
        s.sendall(str(round(num,3)).encode('utf-8'))
        print(i,":",num)
        s.send(b'e')
        #time.sleep(1)
        # i=i+1
        # j=i.byte-
        # print(i)
        
        
        
