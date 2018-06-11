from rest_framework.decorators import api_view
from .models import User, Relationship, Race
from user.serializer import UserSerializer, RelationshipSerializer, RaceSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.get_all_user()
    serializer_class = UserSerializer

    def get(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def gender_count(request):
    result = User.get_gender_count()
    return Response(result)


@api_view(['GET'])
def relationship_count(request):
    result = User.get_relationship_count()
    return Response(result)


@api_view(['GET'])
def search(request, gender, race, relation):
    queryset = User.objects.filter(gender=gender, race=race, relation=relation)
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_selector_list(request):
    result = {}
    result['raceList'] = RaceSerializer(Race.objects.all(), many=True).data
    result['relationList '] = RelationshipSerializer(Relationship.objects.all(), many=True).data
    return Response(result)
