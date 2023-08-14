import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt


teams = {12: 'Sunrisers Hyderabad', 
4: 'Kolkata Knight Riders', 3: 'Gujarat Lions', 
8: 'Pune Warriors', 
1: 'Delhi Daredevils', 
7: 'Mumbai Indians', 5: 'Kochi Tuskers Kerala', 
0: 'Chennai Super Kings', 10: 'Rising Pune Supergiant', 
1: 'Delhi Capitals', 9: 'Royal Challengers Bangalore', 
10: 'Rising Pune Supergiants', 6: 'Kings XI Punjab', 
11: 'Rajasthan Royals', 2: 'Deccan Chargers'}

def imp_data():
    df = pd.read_csv("ipl_ipl.csv")
    # print(df.shape)

    mng_data = df.drop(['id', 'neutral_venue', 'season', 'date','eliminator','method',
    'player_of_match', 'umpire1','venue','loser','result_margin', 'umpire2','result'],axis=1)

    mng_data = mng_data.dropna()

    # print(mng_data.shape)
    # print(mng_data.columns)

    return mng_data

def labelEncoding(data):

    data.winner[data.winner == "Chennai Super Kings"] = 0
    data.winner[data.winner == "Delhi Daredevils"] = 1
    data.winner[data.winner == "Delhi Capitals"] = 1
    data.winner[data.winner == "Deccan Chargers"] = 2
    data.winner[data.winner == "Gujarat Lions"] = 3
    data.winner[data.winner == "Kolkata Knight Riders"] = 4	 
    data.winner[data.winner == "Kochi Tuskers Kerala"] = 5
    data.winner[data.winner == "Kings XI Punjab"] = 6
    data.winner[data.winner == "Mumbai Indians"] = 7
    data.winner[data.winner == "Pune Warriors"] = 8
    data.winner[data.winner == "Royal Challengers Bangalore"] = 9
    data.winner[data.winner == "Rising Pune Supergiant"] = 10
    data.winner[data.winner == "Rising Pune Supergiants"] = 10
    data.winner[data.winner == "Rajasthan Royals"] = 11
    data.winner[data.winner == "Sunrisers Hyderabad"] = 12	 
    
    data.team1[data.team1 == "Chennai Super Kings"] = 0 
    data.team1[data.team1 == "Delhi Daredevils"] = 1
    data.team1[data.team1 == "Delhi Capitals"] = 1
    data.team1[data.team1 == "Deccan Chargers"] = 2
    data.team1[data.team1 == "Gujarat Lions"] = 3
    data.team1[data.team1 == "Kolkata Knight Riders"] = 4	 
    data.team1[data.team1 == "Kochi Tuskers Kerala"] = 5
    data.team1[data.team1 == "Kings XI Punjab"] = 6
    data.team1[data.team1 == "Mumbai Indians"] = 7
    data.team1[data.team1 == "Pune Warriors"] = 8
    data.team1[data.team1 == "Royal Challengers Bangalore"] = 9
    data.team1[data.team1 == "Rising Pune Supergiant"] = 10
    data.team1[data.team1 == "Rising Pune Supergiants"] = 10
    data.team1[data.team1 == "Rajasthan Royals"] = 11
    data.team1[data.team1 == "Sunrisers Hyderabad"] = 12	 
    
    data.team2[data.team2 == "Chennai Super Kings"] = 0 
    data.team2[data.team2 == "Delhi Daredevils"] = 1
    data.team2[data.team2 == "Delhi Capitals"] = 1
    data.team2[data.team2 == "Deccan Chargers"] = 2
    data.team2[data.team2 == "Gujarat Lions"] = 3
    data.team2[data.team2 == "Kolkata Knight Riders"] = 4	 
    data.team2[data.team2 == "Kochi Tuskers Kerala"] = 5
    data.team2[data.team2 == "Kings XI Punjab"] = 6
    data.team2[data.team2 == "Mumbai Indians"] = 7
    data.team2[data.team2 == "Pune Warriors"] = 8
    data.team2[data.team2 == "Royal Challengers Bangalore"] = 9
    data.team2[data.team2 == "Rising Pune Supergiant"] = 10
    data.team2[data.team2 == "Rising Pune Supergiants"] = 10
    data.team2[data.team2 == "Rajasthan Royals"] = 11
    data.team2[data.team2 == "Sunrisers Hyderabad"] = 12	
    
    data.toss_winner[data.toss_winner == "Chennai Super Kings"] = 0 
    data.toss_winner[data.toss_winner == "Delhi Daredevils"] = 1
    data.toss_winner[data.toss_winner == "Delhi Capitals"] = 1
    data.toss_winner[data.toss_winner == "Deccan Chargers"] = 2
    data.toss_winner[data.toss_winner == "Gujarat Lions"] = 3
    data.toss_winner[data.toss_winner == "Kolkata Knight Riders"] = 4	 
    data.toss_winner[data.toss_winner == "Kochi Tuskers Kerala"] = 5
    data.toss_winner[data.toss_winner == "Kings XI Punjab"] = 6
    data.toss_winner[data.toss_winner == "Mumbai Indians"] = 7
    data.toss_winner[data.toss_winner == "Pune Warriors"] = 8
    data.toss_winner[data.toss_winner == "Royal Challengers Bangalore"] = 9
    data.toss_winner[data.toss_winner == "Rising Pune Supergiant"] = 10
    data.toss_winner[data.toss_winner == "Rising Pune Supergiants"] = 10
    data.toss_winner[data.toss_winner == "Rajasthan Royals"] = 11
    data.toss_winner[data.toss_winner == "Sunrisers Hyderabad"] = 12	
    
    data.toss_decision[data.toss_decision == "bat"] = 1
    data.toss_decision[data.toss_decision == "field"] = 2
    
    data.city[data.city == "Hyderabad"] = 1
    data.city[data.city == "Pune"] = 2
    data.city[data.city == "Rajkot"] = 3
    data.city[data.city == "Indore"] = 4
    data.city[data.city == "Bangalore"] = 5
    data.city[data.city == "Mumbai"] = 6
    data.city[data.city == "Kolkata"] = 7
    data.city[data.city == "Delhi"] = 8
    data.city[data.city == "Chandigarh"] = 9
    data.city[data.city == "Kanpur"] = 10
    data.city[data.city == "Jaipur"] = 11
    data.city[data.city == "Chennai"] = 12
    data.city[data.city == "Cape Town"] = 13
    data.city[data.city == "Port Elizabeth"] = 14
    data.city[data.city == "Durban"] = 15
    data.city[data.city == "Centurion"] = 16
    data.city[data.city == "East London"] = 17
    data.city[data.city == "Johannesburg"] = 18
    data.city[data.city == "Kimberley"] = 19
    data.city[data.city == "Bloemfontein"] = 20
    data.city[data.city == "Ahmedabad"] = 21
    data.city[data.city == "Cuttack"] = 22
    data.city[data.city == "Nagpur"] = 23
    data.city[data.city == "Dharamsala"] = 24
    data.city[data.city == "Kochi"] = 25
    data.city[data.city == "Visakhapatnam"] = 26
    data.city[data.city == "Raipur"] = 27
    data.city[data.city == "Ranchi"] = 28
    data.city[data.city == "Abu Dhabi"] = 29
    data.city[data.city == "Sharjah"] = 30
    data.city[data.city == "nan"] = 31
    data.city[data.city == "Mohali"] = 32
    data.city[data.city == "Bengaluru"] = 33
    data.city[data.city == "Dubai"] = 34

    # data.venue[data.venue == "Eden Gardens"] = 1
    # data.venue[data.venue == "M Chinnaswamy Stadium"] = 2
    # data.venue[data.venue == "Wankhede Stadium"] = 3
    # data.venue[data.venue == "Feroz Shah Kotla"] = 4
    # data.venue[data.venue == "Rajiv Gandhi International Stadium, Uppal"] = 5
    # data.venue[data.venue == "MA Chidambaram Stadium, Chepauk"] = 6
    # data.venue[data.venue == "Sawai Mansingh Stadium"] = 7
    # data.venue[data.venue == "Punjab Cricket Association Stadium, Mohali"] = 8
    # data.venue[data.venue == "Maharashtra Cricket Association Stadium"] = 9
    # data.venue[data.venue == "Subrata Roy Sahara Stadium"] = 10
    # data.venue[data.venue == "Dr DY Patil Sports Academy"] = 11
    # data.venue[data.venue == "Kingsmead"] = 12
    # data.venue[data.venue == "Punjab Cricket Association IS Bindra Stadium, Mohali"] = 13
    # data.venue[data.venue == "SuperSport Park"] = 14
    # data.venue[data.venue == "Sardar Patel Stadium, Motera"] = 15
    # data.venue[data.venue == "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium"] = 16
    # data.venue[data.venue == "Brabourne Stadium"] = 17
    # data.venue[data.venue == "Saurashtra Cricket Association Stadium"] = 18
    # data.venue[data.venue == "Holkar Cricket Stadium"] = 19
    # data.venue[data.venue == "Himachal Pradesh Cricket Association Stadium"] = 20
    # data.venue[data.venue == "Rajiv Gandhi Intl. Cricket Stadium"] = 21
    # data.venue[data.venue == "M. A. Chidambaram Stadium"] = 22
    # data.venue[data.venue == "New Wanderers Stadium"] = 23
    # data.venue[data.venue == "Feroz Shah Kotla Ground"] = 24
    # data.venue[data.venue == "Barabati Stadium"] = 25
    # data.venue[data.venue == "M. Chinnaswamy Stadium"] = 26
    # data.venue[data.venue == "M.Chinnaswamy Stadium"] = 26
    # data.venue[data.venue == "St George's Park"] = 27
    # data.venue[data.venue == "Newlands"] = 28
    # data.venue[data.venue == "JSCA International Stadium Complex"] = 29
    # data.venue[data.venue == "Sheikh Zayed Stadium"] = 30
    # data.venue[data.venue == "Dubai International Cricket Stadium"] = 31
    # data.venue[data.venue == "IS Bindra Stadium"] = 32
    # data.venue[data.venue == "Shaheed Veer Narayan Singh International Stadium"] = 32
    # data.venue[data.venue == "Sharjah Cricket Stadium"] = 32
    # data.venue[data.venue == "Nehru Stadium"] = 33
    # data.venue[data.venue == "Green Park"] = 34
    # data.venue[data.venue == "De Beers Diamond Oval"] = 35
    # data.venue[data.venue == "Vidarbha Cricket Association Stadium, Jamtha"] = 36
    # data.venue[data.venue == "Buffalo Park"] = 37
    # data.venue[data.venue == "OUTsurance Oval"] = 38
    # data.venue[data.venue == "ACA-VDCA Stadium"] = 39

    return data

