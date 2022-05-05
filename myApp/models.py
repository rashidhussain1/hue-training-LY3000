from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(default="")
    class Meta:
        db_table = "user"

class Project(models.Model):
    projectId = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=100)
    projectDescription = models.CharField(max_length=300)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = "project"

class Issue(models.Model):
    issueId = models.AutoField(primary_key=True)
    issueName = models.CharField(max_length=100)
    issueType = models.CharField(max_length=100)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigneeId = models.ForeignKey(User, on_delete=models.CASCADE)
    reporterId = models.IntegerField()
    issueStatus = models.IntegerField()
    issueDescription = models.CharField(max_length=300)
    class Meta:
        db_table = "issue" 
