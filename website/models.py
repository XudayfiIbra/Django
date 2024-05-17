from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    url = models.URLField(max_length=400, blank=True) 
    
    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to='website/Project_images/')
    
    
    def __str__(self):
        return self.project.title
    