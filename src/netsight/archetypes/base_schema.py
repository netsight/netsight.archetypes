from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.folder import ATFolderSchema


absolute_base_schema = ATContentTypeSchema.copy()
for field in absolute_base_schema.fields():
    if field.schemata in ['metadata', 'creators']:
        field.widget.visible = False
    if field.getName() in ['location', 'language']:
        field.widget.visible = False


absolute_base_folder_schema = ATFolderSchema.copy()
for field in absolute_base_folder_schema.fields():
    if field.schemata in ['metadata', 'creators']:
        field.widget.visible = False
    if field.getName() in ['location', 'language']:
        field.widget.visible = False
