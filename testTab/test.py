

f = open("test.ly", "w")

ly = "\\version \"2.22.1\"\n\\new Voice \\with {\n\\	omit StringNumber\n} {\n	\\clef \"bass_8\"\n	\\relative {\n		c,4 d e f c d e f\n	}\n}\n\\new TabStaff \\with {\n	stringTunings = #bass-tuning\n} {\n	\\relative {\n		c,4 d e f c d e f\n	}\n}"

f.write(ly)

f.close()