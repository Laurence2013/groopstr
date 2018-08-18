from members.models import *
from members.forms import *
'''
1 - Connect fixtures to its correct week before displaying - test_database_tables.Fixtures_and_Weeks class
'''
class Fixtures_and_Weeks:
    def week_fixture_table(self):
        Week_table.objects.create(id = 11, week_no = 1, date_updated = '2018-08-17 20:44:40', end_date = '2018-08-11', start_date = '2018-08-05', is_current_week = 0)
        Week_table.objects.create(id = 12, week_no = 2, date_updated = '2018-08-17 20:44:46', end_date = '2018-08-18', start_date = '2018-08-12', is_current_week = 0)
        Week_table.objects.create(id = 13, week_no = 3, date_updated = '2018-08-17 20:44:50', end_date = '2018-08-26', start_date = '2018-08-19', is_current_week = 0)

        Fixtures_table.objects.create(fixture = 'Chelsea vs Fiorentina', date_updated = '2018-08-12 16:47:37', competition = 'cl', date_of_game = '2018-08-08', week_no_id = 11)
        Fixtures_table.objects.create(fixture = 'Chelsea vs Arsenal', date_updated = '2018-08-12 16:47:37', competition = 'pl', date_of_game = '2018-08-10', week_no_id = 11)
        Fixtures_table.objects.create(fixture = 'Liverpool vs Everton', date_updated = '2018-08-12 16:47:37', competition = 'pl', date_of_game = '2018-08-10', week_no_id = 12)

        return Week_table.objects.all().values('id','week_no','start_date','end_date','is_current_week'), Fixtures_table.objects.all().values('id','fixture','competition','date_of_game','week_no_id')

    def set_fixtures_and_week(self, get_week):
        for i in range(0, len(get_week[0])):
            for j in range(0, len(get_week[1])):
                if get_week[0][i].get('id') == get_week[1][j].get('week_no_id'):
                    print(get_week[1][j].get('fixture'))
