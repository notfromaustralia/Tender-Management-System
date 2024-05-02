# Generated by Django 5.0.4 on 2024-05-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='company_registration_no',
            field=models.CharField(default='nil', max_length=100),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='kyc_document',
            field=models.FileField(blank=True, upload_to='kyc_docs/'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('approved', 'Approved')], default='pending', max_length=20),
        ),
    ]