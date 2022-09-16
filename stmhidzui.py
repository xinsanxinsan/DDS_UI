import hid
import numpy as np
import math

"""
import time
"""

"""
def seek():
    productlist = ['USB HID device:']
    vid = ['VID:']
    pid = ['PID:']

    for device_dict in hid.enumerate():

        # keys = list(device_dict.keys())
        # keys.sort()
        #for key in keys:
           # print("key:%s : %s" % (key, device_dict[key]))
        #print(device_dict)
        print(device_dict['product_string'])
        print()
        productlist.append(device_dict['product_string'])
        vid.append(device_dict['vendor_id'])
        pid.append(device_dict['product_id'])
    # print(productlist)
    # print(vid,pid)
    return productlist, vid, pid
"""


def opend(Vendor_ID, Product_ID):
    re = 0
    try:
        device = hid.device()
        device.open(Vendor_ID, Product_ID)  # Vendor_ID/Product_ID
        """
        print("Open the device")
        print("Manufacturer: %s" % device.get_manufacturer_string())
        print("Product: %s" % device.get_product_string())
        print("Serial No: %s" % device.get_serial_number_string())
        """
        re = 1

    except IOError as ex:
        re = 0
    return re, device


def senddata(listbuf, device, dc1):

    sb = np.zeros(65, dtype='uint8')

    if dc1 == 0 or dc1 == 2:
        length1 = 19
    elif dc1 == 1:
        length1 = 1
    else:
        length1 = 0

    # str转int
    for i in range(length1):
        num = 0
        for j in range(len(listbuf[i])):
            num = num + int(listbuf[i][j]) * (10 ** (len(listbuf[i]) - j - 1))
            # /12000000 * 2^24

        k = 3
        num1 = round(num)
        if dc1 == 1:
            num1 = round(num)
            while k > 0:
                sb[10 - k + i * 3] = math.floor(num1 / (256 ** (k - 1)))
                num1 = num1 - sb[k] * (256 ** (k - 1))
                k = k - 1
            break
        """
        if i < 2:
            num = num * (2 ** 16) / 46875
            num1 = round(num)
            #print(num, i, num1, i)
        elif (i == 2) or (i == 4) or (i == 6) or (i == 8) \
                or (i == 10) or (i == 12) or (i == 14) or (i == 16):
            num = num * (2 ** 16 - 1) / 360
            num1 = round(num)
        elif i == 3:
            num = num * 256 * 500 / (13400 * 496)  # 0x1400 / 17.6
            #num = num * 256 / 13293
            num1 = round(num)
        elif i == 5:
            num = num * 256 * 180 * 180 / (13600 * 178 * 182) # 0x1400 / 17.6
            #num = num * 256 / 13598
            num1 = round(num)
        elif i == 7:
            num = num * 256 * 180/ (13800 * 178)  # 0x1380 / 17.6
            #num = num * 256 / 13647
            num1 = round(num)
        elif i == 9:
            num = num * 256 * 180 / (14100 * 177)  # 0x1360 / 17.6
            #num = num * 256 / 13865
            num1 = round(num)
        elif i == 11:
            num = num *256 * 180 / (13700 * 178)  # 0x1400 / 17.6
            #num = num * 256 / 13548
            num1 = round(num)
        elif i == 13:
            num = num * 256 * 500 / (14200 * 496)  # 0x1360 / 17.6
            #num = num * 256 / 14086
            num1 = round(num)
        elif i == 15:
            num = num * 256 * 180 / (13500 * 179)  # 0x143B / 17.6
            #num = num * 256 / 13425
            num1 = round(num)
        elif i == 17:
            num = num * 256 * 180 / (13800 * 178)  # 0x1400 / 17.6
            #num = num * 256 / 13647
            num1 = round(num)
        else:
            num1 = round(num)
        #print(num1)
        """
        while k > 0:
            sb[10 - k + i * 3] = math.floor(num1 / (256 ** (k - 1)))
            #num1 = num1 - sb[k] * (256 ** (k - 1))
            k = k - 1

    print(sb)


    try:

        device.set_nonblocking(1)

        # write data to the device
        if dc1 == 0:

            # SENDDATA 发送data
            sb[0] = 0x00
            sb[1] = 0x53
            sb[2] = 0x44
            sb[3] = 0x41
            sb[4] = 0x54
            sb[5] = 0x41
            sb[6] = 0x00
            res = device.write(sb)
            #print(sb)

        elif dc1 == 1:

            # SENDDELAY 发送delay
            sb[0] = 0x00
            sb[1] = 0x53
            sb[2] = 0x44
            sb[3] = 0x45
            sb[4] = 0x4C
            sb[5] = 0x41
            sb[6] = 0x59
            res = device.write(sb)

        elif dc1 == 2:

            sb[0] = 0x00
            sb[1] = 0x53
            sb[2] = 0x41
            sb[3] = 0x56
            sb[4] = 0x45
            sb[5] = 0x44
            sb[6] = 0x41
            res = device.write(sb)


        else:
            sb[0] = 0x00
            sb[1] = 0x54

        if res != 65:

            if res == -1:
                return 0
            return 1

        return 2

    except IOError as ex:
        return 0


