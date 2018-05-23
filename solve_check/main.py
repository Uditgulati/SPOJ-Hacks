import sys
import os
import requests
from bs4 import BeautifulSoup



def get_solved(user):
	page = requests.get("http://www.spoj.com/users/"+user)
	soup = BeautifulSoup(page.content, 'html.parser')

	problems = []

	table = soup.find(class_="table table-condensed")

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

	table = soup.find_all(class_="table")[1]

	for entity in table.find_all('td'):
		#print(entity.get_text())
		text = entity.get_text().strip()

		if text:
			problems.append(text)

	#print(problems)

	return problems


def check_profile():
	problem = sys.argv[1]

	users = [line.rstrip('\n') for line in open('users.txt')]
	for user in users:
		
		solved = get_solved(user)
		tried = get_tried(user)

		if problem in solved:
			print(user + " has solved " + problem + ".")
		elif problem in tried:
			print(user + " has tried " + problem + " but hasn't solved it yet.")

if __name__ == '__main__':
	check_profile()