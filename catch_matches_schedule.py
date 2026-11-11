import requests
from bs4 import BeautifulSoup
import csv

entered_date = input("Enter the date (MM/DD/YYYY): ")
req_page = requests.get(f'https://www.yallakora.com/matches-center?date={entered_date}')

def main(req_page):
    src = req_page.content
    soup = BeautifulSoup(src, 'lxml')
    list_of_matches = []
    championships = soup.find_all('div', {'class': 'matchCard'})
    
    def get_match_details(championship):
        championship_name = championship.contents[1].find('h2').text.strip()
        matches = championship.contents[3].find_all('div', {'class': 'liItem'})

        matches_length = len(matches)
        for i in range(matches_length):
            
            round = matches[i].find('div', {'class': 'date'}).text.strip()
            teamA = matches[i].find('div', {'class': 'teamA'}).text.strip()
            teamB = matches[i].find('div', {'class': 'teamB'}).text.strip()

            # Get Match Score
            score = matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            if len(score) == 2:
                s1 = score[0].text.strip()
                s2 = score[1].text.strip()
                if s1.isdigit() and s2.isdigit():
                    score_format = f'{s1} x {s2}'
                else:
                    score_format = 'لم تُلعب المباراة بعد'
            else:
                score_format = 'لم تُلعب المباراة بعد'
                
            # Get Match Time
            match_time = matches[i].find('span', {'class': 'time'}).text.strip()

            # Add Match Details to List
            list_of_matches.append({'البطولة': championship_name, 'الجولة': round,
                            'التاريخ': entered_date, 'الوقت': match_time,
                            'الفريق الأول': teamA, 'الفريق الثاني': teamB,
                            'النتيجة': score_format})

            print(list_of_matches[i])

    for i in range(len(championships)):
        get_match_details(championships[i])

    # Save Data to a CSV file
    if not list_of_matches:
        print(f"No matches found for the entered date: {entered_date}")
        return
    
    keys = list_of_matches[0].keys()

    with open(rf'D:\Work\Web Scraping Projects\Matches_Schedule\Matches_{entered_date.replace("/", "-")}.csv', 'w', encoding='utf-8-sig', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_matches)
        print(f"Data saved to Matches_{entered_date.replace('/', '-')}.csv")

main(req_page)