def splitdataset(data):

    x = data.drop(columns="winner",axis=1)
    y = data['winner']

    X_train, X_test, y_train, y_test = train_test_split(x, y)

    # print("Shape of X ",x.shape)
    # print("Shape of Y ",y.shape)
    # print("Shape of X_train",X_train.shape)
    # print("Shape of y_train ",y_train.shape)
    # print("Shape of X_test",X_test.shape)
    # print("Shape of y_test ",y_test.shape)

    return x,y,X_train, X_test, y_train, y_test

def decision_tree(X_train,X_test,y_train,g_e,y_test,team1_no,team2_no,rdf):

    clf_gini = DecisionTreeClassifier(criterion = g_e)
    clf_gini.fit(X_train, y_train)
    y_pred = clf_gini.predict(X_test)
    r_pred = clf_gini.predict(rdf)
    # print(y_pred)
    # print("real time data::",r_pred)

    a = accuracy_score(y_test,y_pred)*100

    return a
    
def svm_model(X_train,X_test,y_train,y_test,rdf):

    clf_svc = SVC()
    clf_svc.fit(X_train, y_train)
    y_pred = clf_svc.predict(X_test)
    r_pred = clf_svc.predict(rdf)
    # print(y_pred)
    # print("real time data::",r_pred)

    b = accuracy_score(y_test,y_pred)*100

    return b

