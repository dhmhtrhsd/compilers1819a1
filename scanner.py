"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """

	if pos<0 or pos>=len(text): return None

	c = text[pos]

	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις

	return c	# anything else



def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""

	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None


	while True:

		c = getchar(text,pos)	# get next char (category)

		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char

			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos

		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos

			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos


# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 's0': {'0':'s1', '1':'s1', '2':'s1', '3':'s14'},
       		's1': {'0':'s2', '1':'s2', '2':'s2', '3':'s2', '4':'s2', '5':'s2', '6':'s2', '7':'s2', '8':'s2', '9':'s2'},
		's2': {'0':'s3'},
		's3': {'0':'s4', '1':'s4', '2':'s4', '3':'s4', '4':'s4', '5':'s4', '6':'s4', '7':'s4', '8':'s4', '9':'s4'},
		's4': {'0':'s5', '1':'s5', '2':'s5', '3':'s5', '4':'s5', '5':'s5', '6':'s5', '7':'s5', '8':'s5', '9':'s5'},
		's5': {'G':'s6', 'K':'s12', 'M': 's9'},
		's6': {'0':'s7', '1':'s7', '2':'s7', '3':'s7', '4':'s7', '5':'s7', '6':'s7', '7':'s7', '8':'s7', '9':'s7'},
		's7': {'0':'s8', '1':'s8', '2':'s8', '3':'s8', '4':'s8', '5':'s8', '6':'s8', '7':'s8', '8':'s8', '9':'s8'},
		's8': {'K':'s12', 'M': 's9'},
		's12': {'T':'s13'},
		's9': {'P':'s10'},
		's10': {'S':'s11'},
		's14': {'0':'s2', '1':'s2', '2':'s2', '3':'s2', '4':'s2', '5':'s2'},
     		  }

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = {'s13':'WIND_TOKEN',
	   's11':'WIND_TOKEN'
	  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
