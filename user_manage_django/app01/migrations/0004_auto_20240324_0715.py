# Generated by Django 3.2 on 2024-03-23 23:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_alter_userinfo_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrettyNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号码')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[(1, '初级'), (2, '中级'), (3, '高级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[(0, '未占用'), (1, '已占用')], default=0, verbose_name='状态')),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.department', verbose_name='部门'),
        ),
    ]