from rest_framework import routers, serializers, viewsets
from . import models


class ThoughtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Thought
        fields = ('recorded_at', 'condition', 'notes')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
