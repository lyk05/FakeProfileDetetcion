import pickle
import tweepy                   
# import json
# import csv
# from datetime import date
# from datetime import datetime
# import time
# import re
# Aditya(D3)

def auth_Api():
    api_key = 'PTLIZOQ3WtVdwTmJrmgBtMmq3'
    api_secret_key = 'sK8SSOJ9XlSFPH9oJrQ5Xv68jJYwkIdR8EEsoozoS0LyoEjsVo'
    access_token = '1349672165210255361-v0bxRfaeSTWKoAYyr3hm6HxH0rAKcL'
    access_token_secret = 'E3ggmNifUrdvohzApJJBoDqB3L7WLn56Y6bxwUgQ3kjUF'
    # Aditya(D3)


    # Connect to Twitter API using the secrets
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    # Aditya(D3)
    api = tweepy.API(auth)
    return api



def detect(username,api):
    user_id=username
    try:
        user = api.get_user(user_id)
        
        #use respective path
        Fake_profile_detect = pickle.load(open('G:/LYKOS PROGRESS/MAJOR/New folder/Fake_profile_detector_Dump_model_Rf_.pickle', 'rb'))
        y_pred = Fake_profile_detect.predict([[int(str(user.statuses_count)), int(str(user.followers_count)), int(str(user.friends_count)), int(str(user.favourites_count)), int(str(user.listed_count))]])
        if(y_pred[0]==1):
            print("Real")
        else:
            print("fake")

    except Exception:
        print("No user found ")


def main():
    Api= auth_Api()
    name=input("enter username :- ")
    detect(name,Api)

if __name__ == "__main__":
    main()
