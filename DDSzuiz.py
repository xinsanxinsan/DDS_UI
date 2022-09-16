from tkinter import *
import stmhidzui


def send():
    global Device
    list = ['0']
    #print(t2.get())

    #print(freq1, freq2, len(freq1), len(freq2))
    #print(phase1_1, phase1_2, phase1_3, phase1_4, len(phase1_1), len(phase1_2), len(phase1_3), len(phase1_4))
    #print(amp1_1, amp1_2, amp1_3, amp1_4, len(amp1_1), len(amp1_2), len(amp1_3), len(amp1_4))
    #print(phase2_1, phase2_2, phase2_3, phase2_4, len(phase2_1), len(phase2_2), len(phase2_3), len(phase2_4))
    #print(amp2_1, amp2_2, amp2_3, amp2_4, len(amp2_1), len(amp2_2), len(amp2_3), len(amp2_4))
    list.clear()
    list.append(t2.get())
    list.append(t3.get())
    list.append(t4.get())
    list.append(t5.get())
    list.append(t8.get())
    list.append(t9.get())
    list.append(t12.get())
    list.append(t13.get())
    list.append(t16.get())
    list.append(t17.get())
    list.append(t6.get())
    list.append(t7.get())
    list.append(t10.get())
    list.append(t11.get())
    list.append(t14.get())
    list.append(t15.get())
    list.append(t18.get())
    list.append(t19.get())
    list.append(t21.get())
    #print(list)
    stmhidzui.senddata(list, Device, 0)


def check():
    global VID
    global PID
    global Device

    res, Device = stmhidzui.opend(VID, PID)
    device_txt = {0: '设备 离线', 1: '设备 在线'}
    t1.delete(0.0, END)
    t1.insert('end', device_txt[res])
    #t1.update()
    if res == 0:
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
    else:
        b1.config(state=NORMAL)
        b2.config(state=NORMAL)
        b3.config(state=NORMAL)
        b4.config(state=NORMAL)

    root.after(5000, check)

"""
    t3.delete(0.0, END)
    result = 0
    result, size = stmhid.send(MPGFile, Device)
    result_txt = {0: 'Fail', 1: 'Send Some', 2: 'Send Success'}
    t3.insert('end', result_txt[result])
"""


def refresh():
    global Device

    re, listreceive = stmhidzui.receive(Device, 0)
    t2.delete(0, END)
    t2.insert('end', listreceive[1])
    t3.delete(0, END)
    t3.insert('end', listreceive[2])
    t4.delete(0, END)
    t4.insert('end', listreceive[3])
    t5.delete(0, END)
    t5.insert('end', listreceive[4])
    t8.delete(0, END)
    t8.insert('end', listreceive[5])
    t9.delete(0, END)
    t9.insert('end', listreceive[6])
    t12.delete(0, END)
    t12.insert('end', listreceive[7])
    t13.delete(0, END)
    t13.insert('end', listreceive[8])
    t16.delete(0, END)
    t16.insert('end', listreceive[9])
    t17.delete(0, END)
    t17.insert('end', listreceive[10])
    t6.delete(0, END)
    t6.insert('end', listreceive[11])
    t7.delete(0, END)
    t7.insert('end', listreceive[12])
    t10.delete(0, END)
    t10.insert('end', listreceive[13])
    t11.delete(0, END)
    t11.insert('end', listreceive[14])
    t14.delete(0, END)
    t14.insert('end', listreceive[15])
    t15.delete(0, END)
    t15.insert('end', listreceive[16])
    t18.delete(0, END)
    t18.insert('end', listreceive[17])
    t19.delete(0, END)
    t19.insert('end', listreceive[18])
    t21.delete(0, END)
    t21.insert('end', listreceive[19])
    open_txt = {0: '信号关闭', 1: '信号开启', 3: '接收超时', 4: '接收错误'}
    t20.delete(0.0, END)
    t20.insert('end', open_txt[re])


def sendsignal():
    global Device
    list2 = []
    list2.append(t21.get())
    #list2.append(t22.get())
    stmhidzui.senddata(list2, Device, 1)
    re, list3 = stmhidzui.receive(Device, 1)
    open_txt = {0: '信号关闭', 1: '信号开启', 3: '接收超时', 4:'接收错误'}
    t20.delete(0.0, END)
    t20.insert('end', open_txt[re])

