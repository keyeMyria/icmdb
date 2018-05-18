from celery import Celery, platforms
from chain import settings
from multiprocessing import current_process
from asset.models import AssetInfo
from tasks.ansible_2420.runner import AdHocRunner, PlayBookRunner
from tasks.ansible_2420.inventory import BaseInventory
from tasks.models import Variable, Tools
from index.password_crypt import decrypt_p
import logging
import os
import random


platforms.C_FORCE_ROOT = True
app = Celery('chain')
app.config_from_object('django.conf:settings', )
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

logger = logging.getLogger('tasks_celery')

ids = 3

asset = [{'hostname': 'fhsh', 'ip': '172.16.23.33', 'port': 22, 'username': 'root', 'password': 'iflytek!33', 'private_key': ''}]

@app.task()
def ansbile_asset_hardware(ids, assets):
    print('hehh')
    print(AssetInfo.objects.get(id=ids))



ansbile_asset_hardware(ids,asset)

