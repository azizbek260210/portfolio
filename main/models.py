from django.db import models


class AboutMe(models.Model):
    title = models.TextField()
    body = models.TextField()
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    web_site = models.URLField()
    img = models.ImageField(upload_to='about-me/')



class Education(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    major = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    detail = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=255)
    percentage = models.SmallIntegerField()


class Experience(models.Model):
    start = models.IntegerField()
    finish = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    detail = models.TextField()


class Profiles(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/')
    url = models.URLField()


class Portfolio(models.Model):
    img = models.ImageField(upload_to='portfolio/')
    url = models.URLField()


class Client(models.Model):
    img = models.ImageField(upload_to='client/')
    url = models.URLField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()