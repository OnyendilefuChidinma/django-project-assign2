# Generated by Django 5.0 on 2024-10-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0013_alter_student_profile_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student_profile",
            name="profile_image",
            field=models.ImageField(null=True, upload_to="student_profile"),
        ),
    ]