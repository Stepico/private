import requests


def getNumDraws(year):
    base_url = 'https://jsonmock.hackerrank.com/api/football_matches'
    session = requests.Session()

    draw_cnt = 0
    page = 1

    while True:
        params = {'year': year, 'page': page}
        response = session.get(base_url, params=params)
        data = response.json()

        matches_data = data['data']
        for match_data in matches_data:
            if match_data['team1goals'] == match_data['team2goals']:
                draw_cnt += 1

        page += 1
        if page > data['total_pages']:
            break

    return draw_cnt


if __name__ == '__main__':
    print(getNumDraws(2011))
    

