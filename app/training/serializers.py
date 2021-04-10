from rest_framework import serializers
from core.models import Urllc


class UrllcSerializer(serializers.ModelSerializer):
    """Serializer for ingredient objects"""

    class Meta:
        model = Urllc
        fields = ('id', 'name', 'TargetSNR', 'numberofUsers', 'numerology',
                'sharedBandwidth', 'sharedBandwidth', 'reservedBandwidth',
                'channelGainShadowParam1', 'channelGainFadeParam1',
                'channelGainFadeParam2', 'power', 'trafficDist',
                'trafficParam1', 'trafficParam2')
        read_only_fields = ('id',)
