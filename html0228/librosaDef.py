import librosa
import numpy as np

def tempo(y, sr): #テンポの解析
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
    return np.round(tempo)

def onset_analysis(y, sr): #オンセットの解析
    win_length = 2048
    hop_length = win_length // 4
    n_fft = win_length
    window = 'hann'
    stft = librosa.stft(y, n_fft=n_fft, hop_length=hop_length, win_length=win_length, window=window, center=True)
    amplitude = np.abs(stft)
    log_power = librosa.amplitude_to_db(amplitude, ref=np.max)
    onset_envelope = librosa.onset.onset_strength(S=log_power, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_envelope, sr=sr, hop_length=hop_length)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr, hop_length=hop_length)

    return onset_times

def note_analyis(y, sr): #音名の解析
    y, index = librosa.effects.trim(y)

    hop_length = 512
    window = 'hann'
    bins_per_octave = 12
    n_octaves = 7
    n_bins = bins_per_octave * n_octaves
    cqt_amplitude = np.abs(librosa.cqt(y, sr=sr, hop_length=hop_length, fmin=librosa.note_to_hz('C1'), n_bins=n_bins,
                                       bins_per_octave=bins_per_octave, window=window))

    max_indices = np.argmax(cqt_amplitude, axis=0)
    notes = librosa.hz_to_note(librosa.cqt_frequencies(n_bins=n_bins, fmin=librosa.note_to_hz('C1'), bins_per_octave=bins_per_octave))
    time = librosa.core.frames_to_time(np.arange(max_indices.shape[0]), sr=sr, hop_length=hop_length)
    
    time_sum = 0
    dict01 = {}
    
    for t, max_index in zip(time, max_indices):
        time_sum += t
        if notes[max_index] in dict01.keys():
            dict01[ notes[max_index] ] += 1
        else:
            dict01[ notes[max_index] ] = 1
            
    note = max(dict01)
    
    return note

