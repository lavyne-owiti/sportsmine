
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Coach(models.Model):
    firstcoach_name=models.CharField(max_length=15)
    lastcoach_name=models.CharField(max_length=15)
    coach_email=models.EmailField()
    coach_phonenumber=models.CharField(max_length=20)
    CGENDER_CHOICES=(
        ('M','M'),
        ('F','F')
    )
    coach_gender=models.CharField(max_length=1,choices=CGENDER_CHOICES)
    coach_address=models.TextField()
    coach_nationality=models.CharField(max_length=20)
    coach_pic=models.ImageField(upload_to='images/')
    coach_team=models.CharField(max_length=15)
    COACHTITLE_CHOICES=(
        ('Assistant coach','Assistant coach'),
        ('Head coach','Head coach')
    )
    coach_title=models.CharField(max_length=20,choices=COACHTITLE_CHOICES )

    def __str__(self):
        return self.firstcoach_name

class Team(models.Model):
    team_name=models.CharField(max_length=20)
    no_players=models.IntegerField()
    team_coach=models.ForeignKey(Coach,on_delete=models.CASCADE)
    list_player=ArrayField(
        models.CharField(max_length= 50,blank=True),size=8
    )

    def __str__(self):
        return self.team_name

class Player(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email=models.EmailField()
    player_pic=models.ImageField(upload_to='uploads/')
    Phone_number=models.CharField(max_length=20)
    GENDER_CHOICES=(
        ('M','M'),
        ('F','F')
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    age=models.PositiveSmallIntegerField()
    address=models.TextField()
    nationality=models.CharField(max_length=20)
    players_team=models.ForeignKey(Team,on_delete=models.CASCADE,null=True)
    employed=models.BooleanField()

    def __str__(self):
        return self.first_name



class Leader(models.Model):
    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    leader_email=models.EmailField()
    leader_phonenumber=models.CharField(max_length=20)
    LGENDER_CHOICES=(
        ('M','M'),
        ('F','F')
    ) 
    leader_gender=models.CharField(max_length=1,choices=LGENDER_CHOICES)
    leader_address=models.TextField()
    leader_nationality=models.CharField(max_length=20)
    leader_pic=models.ImageField(upload_to='uploads/')
    LEADERTITLE_CHOICES=(
        ('Federation leader','Federation leader'),
        ('Scout ','Scout')
    )
    leader_title=models.CharField(max_length=30,choices=LEADERTITLE_CHOICES)

    def __str__(self):
        return self.firstname

class New_report(models.Model):
    repoter_name=models.ForeignKey(Leader,on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True)
    REPORTERTITLE_CHOICES=(
        ('Federation leader','Federation leader'),
        ('Scout ','Scout')
    )
    title=models.CharField(max_length=20,choices=REPORTERTITLE_CHOICES)
    message=models.TextField()
    news_image=models.ImageField(upload_to='uploads/')

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.message[:50]}..."


class Fixture(models.Model):
    fixtures=models.FileField(upload_to='uploads/')
    # fiximage=models.ImageField(upload_to='images/')
    date=models.DateField(auto_now_add=True)
    uploaded_by=models.ForeignKey(Leader,on_delete=models.CASCADE)

class Referee(models.Model):
    reffirst_name=models.CharField(max_length=15)
    reflast_name=models.CharField(max_length=15)
    refemail=models.EmailField()
    ref_pic=models.ImageField(upload_to='uploads/')
    refphone_number=models.CharField(max_length=20)
    RGENDER_CHOICES=(
        ('M','M'),
        ('F','F')
    )
    refgender=models.CharField(max_length=1,choices=RGENDER_CHOICES)
    refddress=models.TextField()
    refationality=models.CharField(max_length=20)
    REFTITLE_CHOICES=(
        ('Assistant coach','Assistant coach'),
        ('Head coach','Head coach')
    )
    ref_title=models.CharField(max_length=15,choices=REFTITLE_CHOICES)

    def __str__(self):
        return self.reffirst_name

class Match(models.Model):
    matches_played=models.TextField()
    match_report=models.ForeignKey(New_report,on_delete=models.CASCADE)
    match_datetime=models.DateTimeField(auto_now_add=True)
    match_location=models.CharField(max_length=20)
    match_pic=models.ImageField(upload_to='uploads/')
    match_video=models.FileField(upload_to='uploads/')
    match_ref=models.ForeignKey(Referee,on_delete=models.CASCADE)

    def __str__(self):
        return self.matches_played

class Award(models.Model):
    award_name=models.CharField(max_length=30)
    player_awarded=models.ForeignKey(Player,on_delete=models.CASCADE)
    event_awarded=models.CharField(max_length=30)
    item_award=models.CharField(max_length=30)
    playerward_pic=models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.award_name


class Medic(models.Model):
    medic_name=models.CharField(max_length=20)
    medic_pic=models.ImageField(upload_to='uploads/')
    medic_team=models.ForeignKey(Team,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.medic_name



