import os, subprocess
from os import walk
import shlex
import mimetypes
mimetypes.init()

def make_name(path):
    s = os.path.split(path)
    # s[-1] = "TRANS_"+s[-1]
    return os.path.join("./transcoded", "TRANS_"+s[-1])


def transcode():
    for path, subdirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for name in files:
            print(os.path.join(path, name))
            fn = os.path.join(path, name)
            
            mimestart = mimetypes.guess_type(fn)[0]
            if mimestart != None:
                mimestart = mimestart.split('/')[0]
                if mimestart == 'video':        
                    print(f"""ffmpeg -i "{fn}" -c:v av1_nvenc -crf 55 "{make_name(fn)}" """)
                    subprocess.run(
                        f"""ffmpeg -i "{fn}" -c:v av1_nvenc -crf 55 "{make_name(fn)}" """
                        , shell=True)

def get_transcoded_names():
    for path, subdirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for name in files:
            fn = os.path.join(path, name)
            
            mimestart = mimetypes.guess_type(fn)[0]
            if mimestart != None:
                mimestart = mimestart.split('/')[0]
                if mimestart == 'video':        
                    if "TRANS" in name:
                        print(fn)

def delete_old_videos():
    for path, subdirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
        for name in files:
            print(os.path.join(path, name))
            fn = os.path.join(path, name)
            
            mimestart = mimetypes.guess_type(fn)[0]
            if mimestart != None:
                mimestart = mimestart.split('/')[0]
                if mimestart == 'video' and "TRANS" not in name:        
                    os.remove(fn)

transcode()
get_transcoded_names()
delete_old_videos()