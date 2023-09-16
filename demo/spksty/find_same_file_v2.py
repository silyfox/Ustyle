"""
"""
import os,sys
import shutil


# print('奥利给~~~~','\n')
# def change_file_name():
# #    file_id_list = []
#     with open (file_list, 'r') as f:
#         for line in f.readlines():
#             line = line.strip()
#             line = line.split('.')[0]
#             shutil.copyfile(path1 + '/' + line + '.wav' ,path1_1 + '/' + line  + '.wav')
#             shutil.copyfile(path2 + '/' + line + '.wav' ,path2_1 + '/' + line  + '.wav')
#             shutil.copyfile(path3 + '/' + line + '.wav' ,path3_1 + '/' + line  + '.wav')
#             shutil.copyfile(path4 + '/' + line + '.wav' ,path4_1 + '/' + line  + '.wav')
#             print(path3 + '/'+ line)

print('奥利给~~~~','\n')
def copyvalle():
    valle_list = os.listdir(path1)
    with open (file_list, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            line = line.split('.')[0]
            text = line.split('_')[0]
            spk =  line.split('_')[1]  + '_' + line.split('_')[2] + '_' + line.split('_')[3]
            print(spk)
            for valle_file in valle_list:
                valle_file = valle_file.strip()
                # valle_file = valle_file.split('.')[0]
                # valle_spk = valle_file.split('-')[0]
                # valle_text = (valle_file.split('-')[1]).split('_')[-1]
                valle_spk = valle_file.split('.')[0]
                if valle_spk == spk: # and valle_text == text:
                    shutil.copyfile(path1 + '/' + valle_spk + '.wav', path1_1 + '/' + line  + '.wav')
            print(valle_file, '==', line )



if __name__ == '__main__':
    file_list='ref.scp'
    path1 = 'ref1'#'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/preprocess_for_diffusion/aslp-tacotron_for_fs_getdur/testdata/db6/wavs_normed_1wn' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/preprocess_for_diffusion/aslp-tacotron_for_fs_getdur/testdata/db6/clean_labels' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/text2style2wav/2_emo_ppg_vits/testdata/csspk_cslang/wavs' #'/home/tli/litao/aslp-newsystem/wavernn_wenwen2.0/trainingdata/wenwen_20cn_libritts40en/mels' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/preprocess_for_diffusion/aslp-tacotron_for_fs_getdur/testdata/wenwen_20cn_libritts40en/labels_with_dur' #'/home/work_nfs4_ssd/tli/data/db6_neutral/db6_neutral/clean_labels' #'/home/backup_nfs2/data_tts/biaobei_eng_female/raw/txts' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/data/robot_pick/005001-005500-F/labs' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/data/robot_pick/097001-097500-M/labs' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/tacotron_th/testdata/multspk-db2-db6-aic/emotion_score'
    path1_1 = 'ref'
    # path2 ='demoused/unet_all' #'wavs_normed'  #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/cross_language/testdata/wenwen_20cn_libritts40en/labels/' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/text2style2wav/2_emo_ppg_vits/testdata/csspk_cslang/wavs_used' #'/home/tli/litao/aslp-newsystem/wavernn_wenwen2.0/trainingdata/wenwen_20cn_libritts40en/train/test/mel' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/egsdb6_transformer/testdata/db6/wavs_normed_1wn'  #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/grad_tts/preprocess_for_diffusion/aslp-tacotron_for_fs_getdur/testdata/wenwen_20cn_libritts40en/labels_with_dur_used' #'/home/work_nfs4_ssd/tli/data/db6_neutral/clean_labels' #'/home/tli/ttli/data/db6_neutral/trimmed_wavs_normed' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/cross_language/testdata/cross_language_db1/propsody/en_txt' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/tacotron_th/testdata/multspk-fintune-robot_100_famale3/labels'#'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/tacotron_th/testdata/multspk-fintune-robot_100_mate2/labels' #'/home/tli/litao/aslp-newsystem/201912-Emo-work/emo-mulspk/tacotron_th/testdata/multspk-db3male-db6/emotion_score'
    # path2_1 = 'demopicked/20230913_tli_ust_spkstycmos/unet'
    # path3 ='demoused/anyspk_all'
    # path3_1 ='demopicked/20230913_tli_ust_spkstycmos/anyspk'
    # path4 ='demoused/100h_all'
    # path4_1 ='demopicked/20230913_tli_ust_spkstycmos/proposed'
    # change_file_name()
    copyvalle()