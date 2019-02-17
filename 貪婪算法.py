states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) #要覆蓋的州
#廣播清單
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set() # 存最終廣播台

while states_needed:  # 只要沒有全部覆蓋完就繼續
  best_station = None 
  states_covered = set()  # 存覆蓋的州
  for station, states in stations.items(): # items()存廣播台跟相對應的州
    covered = states_needed & states  # 集合的交集，判斷還未覆蓋的州與此廣播台的交集個數
    if len(covered) > len(states_covered): # 如果當前廣播焦急個數多於當前要覆蓋的州
      best_station = station  # 替換最優的廣播
      states_covered = covered  # 替換已經覆蓋的州

  states_needed -= states_covered # 從要覆蓋的去減已經附蓋過的(集合相減)
    print ('states_needed:',states_needed)
  final_stations.add(best_station) # 貼加最好的廣播

print (final_stations)