import os

import librosa
import numpy as np
import soundfile as sf

def padding(dir_name, window_length=128*128, time_stretch=False):
    os.chdir(dir_name)
    for phase in ['train', 'valid']:
        os.chdir(phase)
        print(os.getcwd())
        fps = os.listdir()
        for fp in fps:
            if fp.endswith('wav'):
                audio, sr = librosa.load(fp, 16000)
                if len(audio) < window_length:
                    audio = np.append(audio, [0.0] * (window_length-len(audio)))
                    assert len(audio) == window_length
                    sf.write(fp, audio, 16000)
                elif len(audio) == window_length:
                    pass
                else:
                    print(fp)
                    rate = len(audio) / window_length
                    audio = librosa.effects.time_stretch(audio, rate)
                    assert len(audio) == window_length
                    sf.write(fp, audio, 16000)
        os.chdir('..')

def stretch(dir_name, window_length=128*128):
    os.chdir(dir_name)
    for phase in ['train', 'valid']:
        os.chdir(phase)
        print(os.getcwd())
        fps = os.listdir()
        for fp in fps:
            if fp.endswith('wav'):
                audio, sr = librosa.load(fp, 16000)
                if len(audio) < window_length:
                    rate = len(audio) / window_length
                    audio = librosa.effects.time_stretch(audio, rate)
                    assert len(audio) == window_length
                    sf.write(fp, audio, 16000)
                elif len(audio) == window_length:
                    pass
                else:
                    audio = audio[:window_length]
                    assert len(audio) == window_length
                    sf.write(fp, audio, 16000)
        os.chdir('..')


if __name__ == '__main__':
    # padding('cat', time_stretch=True)
    stretch('car_horn')
