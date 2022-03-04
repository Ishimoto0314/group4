def check_tab(array):
	if array[0] 


def tab(array, bpm):
	ly ="""
		\\new TabStaff \\with {
		stringTunings = #bass-tuning
	} {
		
		\\tempo 4=
	"""

	ly += bpm

	ly += """
	\\relative {

	"""


	for i in range(len(array)):
		if i == 0:
			