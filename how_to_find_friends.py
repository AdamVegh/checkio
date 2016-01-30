__author__ = 'Vegh Adam'


def check_connection(network, first, second):
    list_teams, list_friends = [], [set(friends.split('-')) for friends in network]
    while list_friends != []:
        last_team = list_friends.pop()
        for friends in list_friends:
            if friends & last_team != set():
                friends |= last_team
                break
        else:
            list_teams.append(last_team)
    return 1 in [set([first, second]).issubset(team) for team in list_teams]
