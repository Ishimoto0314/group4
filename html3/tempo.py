import librosa
import numpy as np

def tempo(file):
	y, sr = librosa.load(file, duration=30)
	onset_env = librosa.onset.onset_strength(y, sr=sr)
	tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)
	return tempo