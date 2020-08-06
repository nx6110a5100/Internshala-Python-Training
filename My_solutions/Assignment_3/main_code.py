import score_functions as sf
player_data={'p1':{'name':'Virat Kohli', 'role':'1', 'runs':112, '4':10, '6':0, 'balls':119, 'field':0},'p2':{'name':'du Plessis', 'role':'1', 'runs':120, '4':11, '6':2, 'balls':112, 'field':0},'p3':{'name':'Bhuvneshwar Kumar', 'role':'0', 'wkts':1, 'overs':10, 'runs':71, 'field':1},'p4':{'name':'Yuzvendra Chahal', 'role':'0', 'wkts':2, 'overs':10, 'runs':45, 'field':0},'p5':{'name':'Kuldeep Yadav', 'role':'0', 'wkts':3, 'overs':10, 'runs':34, 'field':0}}

for j in player_data.items():
    if j['role']==1:
        print("Batting score of {} is:".format(j['name']))
        print(sf.batting_score(j['runs'],j['balls'],j['4'],j['6']))
    if j['role']==0:
        print("Bowling score of {} is:".format(j['name']))
        print(sf.bowling_score(j['wkts'],j['overs'],j['runs'],j['field']))
