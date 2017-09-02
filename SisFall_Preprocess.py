import numpy as np
import os

class_v = 0
time = 0
np.set_printoptions(threshold='nan')
directory = os.listdir(r'C:\Users\Rimon Dubnov\Desktop\GoogleProject\SisFall_dataset\Test')
os.chdir(r'C:\Users\Rimon Dubnov\Desktop\GoogleProject\SisFall_dataset\Test')

for folder in os.listdir():
    class_v = class_v+1
    os.chdir('C:\\Users\\Rimon Dubnov\\Desktop\\GoogleProject\\SisFall_dataset\\Test\\'+folder)
    directory = os.listdir('C:\\Users\\Rimon Dubnov\\Desktop\\GoogleProject\\SisFall_dataset\\Test\\'+folder)
    for file in directory:
        open_file = open(file, 'r')
        read_file = open_file.read()
        af = read_file.replace('\n','')
        a1f = af.replace(' ','')
        bf = a1f.replace(';;',';')
        if bf[-1] == ';':
            mfile = np.matrix(bf[:-1])
        else:
            mfile = np.matrix(bf)

        cluster = str(class_v)
        group = 'D0' + cluster
        status = np.tile(group, len(mfile))[None].T
        data1 = np.hstack([status, mfile])

        i = 0
        timestamp = np.zeros(shape = (len(mfile),1))
        for row in timestamp:
            time = time + 5000000
            timestamp[i] = int(time)
            i = i+1

        data2 = np.hstack([timestamp, data1])
        strdata = str(data2)
        dataset1 = strdata.replace('\n','')
        dataset2 = dataset1.replace('] [', ';\n')

        cf = dataset2.replace('[','')
        df = cf.replace(']','')
        ef = df.replace("' '",',')
        ff = ef.replace("'",'')
        gf = ff.replace(' ','')

        #write_file = open(file,'w')
        #write_file.write(gf)