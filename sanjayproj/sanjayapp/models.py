from django.db import models

# Create your models here.
class Host(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    environment = models.CharField(max_length=20)
    serialnumber = models.CharField(max_length=20)
    OS = models.CharField(max_length=20)
    Architecture = models.CharField(max_length=50)
    


    def __str__(self):
      #return 'Policy: ' + self.name
      return 'Host Name: ' + self.name


class Apps(models.Model):
    name = models.ForeignKey(Host, on_delete=models.CASCADE)
    applicationname = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    Suport_Group = models.CharField(max_length=100)

    def __str__(self):
      #return 'Policy: ' + self.name
      return 'Application Name: ' + self.applicationname


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_num = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    post_code = models.CharField(max_length=50)
    county = models.CharField(max_length=100)


    def __str__(self):
      return 'Musician Name: ' + self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    number_of_song = models.IntegerField()
    song_name = models.CharField(max_length=100) 

