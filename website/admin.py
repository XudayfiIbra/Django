from django.contrib import admin
from . models import Project, Tag, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url',)
    inlines = [ProjectImageInline]
    search_fields = ('title', 'description')
    list_filter = ('tags',)
    



class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ProjectImage)
