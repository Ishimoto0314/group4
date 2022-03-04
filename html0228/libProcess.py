import numpy as np
import librosa
import librosaDef as ld
import duration as du

def process():
	y, sr = librosa.load("audio/1.wav") #librosa読み込み
	bpm = int(ld.tempo(y, sr)) #テンポの解析
	onset_times = ld.onset_analysis(y, sr) #オンセットの検出
	times = np.insert(onset_times, 0 , 0) #0秒目を追加

	array = [] 

	for i in range(len(times)-1): #配列に音名と音の長さのデータを入れていく。←石本くんにはここにAIを組み込んでほしい。そして判別したデータを配列に追加してほしい。
		if i == len(times):
			a, sr2 = librosa.load("audio/1.wav", offset=times[i])
			d = ld.note_analyis(a, sr2)
			y = du.duration_tempo(bpm, librosa.get_duration(a, sr2) - times[i])
			array.append([d, y])
		else:
			a, sr2 = librosa.load("audio/1.wav", offset=times[i], duration=times[i+1] - times[i])
			d = ld.note_analyis(a, sr2)
			print(times[i+1] - times[i])
			y = du.duration_tempo(bpm, times[i+1] - times[i])
			array.append([d, y])



	return array #コマンドラインに出力



	
