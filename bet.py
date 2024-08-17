odds=1/10
min_stake=1000
max_stake=20000
left_players=10
right_players=10
players=''
import soccerdata as ball
import soccer_data_api as api
#the following returns alist of dicts of teams 
epl=api.SoccerDataAPI.english_premier(api)
serie_a=api.SoccerDataAPI.serie_a(api)
bundesliga=api.SoccerDataAPI.bundesliga(api)


print('epl line....................................')

for i in range(20):
    print(epl[i]['team'])
laliga=api.SoccerDataAPI.la_liga(api)

print('laliga line....................................')
for i in range(20):
    print(laliga[i]['team'])


print('serie A line....................................')
for i in range(20):
    print(serie_a[i]['team'])

print('bundesliga line....................................')
for i in range(17):
    print(bundesliga[i]['team'])
# Create a scraper class instance for the 2018/19 Premier League
league = ball.FiveThirtyEight('ENG-Premier League', '1819')


# Fetch data
games = league.read_games()
print(" new error .....................")
print(games)
forecasts = league.read_forecasts()
print(" forecasts .....................")
print(forecasts)
clinches = league.read_clinches()
print(" clinch .....................")
print(clinches)


