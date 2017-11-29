from rest_framework import serializers


class CustomSerializer(serializers.ModelSerializer):
    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields


def get_serializer(model):
    meta = type('Meta', (object,), {
        'model': model,
        'fields': '__all__',
    })

    dynamic_serializer = type(
        'DynamicSerializer', (serializers.ModelSerializer,), {
            'Meta': meta
        }
    )
    return dynamic_serializer
