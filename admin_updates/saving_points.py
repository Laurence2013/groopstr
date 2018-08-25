from players.models import *

class Saving_Points:
    def save_points(self, goals_player, goals, player_id):
        goals_player_dict = {}
        for i in range(0,len(goals)):
            goals_player_dict = {
                'player_id': player_id[i],
                'points': goals[i],
            }
            goals_player.append(goals_player_dict)

        week_no = Goals_table.objects.filter(week_no_id_id = goals_player[0].get('week_no')).values('week_no_id_id', 'player_id')
        week_index = 0
        for j in range(1, len(goals_player)):
            if int(goals_player[0].get('week_no')) == week_no[week_index].get('week_no_id_id') and int(goals_player[j].get('player_id')) == week_no[week_index].get('player_id'):
                Goals_table.objects.filter(week_no_id_id = goals_player[0].get('week_no'), player_id = int(goals_player[j].get('player_id'))).update(points = goals_player[j].get('points'))
            else:
                return False
            week_index += 1
        return True
