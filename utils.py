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

def stretch(dir_name, window_length=128*128, cut=True):
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
                elif len(audio) > window_length:
                    if cut:
                        audio = audio[:window_length]
                        assert len(audio) == window_length
                        sf.write(fp, audio, 16000)
                    else:
                        rate = len(audio) / window_length
                        audio = librosa.effects.time_stretch(audio, rate)
                        assert len(audio) == window_length
                        sf.write(fp, audio, 16000)
        os.chdir('..')


def split(dir_name, window_length=128*128):
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
                elif len(audio) > window_length:
                    i = 0
                    while window_length * i < len(audio):
                        _audio = audio[window_length * i:window_length * (i+1)]
                        assert len(audio) == window_length
                        sf.write(fp[:-4]+'-0'+str(i)+fp[-4:], _audio, 16000)
                        i += 1


if __name__ == '__main__':
    # padding('cat', time_stretch=True)
    # stretch('wood_creaks', cut=False)
    split('rain')