"""
def close_device():
    global Device
    stmhidzui.closeD(Device)
    #t19.delete(0.0, END)
    t1.delete(0.0,END)
    # t3.delete(0.0, END)
"""

def savedata():
    global Device
    list = []
    list.clear()
    list.append(t2.get())
    list.append(t3.get())
    list.append(t4.get())
    list.append(t5.get())
    list.append(t8.get())
    list.append(t9.get())
    list.append(t12.get())
    list.append(t13.get())
    list.append(t16.get())
    list.append(t17.get())
    list.append(t6.get())
    list.append(t7.get())
    list.append(t10.get())
    list.append(t11.get())
    list.append(t14.get())
    list.append(t15.get())
    list.append(t18.get())
    list.append(t19.get())
    list.append(t21.get())
    stmhidzui.senddata(list, Device, 2)


global VID
global PID
global i
global list

VID = 1155
PID = 22352
i = 0
root = Tk()
root.title('Deep Brain Stimulation')  # 窗口名称
root.geometry('1024x700')  # 界面大小英文字母x
root.resizable(width=True, height=True)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
# root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件

frm1 = Frame(root)
frm1.pack(side='top', pady=5)  # padx 水平方向，pady垂直方向
frm2 = Frame(root)
frm2.pack(side='top', pady=5)

frm10 = Frame(root)
frm10.pack(side='top', pady=2)

frm3 = Frame(root)
frm3.pack(side='top', pady=5)
frm4 = Frame(root)
frm4.pack(side='top', pady=5)
frm5 = Frame(root)
frm5.pack(side='top', pady=5)
frm6 = Frame(root)
frm6.pack(side='top', pady=2)
frm7 = Frame(root)
frm7.pack(side='top', pady=2)
frm8 = Frame(root)
frm8.pack(side='top', pady=2)
frm9 = Frame(root)
frm9.pack(side='top', pady=2)
frm11= Frame(root)
frm11.pack(side='top', pady=2)
frm12= Frame(root)
frm12.pack(side='top', pady=2)



Label(frm1, text="Deep Brain Stimulation", fg='Brown', font=('Times New Roman', 24)).pack(side='top', padx=100)

Label(frm2, text="设备状态", width=15, height=1, font=('宋体', 19)).pack(side='left', padx=50)
t1 = Text(frm2, width=15, height=1, font=('宋体', 19))
t1.pack(side='left', padx=20, pady=20)





Label(frm10, text="", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=40)
Label(frm10, text="DDS1", width=12, height=1, fg='purple', font=('Times New Roman', 30)).pack(side='left', padx=20)
Label(frm10, text="", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=10)
Label(frm10, text="", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=10)
Label(frm10, text="DDS2", width=12, height=1, fg='purple', font=('Times New Roman', 30)).pack(side='left', padx=20)
Label(frm10, text="", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=20)


Label(frm3, text="", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=5)
Label(frm3, text="设定频率1\Hz", width=12, height=1, font=('宋体', 19)).pack(side='left', padx=10)
t2 = Entry(frm3, width=12, font=('宋体', 19))
t2.pack(side='left', padx=(10, 30), pady=20)
t2.insert('end', '2000')

Label(frm3, text="", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=(30, 5))
Label(frm3, text="设定频率2\Hz", width=12, height=1, font=('宋体', 19)).pack(side='left', padx=10)
t3 = Entry(frm3, width=12, font=('宋体', 19))
t3.pack(side='left', padx=10, pady=20)
t3.insert('end', '2015')


Label(frm4, text="", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=5)
Label(frm4, text="相位\°", width=12, height=1, font=('宋体', 19)).pack(side='left', padx=10)
Label(frm4, text="幅度\mV", width=12, height=1, font=('宋体', 19)).pack(side='left', padx=(10, 30))
Label(frm4, text="", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=(30, 5))
Label(frm4, text="相位\°", width=12, height=1, font=('宋体', 19)).pack(side='left', padx=10)
Label(frm4, text="幅度\mV", width=12, height=1, font=('宋体', 19)).pack(side='left', padx=10)

