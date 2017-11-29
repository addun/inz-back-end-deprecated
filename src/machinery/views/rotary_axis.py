from rest_framework import viewsets

from machinery.models import ContinuousRotary, LimitedSwing, Indexing
from machinery.serializers.rotary_axis import ContinuousRotarySerializer, LimitedSwingSerializer, IndexingSerializer


class ContinuousRotaryViewSet(viewsets.ModelViewSet):
    queryset = ContinuousRotary.objects.all()
    serializer_class = ContinuousRotarySerializer


class IndexingViewSet(viewsets.ModelViewSet):
    queryset = Indexing.objects.all()
    serializer_class = IndexingSerializer


class LimitedSwingViewSet(viewsets.ModelViewSet):
    queryset = LimitedSwing.objects.all()
    serializer_class = LimitedSwingSerializer
