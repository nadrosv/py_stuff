#! extracts ID3 tags from mp3 files, which can be saved to csv file.
# run with 'path' argument pointing to directory containing mp3 files

import os, re, sys, csv
from mutagen.easyid3 import EasyID3

def save_list(song_list):
    save_reg = re.compile('Y|y|yes|YES|yup|jo|aye|ja|da|tak|T|t')
    if save_reg.match(input('Save list to csv file? (Y/N)')):
        song_file = open(str(input('Enter .csv file name: ')) + '.csv', 'w', newline='')
        csv_writer = csv.writer(song_file, delimiter=';')
        for n in song_list:
            try:
                csv_writer.writerow(n)
            except:
                print('can\'t save ' + str(n) + '\" to file')
                continue
        song_file.close()
        print('thx, bye!')
    else:
        print('ok, bye!')

def list_files(path):
    ext_reg = re.compile('.*.(mp3|MP3)$')
    files = os.listdir(path)
    info_list =[]

    for f in files:
        if ext_reg.search(f):
            try:
                f = EasyID3(path + f)
                info_list.append((f['artist'][0], f['title'][0]))
                print(info_list[-1])
            except:
                print(f + ': no ID3 tags. saving only file name.')
                info_list.append(f)
                continue

    return info_list

def main(argv):

    if len(sys.argv) > 1:

            song_list = list_files(str(sys.argv[1]) + '\\')
            save_list(song_list)

    else: print('no args, bye!')


if (__name__ == '__main__'): 
    main(sys.argv[1:])