from datetime import date

from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

ANIMAL = (
    ('puppy', 'Puppy'),
    ('dog', 'Dog'),
    ('senior_dog', 'Senior Dog'),
    ('kittens', 'Kittens'),
    ('cat', 'Cat'),
    ('senior_cat', 'Senior Cat'),
)


class Angel(models.Model):
    about_home = models.TextField('מידע על הבית', blank=True, default='')
    full_name = models.CharField('שם מלא', max_length=200)
    email = models.EmailField('כתובת דואר אלקטרוני')
    phone = PhoneNumberField('טלפון')
    call_at_night = models.BooleanField('אתם יכולים להתקשר אלי אחרי 22:00 אם יש צורך באומנה', default=False)
    address = models.CharField('כתובת בבית', max_length=200)
    dob = models.DateField('תאריך לידה')  # date of birth
    comment = models.TextField('מידע נוסף', blank=True, default='')
    admin_comment = models.TextField('הערות מנהלים', blank=True, default='')
    created = models.DateTimeField('תאריך הרשמה', auto_now_add=True)

    foster_at_home = models.BooleanField(
        'מגורים בבית',
        blank=True,
        default=False,
    )
    home_with_garden = models.BooleanField(
        'יש גינה',
        blank=True,
        default=False,
    )
    have_car = models.BooleanField(
        'יש רכב',
        blank=True,
        default=False,
    )
    can_pay_food = models.BooleanField(
        'יכולים לשלם על אוכל',
        blank=True,
        default=False,
    )
    can_pay_medicine = models.BooleanField(
        'יכולים לשלם על תרופות וטיפולים',
        blank=True,
        default=False,
    )
    can_handle_sick = models.BooleanField(
        'יכולים לטפל בבע"ח פצועים או חולים',
        blank=True,
        default=False,
    )
    can_handle_bad_behaviour = models.BooleanField(
        'יכולים לטפל בבעיות התנהגות (לא בעלי חיים אגרסיביים)',
        blank=True,
        default=False,
    )
    can_handle_aggressive = models.BooleanField(
        'יכולים לטפל בבעלי חיים אגרסיבים',
        blank=True,
        default=False,
    )

    animals = MultiSelectField(choices=ANIMAL)

    agree_to_no_time_limit = models.BooleanField(
        'אני מודע/ת לכך שהאומנה היא ללא מגבלת זמן',
    )
    agree_to_no_transfer = models.BooleanField(
        'אני מודע/ת לכך שאני לא אוכל למסור את האומנה ללא אישור דימונה אוהבת חיות',
    )
    agree_to_pay = models.BooleanField(
        'אני מודע/ת לכך שאני אצטרך לשלם על כל הצרכים של האומנה אלא אם דימונה אוהבת חיות תשתתף',
    )
    agree_to_week = models.BooleanField(
        'אני מודע/ת לכך שאני לא יכול/ה לסיים את האומנה ללא הודעה מראש של לפחות שבוע לדימונה אוהבת חיות',
    )
    agree_to_take = models.BooleanField(
        'אני מודע/ת לכך שאני אצטרף לקחת את האומנה לכל מקום שנדרש בעצמי',
    )
    agree_to_photo = models.BooleanField(
        'אני מודע/ת לכך שאני אצטרך לספק תמונות של האומנה לדימונה אוהבת חיות',
    )
    agree_to_bring = models.BooleanField(
        'אני מודע/ת לכך שאני אצטרך להביא את האומנה לימי אימוץ כנדרש',
    )
    accept_terms = models.BooleanField(
        'אני מאשר/ת את התנאים',
    )

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '%s (Age %s) | %s | %s' % (self.full_name, self.age(), self.phone, self.email)


class Foster(models.Model):
    angel = models.ForeignKey(Angel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  # pet name
    start_date = models.DateTimeField('starting date')
    end_date = models.DateTimeField('ending date')
    comment = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
