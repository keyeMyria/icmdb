# Generated by Django 2.0.5 on 2018-05-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20180517_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetinfo',
            name='is_active',
            field=models.CharField(choices=[('在线', '在线'), ('下线', '下线'), ('未知', '未知'), ('故障', '故障'), ('备用', '备用')], default='在线', max_length=64, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='assetloginuser',
            name='private_key',
            field=models.FileField(blank=True, null=True, upload_to='upload/privatekey/%Y%m%d68304', verbose_name='私钥'),
        ),
    ]