"""
def closeD(device):
    print("Close the device")
    device.close()
"""


def receive(device, dc1):

    rec = np.zeros(64, dtype='uint8')
    listreceive = ['0']
    if dc1 == 0:
        length1 = 20
    if dc1 == 1:
        length1 = 1
    re = 4

    try:
        device.set_nonblocking(1)

        if dc1 == 0:
            res = device.write([0x00, 0x52, 0x45, 0x41, 0x44, 0x44, 0x41, 0x54, 0x41])

        count = 1  # 接收1次
        while count < 1000000:
            d = device.read(64)
            count = count + 1
            if d:
                d = np.array(d, dtype='uint8')
                if dc1 == 0:
                    print("read", d)
                    for i in range(length1):
                        num = d[i * 3+3] * 65536 + d[i * 3 + 4] * 256 + d[i * 3 + 5]
                        """
                        if i < 2:
                            num = num*46875/(2**16)
                            num1 = round(num)

                        elif i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12 \
                            or i == 14 or i == 16:
                            num = num * 360/(2**16 - 1)
                            num1 = round(num)
                        elif i == 3:
                            num = (num / (500 * 256)) * (13400 * 496)
                            num1 = round(num)
                        elif i == 5:
                            num = (num / (256 * 180 * 180)) * (13600 * 178 * 182)
                            num1 = round(num)
                        elif i == 7:
                            num = (num / (256 * 180)) * (13800 * 178)
                            num1 = round(num)
                        elif i == 9:
                            num = (num / (256 * 180)) * (14100 * 177)
                            num1 = round(num)
                        elif i == 11:
                            num = (num / (256 * 180)) * (13700 * 178)
                            num1 = round(num)
                        elif i == 13:
                            num = (num / (256 * 500)) * (14200 * 496)
                            num1 = round(num)
                        elif i == 15:
                            num = (num / (256 * 180)) * (13500 * 179)
                            num1 = round(num)
                        elif i == 17:
                            num = (num / (256 * 180)) * (13800 * 178)
                            num1 = round(num)
                        elif i == 18:
                            num1 = round(num)
                            print(num1)
                        else:
                        """
                        num1 = round(num)
                        if i == 19:
                            if num == 1:
                                re = 1
                            else:
                                re = 0

                        snum1 = str(num1)
                        listreceive.append(snum1)
                if dc1 == 1:
                    # close
                    if (d[0] == 0x43) and (d[1] == 0x4C) and (d[2] == 0x4F) and (d[3] == 0x53) and (d[4] == 0x45):
                        re = 0
                    #open
                    elif (d[0] == 0x4F) and (d[1] == 0x50) and (d[2] == 0x45) and (d[3] == 0x4E):
                        re = 1
                    else:
                        re = 4


        if count >= 1000000:
            if dc1 == 0:
                for i in range(length1):
                    listreceive.append("-")
        return re, listreceive

    except IOError as ex:
        return 4
