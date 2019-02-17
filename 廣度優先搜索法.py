from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    #建立佇列
	search_queue=deque()
    #初始化佇列
	search_queue+=graph[name]
    #記錄已經搜尋過的人
	searched=[]
    #只要佇列不空就一直搜索
	while len(search_queue) > 0:
        #取出佇列中最左邊的
		person=search_queue.popleft()
        # 只要他沒有被搜尋過就丟進去
		if person not in searched:
            # 判斷是不是seller
			if person_is_seller(person):
				print(person+" is a seller")
				return True
			else:
                # 不是seller,所以將他的朋友都加入佇列
				search_queue+=graph[person]
                # 標記這個人已經被找過了
				search_queue.append(person)
	return False
# 判定是不是seller，規則自訂
def person_is_seller(person):
	if person[-1] == "m":
		return True
	else:
		return False

search("you")