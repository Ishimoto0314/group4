import librosa
import numpy as np

def duration_tempo(tempo, time):#音の長さの解析
    #4分音符 = 60000msec ÷ BPM
    #2分音符や8分音符は2倍や1/2倍で求められる。
    #1秒は1000msecである。
    note_4 = 60000 / tempo / 1000

    dict02 = {}
    dict02[1] = note_4 * 4
    dict02[2] = note_4 * 2
    dict02[4] = note_4
    dict02[8] = note_4 * (1 / 2)
    dict02[16] = note_4 * (1 / 4)
    dict02[32] = note_4 * (1 / 8)

    array01 = [(dict02[1] - dict02[2])/2, (dict02[2] - dict02[4])/2, (dict02[4] - dict02[8])/2, (dict02[8] - dict02[16])/2, (dict02[16] - dict02[32])/2]
    count  = 0
    duration = 0

    for k, v in dict02.items():
        val01 = time - v

        if count == 0:
            if val01 >= (array01[0] * -1):
                duration = 1
                break

        elif count == 1:
            if array01[0] > val01 and val01 >= (array01[1] * -1):
                duration = 2
                break

        elif count == 2:
            if array01[1] > val01 and val01 >= (array01[2] * -1):
                duration = 4
                break

        elif count == 3:
            if array01[2] > val01 and val01 >= (array01[3] * -1):
                duration = 8
                break

        elif count == 4:
            if array01[3] > val01 and val01 >= (array01[4] * -1):
                duration = 16
                break

        elif count == 5:
            if array01[4] > val01:
                duration = 32
                break

        count += 1
    
    return duration