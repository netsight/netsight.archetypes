from Products.Archetypes.BaseContent import BaseSchema


for field in BaseSchema.fields():
    if field.schemata == 'metadata':
        field.widget.visible = False


absolute_base_schema = BaseSchema.copy()
