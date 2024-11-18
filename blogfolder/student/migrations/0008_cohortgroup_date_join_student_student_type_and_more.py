# Generated by Django 5.0 on 2024-10-21 05:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0007_alter_student_profile_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="cohortgroup",
            name="date_join",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="student_type",
            field=models.CharField(
                choices=[
                    ("leader", "cohort leader"),
                    ("deputy", "vice leader"),
                    ("secretary", "secretary"),
                    ("President", "President"),
                    ("member", "member"),
                ],
                default="member",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="first_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="last_name",
            field=models.CharField(max_length=200, verbose_name="last name"),
        ),
        migrations.AlterField(
            model_name="student",
            name="username",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]