from django.contrib import admin
from players.models import *

admin.site.register(Player_table)
admin.site.register(Player_Team_table)
admin.site.register(Clean_Sheets_table)
admin.site.register(Goals_Assist_table)
admin.site.register(Goals_table)
admin.site.register(Man_of_Match_table)
admin.site.register(Own_Goals_table)
admin.site.register(Yellow_Card_table)
admin.site.register(Red_Card_table)
admin.site.register(Form_table)