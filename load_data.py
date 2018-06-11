import sys, os
import django
# Full path and name to your csv file
csv_filepathname="data.csv"
# Full path to the directory immediately above your django project directory
djangoproject_home="/home/kaushal/PycharmProjects/PopulationAnalysis/"


sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'PopulationAnalysis.settings'
django.setup()


from user.models import *

def read_data_csv(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield list(map(str.strip, line.split(',')))


wrk_class_list = WorkClass.objects.all()
edu_list = Education.objects.all()
marital_list = MaritalStatus.objects.all()
occupation_list = Occupation.objects.all()
rel_list = Relationship.objects.all()
race_list = Race.objects.all()
country_list = Country.objects.all()


def get_object(query_list, value):
    for obj in query_list:
        if obj.value == value:
            return obj
    return None


def get_data_choices(choices, value):
    for data in choices:
        if data[1] == value:
            return data[0]
    return None


# Use either of the parser
# 1.Used to load models with known value
for data in read_data_csv(csv_filepathname):
    for item in data:
        WorkClass.objects.create(value=item)


# 2.Used to loas user model
for data in read_data_csv(csv_filepathname):
    wrk_class = get_object(wrk_class_list, data[1])
    edu = get_object(edu_list, data[3])
    marital = get_object(marital_list, data[5])
    occupation = get_object(occupation_list, data[6])
    rel = get_object(rel_list, data[7])
    race = get_object(race_list, data[8])
    gender = get_data_choices(User.GENDER_CHOICES, data[9])
    country = get_object(country_list, data[13])
    cls_grp = get_data_choices(User.CLASS_GROUP_CHOICES, data[14])

    User.objects.create(
        age=data[0],
        wrk_cls=wrk_class,
        fnl_wgt=data[2],
        edu=edu,
        edu_num=data[4],
        mar_status=marital,
        occupation=occupation,
        relation=rel,
        race=race,
        gender=gender,
        cap_gain=data[10],
        cap_loss=data[11],
        hrs_per_week=data[12],
        country=country,
        class_grp=cls_grp
    )
