import vk
from random import randint as rnd
from time import sleep

APPID = 5496064
LOGIN = 79992154597
PASS = "studiosovapoledance21022015"
SCOPES = "wall, groups, friends, messages"
try:
	session = vk.AuthSession(app_id = APPID, user_login = LOGIN, user_password = PASS, scope = SCOPES)
	vkapi = vk.API(session)
except:
	print("AuthError")
else:
	with open("test.txt", "r") as people:
		peopleList = people.readlines()
	victims = peopleList
	peopleAmount = len(peopleList)
	checkText = ["id {0} : isn't friend", "id {0} : outcoming request was", "id {0} : incoming request was", "id {0} : already friend"]
	friendRequestText = ["0", "id {0} Friend request sent", "id {0} Friend request approved"]
	approveFriends = vkapi.friends.areFriends(user_ids=victims)
	for checkPerson in approveFriends:
		checkPersonID = checkPerson["uid"]
		if not(checkPerson["friend_status"]):
			friendRequest = vkapi.friends.add(user_id=checkPersonID)
			print(friendRequestText[friendRequest].format(checkPersonID))
			with open("friendRequestMargarita_log.txt", "a") as log:
				log.write(str(friendRequestText[friendRequest].format(checkPersonID)) + "\n")
		else:
			print(checkText[checkPerson["friend_status"]].format(checkPersonID))
			with open("friendRequestMargarita_log.txt", "a") as log:
				log.write(checkText[checkPerson["friend_status"]].format(checkPersonID) + "\n")
		sleepTime = rnd (2,4)
		sleep(sleepTime)
print("Compleeeeeteeeeee ;)")