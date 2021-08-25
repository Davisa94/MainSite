from django.db import models

# Create your models here.

# We need a name
# A list of technologies used
# A URL to video of demo
# A Github URL
# URL to Devlog video playlist (optional)
# A link to a Design Document
# A list of tags for future searches
class DetailedBase(models.Model):
    name = models.CharField(max_length=255, default="")

# Projects:
# We need a name
# A list of technologies used
# A URL to video of demo
# A link to related dev logs
# A brief description
# A Project Article about any hardships encountered
# A Github URL
# URL to Devlog video playlist (optional)
# A link to a Design Document
# A list of tags for future searches

# DevLogContainer:
# We need a name
# A list of technologies used
# A URL to video of demo
# A link to related dev logs
# A brief description
# A Project Article about any hardships encountered
# A Github URL
# URL to Devlog video playlist (optional)
# A link to a Design Document
# A list of tags for future searches

# DevLogEntry
# Title
# Related Video URL
# Related Image link or URL
# DevLog Body
# Date of Devlog
# Date Created
# Date Modified