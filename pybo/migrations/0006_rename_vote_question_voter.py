# Generated by Django 4.0.3 on 2022-05-10 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_answer_voter_question_vote_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='vote',
            new_name='voter',
        ),
    ]