import requests as r 
get_api = r.get('https://foxes90-prempundit.herokuapp.com/players').json()
print(get_api)


# get data
# produce teams from data
# fill teams with players
# cycle thru positions for team to see if they have met the mandate

class Team():
    pass

    def player_data():
        get_api = r.get('https://foxes90-prempundit.herokuapp.com/players').json()
        print(get_api)
        print(get_api['PLayers'][0]['first_name'])
            # make this based off positions/positions are what the formations are based off of.
        pass


    def UI():
        player = []
        print('What is your team name?')
        user_input = input('')
        player.append(user_input)
        pass
class Players():

    def __init__(self) -> None:
        pass
    





