\version "2.22.1"
\new Voice \with {
\	omit StringNumber
} {
	\clef "bass_8"
	\relative {
		c,4 d e f c d e f
	}
}
\new TabStaff \with {
	stringTunings = #bass-tuning
} {
	\relative {
		c,4 d e f c d e f
	}
}