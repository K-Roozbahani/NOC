from django.db import models
from django.contrib.auth.models import User
# time
from django_jalali.db import models as jmodels
import jdatetime
import datetime
# translate
from django.utils.translation import gettext_lazy as _

# choose site
CHITGAR_SITE = 1
ZARAFSHAN_SITE = 2
SEMNAN_SITE = 3
SITES = ((CHITGAR_SITE, 'چیتگر'), (ZARAFSHAN_SITE, 'زرفشان'), (SEMNAN_SITE, 'سمنان'))


class Expert(models.Model):
    user = models.OneToOneField('User', models.CASCADE, verbose_name=_('user'))
    employ_number = models.IntegerField(_("employ number"), blank=False, unique=True, null=False)
    site = models.SmallIntegerField(_('site'), choices=SITES, default=1)
    shite = models.ManyToManyField(to='Shift', verbose_name=_('shift'), blank=True, null=True)


class Shift(models.Model):
    DAY_SHIFT = 1
    NIGHT_SHIFT = 2
    SHIFT_NAME = ((DAY_SHIFT, 'شیفت روز'), (NIGHT_SHIFT, ('شیفت شب')))
    name = models.SmallIntegerField(_('name'), choices=SHIFT_NAME, default=1)
    date_shift = jmodels.jDateField(_('date shift'), default=jdatetime.date(1401, 1, 1))
    site = models.IntegerField(_('site'), choices=SITES, default=1)
    is_holiday = models.BooleanField(_('is holiday'), default=False)
    shift_program = models.ForeignKey('Shift_Month', models.CASCADE, verbose_name=_('shift program'))


class Shift_Month(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False)
    start_date = jmodels.jDateField(_('start date'), default=jdatetime.date(1401, 1, 1))
    finish_date = jmodels.jDateField(_('finish date'), default=jdatetime.date(1401, 2, 1))
    site = models.SmallIntegerField(_('site'), choices=SITES)
    number_days = models.IntegerField(_('number of days'), blank=True, null=True)
    number_holidays = models.IntegerField(_('number of holidays'), blank=True, null=True)
    duty = models.IntegerField(_('duty'), blank=True, null=True)

    def __str__(self):
        return self.name

    def _create_shift_(self, list_holidays):
        self.determine_number_of_days()

    def determine_number_of_days(self):
        if not self.ob:
            date = self.finish_date.parse_date(datetime.date) - jdatetime.datetime(30)
            number_days = date.day + 10
            self.objects.filter(pk=self.pk).update(number_days=number_days)
