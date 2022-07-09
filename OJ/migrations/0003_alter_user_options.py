from django.db import migrations
class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0002_submissions_previous_submission'),
    ]
    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-score']},
        ),
    ]