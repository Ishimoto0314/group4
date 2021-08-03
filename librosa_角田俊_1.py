import librosa
filename = librosa.util.example_audio_file()
print(filename)

y,sr = librosa.load(filename)
print(type(y))
print(y.shape)
print(type(sr),sr)

tempo,beat_frames = librosa.beat.beat_track(y=y,sr=sr)
print('Estimated tempo:{:.2f}beats per minute'.format(tempo))
print(beat_frames)