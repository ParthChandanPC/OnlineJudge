from django.db import migrations, models
class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissions',
            name='previous_submission',
            field=models.TextField(blank=True, null=True),
        ),
    ]