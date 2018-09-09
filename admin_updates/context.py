class Context:
    def get_context(self, kwargs_context, context_fix, context_stats):
        context = {
            'get_week': True if not kwargs_context else False,
            'get_fixtures': True if context_fix == 'fixtures' else False,
            'get_goals_table': True if context_stats == 'statistics' else False,
            'get_goals_assist_table': True if context_stats == 'statistics' else False,
            # 'get_man_of_the_match_table': True if get_latest_week else False,
            # 'get_own_goals': True if get_latest_week else False,
            # 'get_yellow_cards': True if get_latest_week else False,
            # 'get_red_cards': True if get_latest_week else False,
            # 'get_clean_sheets': True if get_latest_week else False,
            # 'get_form': True if get_latest_week else False,
            # 'get_goalkeepers': True,
            # 'get_defenders': True,
            # 'get_midfielders': True,
            # 'get_forwards': True,
            # 'get_players_points': True,
            # 'get_user_total_points': True,
        }
        return context

    def get_context_false(self, kwargs_context, context_fix, true_or_false):
        context = {
            'get_week': True if not kwargs_context else False,
            'get_fixtures': True if context_fix == 'fixtures' else False,
            'get_goals_table': true_or_false,
            'get_goals_assist_table': true_or_false,
            # 'get_man_of_the_match_table': True if get_latest_week else False,
            # 'get_own_goals': True if get_latest_week else False,
            # 'get_yellow_cards': True if get_latest_week else False,
            # 'get_red_cards': True if get_latest_week else False,
            # 'get_clean_sheets': True if get_latest_week else False,
            # 'get_form': True if get_latest_week else False,
            # 'get_goalkeepers': True,
            # 'get_defenders': True,
            # 'get_midfielders': True,
            # 'get_forwards': True,
            # 'get_players_points': True,
            # 'get_user_total_points': True,
        }
