import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta


def grab_page_data(username:str, password:str):
    URL = "https://scheduling-au3.wfs.cloud/signin/"
    payload = {'task':'signin', 'account':'jaycargroup', 'username': username, 'password': password}
    # Create a webpage session
    with requests.Session() as s:
        # Attempt a login
        p = s.post(URL, data=payload)

        # Check if login was a success
        soup = BeautifulSoup(p.text, 'html.parser')
        user_name = soup.find("li", attrs={'class':'site-branding__meta-username'}).text.strip()
        if user_name:
            return p.text
        else:
            return None

def parse_workdays(page_data:str):
    # Focus on the 'My Shifts' table
    soup = BeautifulSoup(page_data, 'html.parser')
    wd_table = soup.find_all("table", attrs={'class':'table'})[1]
    work_days = wd_table.find_all('td')

    days_dict = {}

    # Append all dates and their times
    for index, day in enumerate(work_days):
        if index % 2 == 0:
            days_dict[day.text.strip()] = work_days[index+1].text.strip()[:-27]

    return days_dict

def str_to_dates(days_dict:dict):

    new_dict = {}

    for date_str in days_dict:
        if date_str == "Today":
            new_dict[str(date.today())] = days_dict[date_str]
        elif date_str == "Tomorrow":
            new_dict[str(date.today() + timedelta(days=1))] = days_dict[date_str]
        else:
            converted_date = datetime.strptime(date_str, "%d/%m").replace(2023).date() # Converts site date format to date object
            new_dict[str(converted_date)] = days_dict[date_str]
    return new_dict

# Test case
if __name__ == "__main__":
    data = grab_page_data('', '')
    with open('output.html', 'r') as f:
        page_data = f.read()
        days_dict = parse_workdays(page_data)
    print(str_to_dates(days_dict))