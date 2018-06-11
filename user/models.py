from django.db import models
from django.db.models import Count


# Create your models here.
class WorkClass(models.Model):
    value = models.CharField(max_length=20,unique=True)


class Education(models.Model):
    value = models.CharField(max_length=20, unique=True)


class MaritalStatus(models.Model):
    value = models.CharField(max_length=20, unique=True)


class Occupation(models.Model):
    value = models.CharField(max_length=20, unique=True)


class Relationship(models.Model):
    value = models.CharField(max_length=20, unique=True)


class Race(models.Model):
    value = models.CharField(max_length=20, unique=True)


class Country(models.Model):
    value = models.CharField(max_length=20, unique=True)


class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    CLASS_GROUP_CHOICES = (
        ('U', '>50K'),
        ('L', '<=50K'),
    )
    age = models.IntegerField(null=True)
    wrk_cls = models.ForeignKey(WorkClass, on_delete=models.CASCADE, null=True)
    fnl_wgt = models.IntegerField(null=True)
    edu = models.ForeignKey(Education, on_delete=models.CASCADE, null=True)
    edu_num = models.IntegerField(null=True)
    mar_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE, null=True)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE, null=True)
    relation = models.ForeignKey(Relationship, on_delete=models.CASCADE, null=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    cap_gain = models.IntegerField(null=True)
    cap_loss = models.IntegerField(null=True)
    hrs_per_week = models.IntegerField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    class_grp = models.CharField(max_length=10, choices=CLASS_GROUP_CHOICES, null=True)

    @property
    def wrk_cls_val(self):
        if self.wrk_cls.value:
            return self.wrk_cls.value
        else:
            return ''

    @property
    def edu_val(self):
        return self.edu.value

    @property
    def mar_status_val(self):
        return self.mar_status.value

    @property
    def occupation_val(self):
        return self.occupation.value

    @property
    def relation_val(self):
        if self.relation.value:
            return self.relation.value
        else:
            return ''

    @property
    def race_val(self):
        if self.race.value:
            return self.race.value
        else:
            return ''

    @property
    def gender_val(self):
        if self.gender == 'M':
            return 'Male'
        else:
            return 'Female'

    @property
    def country_val(self):
        if self.country.value:
            return self.country.value
        else:
            return ''

    @property
    def class_grp_val(self):
        if self.class_grp == 'L':
            return '<50K'
        else:
            return '>=50K'

    @staticmethod
    def get_all_user():
        return User.objects.all()

    @staticmethod
    def get_gender_count():
        return User.objects.values('gender').annotate(count=Count('gender'))

    @staticmethod
    def get_relationship_count():
        return User.objects.values('relation__value').annotate(count=Count('relation'))

