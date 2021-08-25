from django.db import models

# Create your models here.

# We need a name
# A list of technologies used
# A link to video of demo
# A link to related dev logs
# A brief description
# A Project Article about any hardships encountered
# A Github link
# Link to Devlog video playlist (optional)
# A link to a Design Document
class Project(models.Model):
    name = models.CharField(max_length=255, default="")


