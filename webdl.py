
 import os
 import json
 import subprocess
 import argparse
 import sys
 import pyfiglet
 from rich import print
 from typing import DefaultDict
title = pyfiglet.figlet_format('WEBDL Script', font='slant')
print(f'[magenta]{title}[/magenta]')
print("Required files : yt-dlp.exe, mp4decrypt.exe\n")

arguments = argparse.ArgumentParser()
# arguments.add_argument("-m", "--video-link", dest="mpd", help="MPD url")
arguments.add_argument("-o", '--output', dest="output", help="Specify output file name with no extension", required=True)
arguments.add_argument("-id", dest="id", action='store_true', help="use if you want to manually enter video and audio id.")
arguments.add_argument("-s", dest="subtitle", help="enter subtitle url")
arguments.add_argument("-k", dest="keyfile", action='store_true', help="Use keyfile with the same name as specified output")
arguments.add_argument("-d", dest="delenc", action='store_true', help="Delete encoded AND JSON FILE upon completion")
args = arguments.parse_args()

if args.keyfile:
    keyfile = str(args.output) + ".json"
    else:
        keyfile = "keys.json"
with open(keyfile) as json_data:
    config = json.load(json_data)
        json_mpd_url = config[0]['mpd_url']
            try:
                    keys = ""
                            for i in range(1, len(config)):
                                        keys += f"--key {config[i]['kid']}:{config[i]['hex_key']} "
                                            except:
                                                    keys = ""
                                                            for i in range(1, len(config)-1):
                                                                        keys += f"--key {config[i]['kid']}:{config[i]['hex_key']} "
currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)

youtubedlexe = dirPath + '/binaries/yt-dlp.exe'
mp4decryptexe = dirPath + '/binaries/mp4decrypt_new.exe'

# mpdurl = str(args.mpd)
output = str(args.output)
subtitle = str(args.subtitle)

if args.id:
    print(f'Selected MPD : {json_mpd_url}\n')    
        subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-F', json_mpd_url])
    vid_id = input("\nEnter Video ID : ")
        audio_id = input("Enter Audio ID : ")
            subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', audio_id, '--fixup', 'never', json_mpd_url, '-o', 'encrypted.m4a', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
                subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', vid_id, '--fixup', 'never', json_mpd_url, '-o', 'encrypted.mp4', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])   
else:
    print(f'Selected MPD : {json_mpd_url}\n')
        subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', 'ba', '--fixup', 'never', json_mpd_url, '-o', 'encrypted.m4a', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])
            subprocess.run([youtubedlexe, '-k', '--allow-unplayable-formats', '--no-check-certificate', '-f', 'bv', '--fixup', 'never', json_mpd_url, '-o', 'encrypted.mp4', '--external-downloader', aria2cexe, '--external-downloader-args', '-x 16 -s 16 -k 1M'])    

print("\nDecrypting .....")
subprocess.run(f'{mp4decryptexe} --show-progress {keys} encrypted.m4a decrypted.m4a', shell=True)
subprocess.run(f'{mp4decryptexe} --show-progress {keys} encrypted.mp4 decrypted.mp4', shell=True)  

    delete_choice = 1
        if os.path.isfile(output + ".mkv"):
                os.remove(keyfile)
                else:
                    print("\nDo you want to delete the Encrypted Files : Press 1 for yes , 2 for no")
                        delete_choice = int(input("Enter Response : "))
if delete_choice == 1:
    os.remove("encrypted.m4a")
        os.remove("encrypted.mp4")
            os.remove("decrypted.m4a")
                os.remove("decrypted.mp4")
                    try:    
                            os.remove("en.srt")
                                except:
                                        pass
                                        else:
                                            pass
