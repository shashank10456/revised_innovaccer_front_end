# Generated by Django 2.0 on 2018-02-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='about',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='codeforces',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='hackerrank',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='username',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='cost',
            field=models.TextField(default='0000000', editable=False, max_length=30),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='description',
            field=models.TextField(default='0000000', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='quantity',
            field=models.TextField(default='0000000', editable=False, max_length=10),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='total',
            field=models.TextField(default='0000000', editable=False, max_length=13),
        ),
    ]
