from django.db import models

# Create your models here.

# We need a name
# A list of technologies used
# A URL to video of demo
# A Github URL
# URL to Devlog video playlist (optional)
# A link to a Design Document
# A list of tags for future searches
class BaseArticle(models.Model):
    name = models.CharField(max_length=255, default="")
    related_video = models.CharField(max_length=255)
    related_image = models.CharField(max_length=255)
    

# Base for article entries 
# Title
# Related Video URL
# Related Image link or URL
# DevLog Body
# Date of Devlog
# Date Created
# Date Modified
class BaseEntry(models.Model):
    title = models.CharField(max_length=255)
    related_video = models.CharField(max_length=255)
    related_image = models.CharField(max_length=255)
    main_body = models.TextField()
    date = models.DateTimeField()
    modified = models.DateTimeField()
    created = models.DateTimeField()


# Tags
# A collection of desctiptors
# tag name
# tag description

# Technologies
# A collection of relevant technologies
# tech name
# tech description

# TechnologiesToArticles
# Many to Many
# tech id
# article id

# TagsToArticles
# Many to Many
# tag id
# article id


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

# ProjectToDevLog

# DevLog:
# We need a name
# A list of technologies used
# A URL to related Video
# A brief description
# Linked Project
# A Github URL
# URL to Devlog video playlist (optional)
# A link to a Design Document
# A list of tags for future searches


# Devlog to Entries
# DevLog ID
# DevLogEntry ID
# one to many

# DevLogEntry
# Title
# Related Video URL
# Related Image link or URL
# DevLog Body
# Date of Devlog
# Date Created
# Date Modified

# TutorialSeries
# We need a name
# A list of technologies used
# A URL to video of tutorial
# A link to related dev logs
# A brief description
# Tutorial Body
# A Github URL
# URL to Tutorial video playlist (optional)
# A link to Additional resources
# A list of tags for future searches

# TutorialEntry
# Title
# Related Video URL
# Related Image link or URL
# Tutorial Body
# Date of Tutorial
# Date Created
# Date Modified

# TutorialToEntries
