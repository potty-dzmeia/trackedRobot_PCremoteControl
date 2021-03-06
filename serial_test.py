__author__ = 'potty'

import serial
from baud_rates import BaudRates
import time
import socket
import sys


UDP_MESSAGE_INTERVAL_IN_SEC = 0.1


def get_as_hex_string(data):
    if type(data) == str:
        return ' '.join('0x%02x' % ord(b) for b in data)
    elif type(data) == list:
        return ' '.join('0x%02x' % b for b in data)


def isExpired(start_time):
    """

    :param start_time:
    :return True if timer has expired:
    :type return: bool
    """
    if (time.clock() - start_time) > UDP_MESSAGE_INTERVAL_IN_SEC:
        return True

    return False


def sendUDP(to_socket, to_address, msg):
    # Send data
    print >> sys.stderr, 'sending "%s"' % msg
    sent = to_socket.sendto(msg, to_address)


#
if __name__ == "__main__":

    # Open serial/bluetooth connection for receiving commands
    # --------------------------------
    ser = serial.Serial('/dev/ttyUSB0',
                        baudrate=BaudRates.B_115200,
                        xonxoff=False,
                        rtscts=False,
                        dsrdtr=False,
                        timeout=UDP_MESSAGE_INTERVAL_IN_SEC)
    ser.flushInput()
    ser.flushOutput()

    # Open UDP for sending commands
    # --------------------------------
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('192.168.0.104', 10000)

    keys_status = 0

    while True:
        start_time = time.clock()
        data = ser.read(1)

        # If no message comes within the timeout (100ms) we need to reset the keys_status to 0
        if not data:
            if keys_status:
                keysbb_status = 0
                sendUDP(socket, server_address, keys_status)


        print data

#
#
#
# class KeysStatus:
#         UP          = 0b00000001
#         DOWN        = 0b00000010
#         LEFT        = 0b00000100
#         RIGHT       = 0b00001000
#         BRAKE       = 0b00010000
#         QUIT        = 0b00100000
#         SPEED_UP    = 0b01000000
#         SPEED_DOWN  = 0b10000000
#
# UDP_MESSAGE_INTERVAL_IN_SEC = 0.1
#
#

#
#

#
#
#
# def run():
#
#     # 2 - Initialize the "game"
#     pygame.init()
#     width, height = 300, 200
#     screen = pygame.display.set_mode((width, height))
#
#     key_status = 0  # tells us which keys are being pressed.
#     new_key_status = 0
#
#
#
#     start = time.clock()
#     # 4 - keep looping through
#     while 1:
#         # # 5 - clear the screen before drawing it again
#         screen.fill(0)
#
#         # Send new commands to vehicle
#         if new_key_status != key_status or isExpired(start):
#             key_status = new_key_status
#             if key_status: # do not send empty KeysStatus
#                 sendUDP(sock, server_address, str(key_status))
#             start = time.clock()
#
#         texts("{0:b}".format(key_status), screen)
#
#         # # 7 - update the screen
#         pygame.display.flip()
#
#         # # 8 - loop through the events
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key==K_UP:
#                     new_key_status = new_key_status | KeysStatus.UP
#                 elif event.key==K_DOWN:
#                     new_key_status = new_key_status | KeysStatus.DOWN
#                 elif event.key==K_LEFT:
#                     new_key_status = new_key_status | KeysStatus.LEFT
#                 elif event.key==K_RIGHT:
#                     new_key_status = new_key_status | KeysStatus.RIGHT
#                 elif event.key==K_SPACE:
#                     new_key_status = new_key_status | KeysStatus.BRAKE
#                 elif event.key== K_ESCAPE:
#                     new_key_status = new_key_status | KeysStatus.QUIT
#                 elif event.key== K_a:
#                     new_key_status = new_key_status | KeysStatus.SPEED_UP
#                 elif event.key== K_z:
#                     new_key_status = new_key_status | KeysStatus.SPEED_DOWN
#
#             elif event.type == pygame.KEYUP:
#                 if event.key==K_UP:
#                     new_key_status = new_key_status & ~KeysStatus.UP
#                 elif event.key==K_DOWN:
#                     new_key_status = new_key_status & ~KeysStatus.DOWN
#                 elif event.key==K_LEFT:
#                     new_key_status = new_key_status & ~KeysStatus.LEFT
#                 elif event.key==K_RIGHT:
#                     new_key_status = new_key_status & ~KeysStatus.RIGHT
#                 elif event.key==K_SPACE:
#                     new_key_status = new_key_status & ~ KeysStatus.BRAKE
#                 elif event.key== K_ESCAPE:
#                     new_key_status = new_key_status & ~KeysStatus.QUIT
#                 elif event.key== K_a:
#                     new_key_status = new_key_status & ~KeysStatus.SPEED_UP
#                 elif event.key== K_z:
#                     new_key_status = new_key_status & ~KeysStatus.SPEED_DOWN
#                 if event.key == K_ESCAPE:
#                     return
#
#
#
#
# if __name__ == "__main__":
#     run()
#
#
#
#
