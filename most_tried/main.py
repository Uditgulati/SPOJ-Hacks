import sys
import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen



def get_solved(user):
	page = requests.get("http://www.spoj.com/users/"+user)
	soup = BeautifulSoup(page.content, 'html.parser')

	problems = []

	table = soup.find(class_="table table-condensed")

	if table is None:
		return

	for entity in table.find_all('td'):
		#print(entity.get_text())
		text = entity.get_text().strip()

		if text:
			problems.append(text)

	#print(problems)

	return problems


def get_tried(user):
	page = requests.get("http://www.spoj.com/users/"+user)
	soup = BeautifulSoup(page.content, 'html.parser')

	problems = []

	try:
		table = soup.find_all(class_="table")[1]
	except IndexError:
		return problems

	for entity in table.find_all('td'):
		#print(entity.get_text())
		text = entity.get_text().strip()

		if text:
			problems.append(text)

	#print(problems)

	return problems


def print_list():
	num = sys.argv[1]

	invalid_users = []

	users = [line.rstrip('\n') for line in open('users.txt')]

	dict1, dict2, dict3 = {}, {}, {}

	for user in users:	

		solved = get_solved(user)
		if solved is None:
			invalid_users.append(user)
			continue

		tried = get_tried(user)

		for problem in solved:
			if problem in dict1:
				dict1[problem] += 1
			else:
				dict1[problem] = 1

			if problem in dict3:
				dict3[problem] += 1
			else:
				dict3[problem] = 1

		for problem in tried:
			if problem in dict2:
				dict2[problem] += 1
			else:
				dict2[problem] = 1

			if problem in dict3:
				dict3[problem] += 1
			else:
				dict3[problem] = 1

	for problem in dict3.keys():

		num1, num2 = 0, 0

		try:
			num1 = dict1[problem]
		except KeyError:
			num1 = 0

		try:
			num2 = dict2[problem]
		except KeyError:
			num2 = 0

		print(problem + ' - solved by ' + str(num1) + ' and tried by ' + str(num2) + '.')

	print()

	for user in invalid_users:
		print(user + " is invalid.")

if __name__ == '__main__':
	print_list()