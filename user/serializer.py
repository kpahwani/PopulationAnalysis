from rest_framework import serializers
from .models import User, Race, Relationship


class UserSerializer(serializers.ModelSerializer):
    wrk_cls_val = serializers.ReadOnlyField()
    edu_val = serializers.ReadOnlyField()
    mar_status_val = serializers.ReadOnlyField()
    occupation_val = serializers.ReadOnlyField()
    relation_val = serializers.ReadOnlyField()
    race_val = serializers.ReadOnlyField()
    gender_val = serializers.ReadOnlyField()
    country_val = serializers.ReadOnlyField()
    class_grp_val = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = (
            'age',
            'wrk_cls_val',
            'fnl_wgt',
            'edu_val',
            'edu_num',
            'mar_status_val',
            'occupation_val',
            'relation_val',
            'race_val',
            'gender_val',
            'cap_gain',
            'cap_loss',
            'hrs_per_week',
            'country_val',
            'class_grp_val',
        )


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'
