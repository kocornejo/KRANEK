# Generated by Django 4.1 on 2022-09-07 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_quiz_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
    ]
