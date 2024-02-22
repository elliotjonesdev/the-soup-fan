from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]
    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID'
            ),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='id',
            field=models.BigAutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name='ID'
            ),
        ),
    ]
