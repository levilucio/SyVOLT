import os
import psutil


_vmb_data = []
_pid = 0

def _VmB():
    '''Private.
    '''
    process = psutil.Process()
    mem_info = process.memory_info()
    data = [mem_info.rss, mem_info.vms]

    # for key in keys:
    #
    #     try:
    #         i = v.index(key)
    #     except ValueError:
    #         continue
    #     new_v = v[i:].split(None, 3)  # whitespace
    #     if len(new_v) < 3:
    #         print(new_v)
    #         raise Exception()# invalid format?
    #
    #      # convert Vm value to bytes
    #     data.append(float(new_v[1]) * _scale[new_v[2]])
    return data


def mem_before():
    global _vmb_data
    global _pid
    _pid = os.getpid()
    _vmb_data = _VmB()

def mem_after(fcn_name):
    global _vmb_data
    new_data = _VmB()

    diff_data = [d - _vmb_data[i] for i, d in enumerate(new_data)]

    if sum(diff_data) > 1 or sum(diff_data) < -1:
        print("Function " + fcn_name + " mem usage: " + str(sum(diff_data)))
    else:
        print("Function " + fcn_name + ": no memory usage seen")

#-------USING SMEM---------
# https://www.selenic.com/smem/
# https://www.selenic.com/smem/download/smem.pdf
import subprocess

def report_memory(pid):
    proc = subprocess.Popen(['smem', '-P test_'], stdout = subprocess.PIPE)
    while True:
        line = proc.stdout.readline().decode('utf-8')
        if not line:
            break

        print("test: " + str(line))
        if line.strip().startswith(str(pid)):
            print("Found!")
