from django.db import models
from django_jalali.db import models as jmodels
from experts.models import Expert


class ProgramMonth(models.Model):
    SITE_CHITGHAR = 1
    SITE_ZARAFSHAN = 2
    SITE_SEMNAN = 3
    SITES = ((SITE_SEMNAN, 'Site Chitghar'), (SITE_ZARAFSHAN, 'Site Zarafshan'), (SITE_SEMNAN, 'Site Semnan'))
    name = models.CharField(max_length=30)
    start_date = jmodels.jDateField()
    finish_date = jmodels.jDateField()
    site = models.PositiveSmallIntegerField(choices=SITES, default=1)
    number_of_days = models.PositiveSmallIntegerField(max_length=31)
    number_of_holidays = models.PositiveSmallIntegerField()
    duty_time = models.PositiveIntegerField()


class Shift(models.Model):
    TYPE_DAY = 1
    TYPE_NIGHT = 2
    TYPE = ((TYPE_DAY, 'Day shift'), (TYPE_NIGHT, 'Night shift'))
    type = models.PositiveSmallIntegerField(choices=TYPE)
    date = jmodels.jDateField()
    program_mont = models.ForeignKey(ProgramMonth, models.CASCADE)
    is_holiday = models.BooleanField(default=False)
    is_working_day = models.BooleanField(default=False)


class ExpertShift(models.Model):
    STATUS_RESERVE = 1
    STATUS_ENABLE = 2
    STATUS_PASS = 3
    STATUS_CHANGE = 4
    STATUS = ((STATUS_RESERVE, 'Reserve'), (STATUS_ENABLE, 'Enable'), (STATUS_PASS, 'Pass'), (S))
    experts = models.ForeignKey(Expert, models.PROTECT)
    shift = models.ForeignKey(Shift, models.CASCADE)
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS)
    description = models.CharField(max_length=100, blank=True, null=None)
