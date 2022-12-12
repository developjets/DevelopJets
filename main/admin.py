from django.contrib import admin

# Register your models here.

from .models import Team, Contact, Client, Project

class teamAdmin(admin.ModelAdmin):
    team_display = ["name", "designation", "photo"]

class contactAdmin(admin.ModelAdmin):
    contact_display = ["name", "email", "subject", "message"]

class clientAdmin(admin.ModelAdmin):
    client_display = ["name", "logo", "portfolio", "phone", "email"]

class projectAdmin(admin.ModelAdmin):
    project_display = ["title", "detail", "image1", "image2", "image3", "image4", "url", "date", "clientName", "category"]


admin.site.register(Team, teamAdmin)
admin.site.register(Contact, contactAdmin)
admin.site.register(Client, clientAdmin)
admin.site.register(Project, projectAdmin)