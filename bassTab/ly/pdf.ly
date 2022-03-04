
#(define (tie::tab-clear-tied-fret-numbers grob)
   (let* ((tied-fret-nr (ly:spanner-bound grob RIGHT)))
      (ly:grob-set-property! tied-fret-nr 'transparent #t)))

\version "2.14.0"
\paper {
   indent = #0
   print-all-headers = ##t
   ragged-right = ##f
   ragged-bottom = ##t
}
\layout {
   \context { \Score
      \override MetronomeMark #'padding = #'5
   }
   \context { \Staff
      \override TimeSignature #'style = #'numbered
      \override StringNumber #'transparent = ##t
   }
   \context { \TabStaff
      \override TimeSignature #'style = #'numbered
      \override Stem #'transparent = ##f
      \override Beam #'transparent = ##f
      \override Tie  #'after-line-breaking = #tie::tab-clear-tied-fret-numbers
   }
   \context { \StaffGroup
      \consists "Instrument_name_engraver"
   }
}
TrackAVoiceAMusic = #(define-music-function (parser location inTab) (boolean?)
#{
	\tempo 4=136
	\clef #(if $inTab "tab" "treble_8")
	\key c \major
	\time 4/4
	\oneVoice

	<e,,\4>1 <f,,\4>16 <e,,\4>8 <f,,\4>16 <e,,\4>16 <f,,\4>16 <e,,\4>8 <f,,\4>16 <e,,\4>16 <f,,\4>16 <g,,\4>16 <fis,,\4>16 <f,,\4>16 <e,,\4>4 <f,,\4>16 <f,,\4>16 <b,\1>32 <gis,\1>16 <d,\2>16 <cis,\3>16 <dis,\2>8 <e,\2>8 <dis,\2>8 <e,\2>16 <e,\2>16 <ais,,\3>16 <e,,\4>32 <f,,\4>16 <e,,\4>16 <f,,\4>8 <g,,\4>8 <fis,,\4>16 <f,,\4>8 <e,,\4>16 <f,,\4>16 <e,,\4>16 <f,,\4>16 <e,,\4>16 <f,,\4>8 <e,,\4>8 <f,,\4>16 <e,,\4>16 <dis,\2>8 <c,\3>16 <a,\1>16 <dis,\2>32 <e,,\4>16 <f,\2>16 <f,,\4>8 <e,\2>8 <dis,\2>16 <e,\2>16 <dis,\2>16 
	\bar "|."
	\pageBreak
#})
TrackAVoiceBMusic = #(define-music-function (parser location inTab) (boolean?)
#{
#})
TrackALyrics = \lyricmode {
   \set ignoreMelismata = ##t
   
   \unset ignoreMelismata
}
TrackAStaff = \new Staff <<
   \context Voice = "TrackAVoiceAMusic" {
      emoveWithTag #'chords
      emoveWithTag #'texts
      \TrackAVoiceAMusic ##f
   }
   \context Voice = "TrackAVoiceBMusic" {
      \removeWithTag #'chords
      emoveWithTag #'texts
      \TrackAVoiceBMusic ##f
   }
>>
TrackATabStaff = \new TabStaff \with { stringTunings = #`( ,(ly:make-pitch -2 4 NATURAL) ,(ly:make-pitch -2 1 NATURAL) ,(ly:make-pitch -3 5 NATURAL) ,(ly:make-pitch -3 2 NATURAL) ) } <<
   \context TabVoice = "TrackAVoiceAMusic" {
      \removeWithTag #'chords
      \removeWithTag #'texts
      \TrackAVoiceAMusic ##t
   }
   \context TabVoice = "TrackAVoiceBMusic" {
      \removeWithTag #'chords
      \removeWithTag #'texts
      \TrackAVoiceBMusic ##t
   }
>>
TrackAStaffGroup = \new StaffGroup <<
   \TrackATabStaff
>>
\score {
   \TrackAStaffGroup
   \header {
      title = "" 
      composer = "" 
   }
}

