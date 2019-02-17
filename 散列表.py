vote={}
def check_vote(name):
	if vote.get(name):
		print("勾勾")
	else:
		vote.setdefault(name,name)
		print("xx")

while True:
	name=input("輸入名子")
	check_vote(name)