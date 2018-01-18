from rest_framework import serializers, viewsets, routers

from lamp_control.models import Lamp


class LampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lamp
        fields = '__all__'


class LampViewSet(viewsets.ModelViewSet):
    serializer_class =  LampSerializer
    queryset = Lamp.objects.all()


router = routers.DefaultRouter()
router.register(r'lamps', LampViewSet)
