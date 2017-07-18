import pandas as pd

link_info = pd.read_csv('../datas/gy_contest_link_info.txt') 
link_top = pd.read_csv('../datas/gy_contest_link_top20170715.txt')
# history_traveltime = pd.read_csv('../datas/gy_contest_link_traveltime_training_data.txt')
# print(history_traveltime)

print(link_top.describe())
print(link_info.describe())


