"""
"""
import os,sys
import shutil


print('奥利给~~~~','\n')
def change_file_name():
    wav_names1 = os.listdir(path1)  #wavs的文件名列表
    lab_names2 = os.listdir(path2)  ##lab的文件名列表
    index = 0                       #指针从零开始
    print(wav_names1)               #这俩是个列表
    wav_id_list=[]
    lab_id_list=[]
    a=[]
    b=[]
    for wav_name in wav_names1: 
        wav_id = wav_name.split('.')[0] 
        #wav_id_list.append(wav_id)
    for lab_name in lab_names2:
        lab_id = lab_name.split('.')[0]
        lab_id_list.append(lab_id)
    for fil in lab_id_list :
            shutil.copyfile(path1 + '/' + wav_id + '.wav' ,path3 + '/' + fil + '.wav')
            print(path3 + '/'+ fil)
    print('一给我哩giao~~~~giao~~~~','\n') 
   
if __name__ == '__main__':
    path1 = 'r'#'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/preprocess_for_diffusion/aslp-tacotron_for_fs_getdur/testdata/db6/labels_with_dur_1wneutral'
    path2 = 'proposed'#'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/preprocess_for_diffusion/aslp-tacotron_for_fs_getdur/testdata/db6/clean_labels'
    path3 ='ref1'
    change_file_name()
