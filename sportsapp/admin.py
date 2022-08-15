from django.contrib import admin

from sportsapp.models import Award, Coach, Fixture, Leader, Match, New_report,Player, Referee, Team

# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(New_report)
admin.site.register(Coach)
admin.site.register(Leader)
admin.site.register(Award)
admin.site.register(Referee)
admin.site.register(Match)