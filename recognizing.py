from vosk import Model, KaldiRecognizer
from config import MODEL_PATH
from vosk import Model, KaldiRecognizer, SetLogLevel

import wave
import json

SetLogLevel(0)

model = Model(MODEL_PATH)

def parse_wav(path):
    wf = wave.open(path, "rb")

    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print("Audio file must be WAV format mono PCM.")
        exit (1)

    rec = KaldiRecognizer(model, wf.getframerate())
    
    results = []

    while True:
        data = wf.readframes(16000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            jresult = rec.Result()
            res = json.loads(jresult)
            results.append(res['text'])

    results.append(json.loads(rec.FinalResult())['text'])
    return results

