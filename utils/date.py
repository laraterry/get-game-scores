from datetime import datetime, timedelta

def get_yesterdays_date():
    today = datetime.now() 
    yesterday = today - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')

def get_todays_date():
    today = datetime.now() 
    return today.strftime('%Y-%m-%d')



