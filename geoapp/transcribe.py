#!/usr/bin/env python

# DO NOT EDIT THIS FILE : Generated from scribe/notebooks/transcribe.ipynb
#!pip install git+https://github.com/openai/whisper.git

from mangorest import mango
from  mangorest.mango import webapi
import colabexts.utils as colabexts_utils
import io, os, librosa, logging, sys

logger = logging.getLogger( "geoapp" )

# ----------------------------------------------------------------------
fn="/Users/snarayan/Desktop/data/audio/test.wav"
# ------------------------------------------------------------------------------
whisperModel  = None
def getModel():
    global whisperModel
    if ( whisperModel is None):
        import whisper
        whisperModel = whisper.load_model("base")
        #whisperModel.DecodingOptions(fp16 = True) 
    return whisperModel

@webapi("/geoaudio/transcribe/")
def transcribe(request=None, file="/tmp/test.wav", offset=0, duration=None, save="", **kwargs): 
    if ( request and request.FILES.getlist('file')):
        for f in request.FILES.getlist('file'):
            file = f.read()
            if ( save ):
                filename = save or '/tmp/test.wav'
                logger.info(f'GOT FILE will save to {filename} and transcribe')
                with open (f"{filename}", "wb") as ff:
                    ff.write(file)
            break;

    if (type(file) == str):
        logger.info(f'File ...{file}')
        if ( not file or not os.path.exists(file)):
            return f"{file}"
        data, sample_rate = librosa.load(file, offset=offset, duration=duration, mono=True, sr=16000)
    else:
        content = io.BytesIO(file)
        logger.info(f'Bytes ... {content.getbuffer().nbytes}')
        data, sample_rate = librosa.load(content,sr=16000, mono=True, offset=offset, duration=duration)
    
    audio, _ = librosa.effects.trim(data)

    out = getModel().transcribe(data)
    #print(out)
    return out['text']

if __name__ == '__main__' and not colabexts_utils.inJupyter():
    transcribe(sys.argv[1])