def knn_model(X_train,X_test,y_train,y_test,rdf):

    clf_knn = KNeighborsClassifier(n_neighbors=7)
    clf_knn.fit(X_train, y_train)
    y_pred = clf_knn.predict(X_test)
    r_pred = clf_knn.predict(rdf)
    # print(y_pred)
    # print("real time data::",r_pred)
    
    c = accuracy_score(y_test,y_pred)*100

    return c

def rf_model(X_train,X_test,y_train,y_test,rdf):

    clf_rf = RandomForestClassifier(n_estimators = 1000)
    clf_rf.fit(X_train, y_train)
    y_pred = clf_rf.predict(X_test)
    r_pred = clf_rf.predict(rdf)
    # print(y_pred)
    # print("real time data::",r_pred)

    d = accuracy_score(y_test,y_pred)*100
    return d
# def test(aa):
#     print(aa)
def recdata(t1sel,t2sel,tsdici,selct,seltswin):
    mng_data = imp_data()

    mng_data = labelEncoding(mng_data)

    # print(mng_data.winner.unique())
    mng_data = mng_data.dropna()

    mng_data.winner = mng_data.winner.astype('int')
    mng_data.team1 = mng_data.team1.astype('int')
    mng_data.team2 = mng_data.team2.astype('int')
    mng_data.toss_winner = mng_data.toss_winner.astype('int')
    mng_data.toss_decision = mng_data.toss_decision.astype('int')
    mng_data.city = mng_data.city.astype('int')
    # mng_data.venue = mng_data.venue.astype('int')

    # print("========================================")
    # for i in teams:
    #     print(i,teams[i])

    # # print(mng_data.head())
    # print("========================================")

    # # team1_no = int(input("Enter first team::"))
    # # team2_no = int(input("Enter sec team::"))
    # print("========================================")

    team1_no = t1sel
    team2_no = t2sel

    rdata = {
        'city':[selct],
        'team1':[t1sel],
        'team2':[t2sel],
        'toss_winner':[seltswin],
        'toss_decision':[tsdici]
    }

    rdf = pd.DataFrame(rdata)
    print(rdf)
    data1 = mng_data[(mng_data['team1'] == team1_no) & (mng_data['team2'] == team2_no)]
    data2 = mng_data[(mng_data['team1'] == team2_no) & (mng_data['team2'] == team1_no)]

    mng_data = pd.concat([data1,data2],axis=0)

    X , Y, X_train,X_test, y_train, y_test = splitdataset(mng_data)

    print("========================================")

    print("Teams :: ",teams[team1_no]," VS ",teams[team2_no])
    print("========================================")

    a = decision_tree(X_train,X_test,y_train,"gini",y_test,team1_no,team2_no,rdf)
    print("========================================")
    b = decision_tree(X_train,X_test,y_train,"entropy",y_test,team1_no,team2_no,rdf)
    print("========================================")
    c = svm_model(X_train,X_test,y_train,y_test,rdf)
    print("========================================")
    d = knn_model(X_train,X_test,y_train,y_test,rdf)
    print("========================================")
    e = rf_model(X_train,X_test,y_train,y_test,rdf)
    print("========================================")

    models = {'a':a,'b':b,'c':c,'d':d,'e':e}

    ans = max(models)

    print("Max_accuracy::",ans)

    for i in models:
        if models[i] == ans:
            print("Selected model::",i)
            break

    
    if i == 'a':
        clf_gini = DecisionTreeClassifier(criterion = "gini")
        clf_gini.fit(X_train, y_train)
        rpred=clf_gini.predict(rdf)
        print("predict answer:",rpred)
    elif i == 'b':
        clf_et = DecisionTreeClassifier(criterion = "entropy")
        clf_et.fit(X_train, y_train)
        rpred=clf_et.predict(rdf)
        print("predict answer:",rpred)
    elif i == 'c':
        clf_svc = SVC()
        clf_svc.fit(X_train, y_train)
        rpred=clf_svc.predict(rdf)
        print("predict answer:",rpred)
    elif i== 'd':
        clf_knn = KNeighborsClassifier(n_neighbors=7)
        clf_knn.fit(X_train, y_train)
        rpred=clf_knn.predict(rdf)
        print("predict answer:",rpred)
    elif i== 'e':
        clf_rf = RandomForestClassifier(n_estimators = 1000)
        clf_rf.fit(X_train, y_train)
        rpred=clf_rf.predict(rdf)
        print("predict answer:",rpred)

    return rpred
# if __name__=="__main__":
#     main()