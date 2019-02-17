#先定義會用到的資料
#起點
graph={}
graph["start"]={}
graph["start"]["a"]=6
graph["start"]["b"]=2
#a
graph["a"]={}
graph["a"]["fin"]=1
#b
graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5
#終點
graph["fin"]={}
#cost
infinity=float("inf")
costs={}
costs["a"]=6
costs["b"]=2
costs["fin"]=infinity
#parents
parents={}
parents["a"]="start"
parents["b"]="start"
parents["fin"]=None
#tmp
processed=[]

def find_lower_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node in costs:#跑過所有點
        cost=costs[node]
        if cost<lowest_cost and node not in processed:#如果找到更快的路徑，且那個節點定沒有用過
            lowest_cost=cost
            lowest_cost_node=node#就把它設為最低(更新資料)
    return lowest_cost_node

node=find_lower_cost_node(costs)#在還沒處理過的節點找出最快路徑
while node is not None:#這個迴圈將在所有節點都找過後才結束
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():#找遍該節點的鄰居
        new_cost=cost+neighbors[n]
        if costs[n]>new_cost:#如果這條路比較快
            costs[n]=new_cost#就更新表格
            parents[n]=node#同時將該鄰居的父節點設成當前節點
    processed.append(node)#將當前節點設定成已使用過
    node=find_lower_cost_node(costs)#找出接下來要跑的節點並循環
print(costs)
print(parents[parents["fin"]]+"-->"+parents["fin"]+"-->"+"fin")



