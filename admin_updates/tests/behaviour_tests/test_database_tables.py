from members.models import *
from players.models import *
class Fixtures_and_Weeks:
    '''
    1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks class
    '''
    def week_fixture_table_00(self):
        Week_table.objects.create(id = 11, week_no = 1, date_updated = '2018-08-17 20:44:40', end_date = '2018-08-11', start_date = '2018-08-05', is_current_week = 0)
        Week_table.objects.create(id = 12, week_no = 2, date_updated = '2018-08-17 20:44:46', end_date = '2018-08-18', start_date = '2018-08-12', is_current_week = 0)
        Week_table.objects.create(id = 13, week_no = 3, date_updated = '2018-08-17 20:44:50', end_date = '2018-08-26', start_date = '2018-08-19', is_current_week = 0)

        Fixtures_table.objects.create(fixture = 'Chelsea vs Fiorentina', date_updated = '2018-08-12 16:47:37', competition = 'cl', date_of_game = '2018-08-08', week_no_id = 11)
        Fixtures_table.objects.create(fixture = 'Chelsea vs Arsenal', date_updated = '2018-08-12 16:47:37', competition = 'pl', date_of_game = '2018-08-10', week_no_id = 11)
        Fixtures_table.objects.create(fixture = 'Liverpool vs Everton', date_updated = '2018-08-12 16:47:37', competition = 'pl', date_of_game = '2018-08-10', week_no_id = 12)

        return Week_table.objects.all().values('id','week_no','start_date','end_date','is_current_week'), Fixtures_table.objects.all().values('id','fixture','competition','date_of_game','week_no_id')

    def week_fixture_table_01(self):
        Week_table.objects.create(id = 11, week_no = 1, date_updated = '2018-08-17 20:44:40', end_date = '2018-08-11', start_date = '2018-08-05', is_current_week = 0)
        Week_table.objects.create(id = 12, week_no = 2, date_updated = '2018-08-17 20:44:46', end_date = '2018-08-18', start_date = '2018-08-12', is_current_week = 0)
        Week_table.objects.create(id = 13, week_no = 3, date_updated = '2018-08-17 20:44:50', end_date = '2018-08-26', start_date = '2018-08-19', is_current_week = 0)

        Fixtures_table.objects.create(fixture = 'Chelsea vs Fiorentina', date_updated = '2018-08-12 16:47:37', competition = 'cl', date_of_game = '2018-08-08', week_no_id = 11)
        Fixtures_table.objects.create(fixture = 'Chelsea vs Arsenal', date_updated = '2018-08-12 16:47:37', competition = 'pl', date_of_game = '2018-08-10', week_no_id = 12)
        Fixtures_table.objects.create(fixture = 'Liverpool vs Everton', date_updated = '2018-08-12 16:47:37', competition = 'pl', date_of_game = '2018-08-10', week_no_id = 12)

        return Week_table.objects.all().values('id','week_no','start_date','end_date','is_current_week'), Fixtures_table.objects.all().values('id','fixture','competition','date_of_game','week_no_id')

    def week_fixture_table_02(self):
        Week_table.objects.create(id = 11, week_no = 1, date_updated = '2018-08-17 20:44:40', end_date = '2018-08-11', start_date = '2018-08-05', is_current_week = 0)
        Week_table.objects.create(id = 12, week_no = 2, date_updated = '2018-08-17 20:44:46', end_date = '2018-08-18', start_date = '2018-08-12', is_current_week = 0)
        Week_table.objects.create(id = 13, week_no = 3, date_updated = '2018-08-17 20:44:50', end_date = '2018-08-26', start_date = '2018-08-19', is_current_week = 0)

        Fixtures_table.objects.create(fixture = 'Chelsea vs Fiorentina', date_updated = '2018-08-12 16:47:37', competition = 'cl', date_of_game = '2018-08-08', week_no_id = 12)
        Fixtures_table.objects.create(fixture = 'Chelsea vs Arsenal', date_updated = '2018-08-12 16:47:37', competition = 'pl', date_of_game = '2018-08-10', week_no_id = 12)
        Fixtures_table.objects.create(fixture = 'Liverpool vs Everton', date_updated = '2018-08-12 16:47:37', competition = 'pl', date_of_game = '2018-08-10', week_no_id = 13)

        return Week_table.objects.all().values('id','week_no','start_date','end_date','is_current_week'), Fixtures_table.objects.all().values('id','fixture','competition','date_of_game','week_no_id')

    def week_table_for_client(self):
        Week_table.objects.create(id = 11, week_no = 1, date_updated = '2018-08-17 20:44:40', end_date = '2018-08-11', start_date = '2018-08-05', is_current_week = 0)
        Week_table.objects.create(id = 12, week_no = 2, date_updated = '2018-08-17 20:44:46', end_date = '2018-08-18', start_date = '2018-08-12', is_current_week = 0)
        Week_table.objects.create(id = 13, week_no = 3, date_updated = '2018-08-17 20:44:50', end_date = '2018-08-26', start_date = '2018-08-19', is_current_week = 0)

        return Week_table.objects.all()

    def week_table_for_admin(self):
        Week_table.objects.create(id = 13, week_no = 8, date_updated = '2018-08-17 20:44:50', end_date = '2018-08-26', start_date = '2018-08-19', is_current_week = 0)

    '''
    4 - Get Admin to check (using radio button) the most current week save it to all statistics tables -> forms, goals, goal_assist, red_cards etc
    '''
    def stats_goals_table00(self):
        Week_table.objects.create(id = 11, week_no = 1, date_updated = '2018-08-17 20:44:40', end_date = '2018-08-11', start_date = '2018-08-05', is_current_week = 0)
        Goals_table.objects.create(points = 0, player_id = None, week_no_id_id = 11)
        return Goals_table.objects.all().values('id','points','player_id','week_no_id_id')

    def stats_goals_table01(self, id, points):
        Week_table.objects.create(id = 11, week_no = 1, date_updated = '2018-08-17 20:44:40', end_date = '2018-08-11', start_date = '2018-08-05', is_current_week = 0)
        Goals_table.objects.create(points = 20, player_id = None, week_no_id_id = 11)
        Goals_table.objects.filter(player_id = id).update(points = points)
        return Goals_table.objects.all().values('id','points','player_id','week_no_id_id')

    def set_fixtures_and_week(self, get_week):
        week_fixture = []
        for i in range(0, len(get_week[0])):
            for j in range(0, len(get_week[1])):
                if get_week[0][i].get('id') == get_week[1][j].get('week_no_id'):
                    context = {
                        'fixture': get_week[1][j].get('fixture'),
                        'date_of_game': get_week[1][j].get('date_of_game'),
                        'competition': get_week[1][j].get('competition'),
                        'week_no': get_week[0][i].get('week_no'),
                        'start_date': get_week[0][i].get('start_date'),
                        'end_date': get_week[0][i].get('end_date'),
                    }
                    week_fixture.append(context)
        return week_fixture
