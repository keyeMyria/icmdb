


import os,django,time,datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chain.settings")
django.setup()

from asset.models import  AssetLoginUser, AssetProject
from asset.models import AssetInfo as Asset

# fields = [
#             field for field in Asset._meta.fields
#             if field.name not in [
#                 'date_created'
#             ]

assets_user = []
for i in AssetLoginUser.objects.all():
    assets_user.append(i)

print(assets_user)

for row in assets_user:
    print(row.username,row.project,row.user_name.count)


