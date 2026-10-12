from django.db import models


class Facility(models.Model):
    id = models.IntegerField(db_column='facid', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    member_cost = models.FloatField(db_column='membercost')
    guest_cost = models.FloatField(db_column='guestcost')
    initial_outlay = models.PositiveIntegerField(db_column='initialoutlay')
    monthly_maintenance = models.PositiveIntegerField(db_column='monthlymaintenance')

    class Meta:
        managed = True
        db_table = 'facilities'


class Members(models.Model):
    id = models.IntegerField(db_column='memid', primary_key=True)
    first_name = models.CharField(db_column='firstname', max_length=200)
    last_name = models.CharField(db_column='surname', max_length=200)
    address = models.CharField(db_column='address', max_length=300)
    zipcode = models.IntegerField(db_column='zipcode')
    telephone = models.CharField(db_column='telephone', max_length=20)
    recommended_by = models.ForeignKey('self', db_column='recommendedby', null=True, on_delete=models.SET_NULL)
    join_date = models.DateTimeField(db_column='joindate')

    class Meta:
        managed = True
        db_table = 'members'


class Bookings(models.Model):
    id = models.IntegerField(db_column='bookid', primary_key=True)
    facility = models.ForeignKey(Facility, db_column='facid', blank=False, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, db_column='memid', blank=False, null=False, on_delete=models.CASCADE)
    start_time = models.DateTimeField(db_column='starttime', null=False)
    slots = models.IntegerField(db_column='slots')

    class Meta:
        managed = True
        db_table = 'bookings'
