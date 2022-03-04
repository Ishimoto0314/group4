import numpy as np
import subprocess

def check_note(note, note_count, b_note):
	note_place = {1:["g,", "gis,", "a,", "ais,", "b,", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "c'", "cis'", "d'", "dis'", "e'", "f'"],
	2:["d,", "dis,", "e,", "f,", "fis,", "g,", "gis,", "a,", "ais,", "b,", "c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "c'"],
	3:["a,,", "ais,,", "b,,", "c,", "cis,", "d,", "dis,", "e,", "f,", "fis,", "g,", "gis,", "a,", "ais,", "b,", "c", "cis", "d", "dis", "e", "f", "fis", "g"],
	4:["e,,", "f,,", "fis,,", "g,,", "gis,,", "a,,", "ais,,", "b,,", "c,", "cis,", "d,", "dis,", "e,", "f,", "fis,", "g,", "gis,", "a,", "ais,", "b,", "c", "cis", "d"]}

	notes_dict = {"C1":[50, 50, 50, 0], "E2":[50, 50, 50, 0], "F2":[50, 50, 50, 1], "F#2":[50, 50, 50, 2], "G2":[50, 50, 50, 3], "G#2":[50, 50, 50, 4],
	"A2":[50, 50, 0, 5], "A#2":[50, 50, 1, 6], "B2":[50, 50, 2, 7], "C3":[50, 50, 3, 8],
	"C#3":[50, 50, 4, 9], "D3":[50, 0, 5, 10], "D#3":[50, 1, 6, 11], "E3":[50, 2, 7, 12],
	"F3":[50, 3, 8,13], "F#3":[50, 4, 9, 14], "G3":[0, 5, 10, 15],
	"G#3":[1, 6, 11, 16], "A3":[2, 7, 12, 17], "A#3":[3, 8, 13, 18],
	"B3":[4, 9, 14, 19], "C4":[5, 10, 15, 20], "C#4":[6, 11, 16, 21],
	"D4":[7, 12, 17, 22], "D#4":[8, 13, 18, 50], "E4":[9, 14, 19, 50],
	"F4":[10, 15, 20, 0], "F#4":[11, 16, 21, 0], "G4":[12, 17, 22, 50],
	"G#4":[13, 18, 50, 50], "A4":[14, 19, 50, 50], "A#4":[15, 20, 50, 50], "B4":[16, 21, 50, 50],
	"C5":[17, 22, 50, 50], "C#5":[18, 50, 50, 50], "D5":[19, 50, 50, 50], "D#5":[20, 50, 50, 50], "E5":[21, 50, 50, 50], "F5":[22, 50, 50, 50]}

	r_note = ""

	if note not in notes_dict.keys():
		note = 'C1'

	n = 0

	if note_count == 0:
		for d in notes_dict:
			if note == d:
				notes_num = notes_dict[d].index(min(notes_dict[d]))
				print(notes_dict[d][min(notes_dict[d])])
				r_note = note_place[notes_num + 1][min(notes_dict[d])]
				return r_note, notes_num+1
	else:
		for d in notes_dict:
			if note == d:
				for i in note_place:
					if i == b_note[1]:
						for f in note_place[i]:
							if f == b_note[0]:
								n = note_place[i].index(f) - 1

				array02 = [np.abs(notes_dict[d][0]-n), np.abs(notes_dict[d][1]-n), np.abs(notes_dict[d][2]-n), np.abs(notes_dict[d][3]-n)]
				notes_num = array02.index(min(array02))
				r_note = note_place[notes_num + 1][min(array02)]
				return r_note, notes_num+1


def tab(array, bpm):
	f = open("pdf.ly", "w")
	ly ="""#(define (tie::tab-clear-tied-fret-numbers grob)
   (let* ((tied-fret-nr (ly:spanner-bound grob RIGHT)))
      (ly:grob-set-property! tied-fret-nr 'transparent #t)))

\\version "2.14.0"
\\paper {
   indent = #0
   print-all-headers = ##t
   ragged-right = ##f
   ragged-bottom = ##t
}
\\layout {
   \\context { \\Score
      \\override MetronomeMark #'padding = #'5
   }
   \\context { \\Staff
      \\override TimeSignature #'style = #'numbered
      \\override StringNumber #'transparent = ##t
   }
   \\context { \\TabStaff
      \\override TimeSignature #'style = #'numbered
      \\override Stem #'transparent = ##f
      \\override Beam #'transparent = ##f
      \\override Tie  #'after-line-breaking = #tie::tab-clear-tied-fret-numbers
   }
   \\context { \\StaffGroup
      \\consists "Instrument_name_engraver"
   }
}
TrackAVoiceAMusic = #(define-music-function (parser location inTab) (boolean?)
#{
	"""

	ly += "\\tempo 4=" + str(bpm)

	ly += """
	\\clef #(if $inTab "tab" "treble_8")
	\\key c \\major
	\\time 4/4
	\\oneVoice

	"""

	note_count = 0
	note_array = ['t', 0]
	for i in range(len(array)):
			text = "<"
			note, num01 = check_note(array[i][0], note_count, note_array)
			note_array = [note, num01]
			text += note + "\\" + str(num01) + ">" + str(array[i][1]) + " "
			ly += text
			note_count += 1

	ly += """
	\\bar "|."
	\\pageBreak
#})
TrackAVoiceBMusic = #(define-music-function (parser location inTab) (boolean?)
#{
#})
TrackALyrics = \\lyricmode {
   \\set ignoreMelismata = ##t
   
   \\unset ignoreMelismata
}
TrackAStaff = \\new Staff <<
   \\context Voice = "TrackAVoiceAMusic" {
      \removeWithTag #'chords
      \removeWithTag #'texts
      \\TrackAVoiceAMusic ##f
   }
   \\context Voice = "TrackAVoiceBMusic" {
      \\removeWithTag #'chords
      \removeWithTag #'texts
      \\TrackAVoiceBMusic ##f
   }
>>
TrackATabStaff = \\new TabStaff \\with { stringTunings = #`( ,(ly:make-pitch -2 4 NATURAL) ,(ly:make-pitch -2 1 NATURAL) ,(ly:make-pitch -3 5 NATURAL) ,(ly:make-pitch -3 2 NATURAL) ) } <<
   \\context TabVoice = "TrackAVoiceAMusic" {
      \\removeWithTag #'chords
      \\removeWithTag #'texts
      \\TrackAVoiceAMusic ##t
   }
   \\context TabVoice = "TrackAVoiceBMusic" {
      \\removeWithTag #'chords
      \\removeWithTag #'texts
      \\TrackAVoiceBMusic ##t
   }
>>
TrackAStaffGroup = \\new StaffGroup <<
   \\TrackATabStaff
>>
\\score {
   \\TrackAStaffGroup
   \\header {
      title = "" 
      composer = "" 
   }
}

"""

	f.write(ly)
	f.close()

	cmd = "lilypond pdf.ly"
	p = subprocess.Popen(cmd.split(), shell=True)
