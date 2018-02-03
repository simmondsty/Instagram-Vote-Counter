import string
import io

chars_to_check = [u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H']

record_dictionary = {}

for char in chars_to_check:
	record_dictionary[char] = 0

users = {}

with io.open("COMP_TESTING.txt", mode="r", encoding="utf-8") as infile:

	for line in infile.read().split('\n'):

		capitals = ''.join([char for char in line if char in chars_to_check])

		if len(capitals) > 0:

			copyend = line.find(capitals[0])
			user = line[0:copyend]

			if not(user in users.keys()):

				users[user] = 0
				record_dictionary[capitals[0]] += 1

			else:
				users[user] += 1

max_votes = 0
winning_character = ''

max_votes = 0

for user in users:
	if users[user] > max_votes:
		max_votes = users[user]

print max_votes

vote_amounts = {}

for vote_amount in range(max_votes):
	vote_amounts[str(vote_amount + 1)] = 0
	for user in users:
		if users[user] == vote_amount:
			vote_amounts[str(vote_amount + 1)] += 1

for vote_amount in vote_amounts.keys():
	print '%s people voted %s times' % (vote_amounts[vote_amount], vote_amount)

print 'In total, %s users voted' % (str(len(users)))

for key in record_dictionary.keys():

	print 'Letter %s received %s votes' % (key, record_dictionary[key])

	if record_dictionary[key] > max_votes:
		max_votes = record_dictionary[key]
		winning_character = key

print 'The winning character was %s, with %s votes' % (winning_character, str(max_votes))			
