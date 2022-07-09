from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0003_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submissions',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='submissions',
            name='language',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('language', models.CharField(max_length=10)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OJ.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]