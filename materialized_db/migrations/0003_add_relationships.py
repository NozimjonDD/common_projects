import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materialized_db', '0002_alter_bookings_options_alter_facility_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='facility',
            field=models.ForeignKey(
                db_column='facid',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='materialized_db.facility',
            ),
        ),
        migrations.AddField(
            model_name='bookings',
            name='member',
            field=models.ForeignKey(
                db_column='memid',
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='materialized_db.members',
            ),
        ),
        migrations.AddField(
            model_name='members',
            name='recommended_by',
            field=models.ForeignKey(
                db_column='recommendedby',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='materialized_db.members',
            ),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='facility',
            field=models.ForeignKey(
                db_column='facid',
                on_delete=django.db.models.deletion.CASCADE,
                to='materialized_db.facility',
            ),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='member',
            field=models.ForeignKey(
                db_column='memid',
                on_delete=django.db.models.deletion.CASCADE,
                to='materialized_db.members',
            ),
        ),
    ]
