from machinery.models import MachineToolElement
from machinery.serializers.element_capability import TailstockSerializer, ColletSerializer, CoolantSerializer, \
    BarFeederSerializer
from machinery.serializers.machine_tool_axis import LinearAxisSerializer, MachineToolAxisSerializer
from machinery.serializers.rotary_axis import ContinuousRotarySerializer, IndexingSerializer, LimitedSwingSerializer
from machinery.serializers.sensor import ToolSettingSerializer, PartProbeSerializer, ToolBreakageSerializer
from machinery.serializers.spindle import SpindleSerializer, ToolSpindleSerializer, TaperedSpindleSerializer, \
    StraightSpindleSerializer, ThreadedSpindleSerializer, WorkSpindleSerializer
from machinery.serializers.tool_handling_unit import ToolChangerSerializer, ToolMagazineSerializer, TurretSerializer
from machinery.serializers.utils import CustomSerializer
from machinery.serializers.work_table import CircularWorkTableSerializer, RectangularWorkTableSerializer, \
    PalletSerializer


class MachineToolElementSerializer(CustomSerializer):
    tailstocks = TailstockSerializer(many=True, read_only=True)
    coolants = CoolantSerializer(many=True, read_only=True)
    collets = ColletSerializer(many=True, read_only=True)
    barfeeders = BarFeederSerializer(many=True, read_only=True)
    continuousrotary = ContinuousRotarySerializer(many=True, read_only=True)
    indexing = IndexingSerializer(many=True, read_only=True)
    limitedswing = LimitedSwingSerializer(many=True, read_only=True)
    linearaxis = LinearAxisSerializer(many=True, read_only=True)
    machinetoolaxis = MachineToolAxisSerializer(many=True, read_only=True)
    circularworktable = CircularWorkTableSerializer(many=True, read_only=True)
    rectangularworktable = RectangularWorkTableSerializer(many=True, read_only=True)
    pallet = PalletSerializer(many=True, read_only=True)
    spindle = SpindleSerializer(many=True, read_only=True)
    toolspindle = ToolSpindleSerializer(many=True, read_only=True)
    taperedspindle = TaperedSpindleSerializer(many=True, read_only=True)
    straightspindle = StraightSpindleSerializer(many=True, read_only=True)
    threadedspindle = ThreadedSpindleSerializer(many=True, read_only=True)
    workspindle = WorkSpindleSerializer(many=True, read_only=True)
    toolchanger = ToolChangerSerializer(many=True, read_only=True)
    toolmagazine = ToolMagazineSerializer(many=True, read_only=True)
    turret = TurretSerializer(many=True, read_only=True)
    toolsetting = ToolSettingSerializer(many=True, read_only=True)
    partprobe = PartProbeSerializer(many=True, read_only=True)
    toolbreakage = ToolBreakageSerializer(many=True, read_only=True)

    class Meta:
        model = MachineToolElement
        fields = '__all__'
        extra_fields = [
            'collets',
            'tailstocks',
            'coolants',
            'barfeeders',
            'continuousrotary',
            'indexing',
            'limitedswing',
            'linearaxis',
            'machinetoolaxis',
            'circularworktable',
            'rectangularworktable',
            'pallet',
            'spindle',
            'toolspindle',
            'taperedspindle',
            'straightspindle',
            'threadedspindle',
            'workspindle',
            'toolchanger',
            'toolmagazine',
            'turret',
            'toolsetting',
            'partprobe',
            'toolbreakage',
        ]
