# Generated by Django 2.2.3 on 2019-07-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
    ]