Label(frm5, text="ch1_1", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=5)
t4 = Entry(frm5, width=12, font=('宋体', 19))
t4.pack(side='left', padx=10)
t4.insert('end', '0')
t5 = Entry(frm5, width=12, font=('宋体', 19))
t5.pack(side='left', padx=(10, 30))
t5.insert('end', '5000')

Label(frm5, text="ch2_1", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=(30, 5))
t6 = Entry(frm5, width=12, font=('宋体', 19))
t6.pack(side='left', padx=10)
t6.insert('end', '0')
t7 = Entry(frm5, width=12, font=('宋体', 19))
t7.pack(side='left', padx=10)
t7.insert('end', '5000')

Label(frm6, text="ch1_2", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=5)
t8 = Entry(frm6, width=12, font=('宋体', 19))
t8.pack(side='left', padx=10)
t8.insert('end', '0')
t9 = Entry(frm6, width=12, font=('宋体', 19))
t9.pack(side='left', padx=(10, 30))
t9.insert('end', '5000')


Label(frm6, text="ch2_2", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=(30, 5))
t10 = Entry(frm6, width=12, font=('宋体', 19))
t10.pack(side='left', padx=10)
t10.insert('end', '0')
t11 = Entry(frm6, width=12, font=('宋体', 19))
t11.pack(side='left', padx=10)
t11.insert('end', '5000')

Label(frm7, text="ch1_3", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=5)
t12 = Entry(frm7, width=12, font=('宋体', 19))
t12.pack(side='left', padx=10)
t12.insert('end', '0')
t13 = Entry(frm7, width=12, font=('宋体', 19))
t13.pack(side='left', padx=(10, 30))
t13.insert('end', '5000')

Label(frm7, text="ch2_3", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=(30, 5))
t14 = Entry(frm7, width=12, font=('宋体', 19))
t14.pack(side='left', padx=10)
t14.insert('end', '0')
t15 = Entry(frm7, width=12, font=('宋体', 19))
t15.pack(side='left', padx=10)
t15.insert('end', '5000')


Label(frm8, text="ch1_4", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=5)
t16 = Entry(frm8, width=12, font=('宋体', 19))
t16.pack(side='left', padx=10)
t16.insert('end', '0')
t17 = Entry(frm8, width=12, font=('宋体', 19))
t17.pack(side='left', padx=(10, 30))
t17.insert('end', '5000')

Label(frm8, text="ch2_4", width=5, height=1, font=('宋体', 19)).pack(side='left', padx=(30, 5))
t18 = Entry(frm8, width=12, font=('宋体', 19))
t18.pack(side='left', padx=10)
t18.insert('end', '0')
t19 = Entry(frm8, width=12, font=('宋体', 19))
t19.pack(side='left', padx=10)
t19.insert('end', '5000')


Label(frm9, text="信号状态", width=15, height=1, font=('宋体', 19)).pack(side='left', padx=(20, 5), pady=40)
t20 = Text(frm9, width=15, height=1, font=('宋体', 19))
t20.pack(side='left', padx=(5, 40))
t20.insert('end', "信号关闭")

b1 = Button(frm9, text="发送数据", width=15, height=1, command=send, font=('黑体', 22))
b1.pack(side='left', padx=20, pady=40)
b2 = Button(frm9, text="读取数据", width=15, height=1, command=refresh, font=('黑体', 22))
b2.pack(side='left', padx=20, pady=40)

Label(frm11, text="信号缓变时间\S", width=15, height=1, font=('宋体', 19)).pack(side='left', padx=(20, 5), pady=40)
t21 = Entry(frm11, width=15, font=('宋体', 19))
t21.pack(side='left', padx=(5, 40))
t21.insert('end', '60')

b3 = Button(frm11, text="保存数据", width=15, height=1, command=savedata, font=('黑体', 22))
b3.pack(side='left', padx=20, pady=20)
b4 = Button(frm11, text="信号开关", width=15, height=1, command=sendsignal, font=('黑体', 22))
b4.pack(side='left', padx=20, pady=20)


# 显示界面
#mainloop 死循环，不执行后面的代码
root.after(1000, check)
root.mainloop()


