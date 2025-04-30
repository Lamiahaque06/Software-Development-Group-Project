from django.contrib import admin
from .models import Team, Question, Response, Department
from .models import Profile

admin.site.register(Team)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Department)
admin.site.register(Profile)