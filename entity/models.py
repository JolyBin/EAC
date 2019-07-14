from django.db import models


from directory.models import City


class Entity(models.Model):
    """Модель Юридические лица."""

    inn = models.CharField('ИНН', primary_key=True, max_length=12, blank=True)
    name_entity = models.TextField('Наименование', blank=True)
    form = models.CharField('Форма', max_length=20, choices=[('Юридическое лицо', 'Юридическое лицо'),
                                                             ('Индивидуальный предприниматель',
                                                              'Индивидуальный предприниматель')])
    ogrn = models.CharField('ОГРН', max_length=25, blank=True)
    kpp = models.CharField('КПП', max_length=25, blank=True)
    sur_ip = models.CharField('Фамилия ИП', null=True, max_length=25, default='', blank=True)
    name_ip = models.CharField('Иимя ИП', null=True, max_length=25, default='', blank=True)
    pat_ip = models.CharField('Отчество ИП', null=True, max_length=25, default='', blank=True)
    date_reg = models.DateField('Дата регистрации', blank=True)
    status = models.CharField('Статус', max_length=20, blank=True)
    date_stat = models.DateField('Дата статуса', blank=True)
    date_term = models.DateField('Дата прекращения', blank=True)
    capital = models.PositiveIntegerField('Капитал суммы', blank=True)
    address = models.ForeignKey(City, verbose_name='Город', on_delete=models.CASCADE, blank=True)
    leader = models.ForeignKey('Leader', verbose_name='Руководитель', on_delete=models.CASCADE, blank=True)
    black_list = models.BooleanField('Черный список', blank=True)
    number_stuff = models.IntegerField('Численность персонала', blank=True)
    negative = models.OneToOneField('Negative', verbose_name='Негативные показатели', on_delete=None, blank=True)
    stop = models.OneToOneField('Stop_Params', verbose_name='Параметры блокировки',
                                on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.inn)

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Юридическое лицо или ИП'
        verbose_name_plural = 'Юридические лица или ИП'


class Founders(models.Model):
    """Модель Учредителей."""

    inn = models.CharField('ИНН', max_length=12)
    type = models.CharField('Тип', choices=[('Юридическое лицо', 'Юридическое лицо'),
                                            ('Физическое лицо', 'Физическое лицо')], max_length=20, blank=True)
    sur_ip = models.CharField('Фамилия ИП', null=True, max_length=25, default='', blank=True)
    name_ip = models.CharField('Иимя ИП', null=True, max_length=25, default='', blank=True)
    pat_ip = models.CharField('Отчество ИП', null=True, max_length=25, default='', blank=True)
    name = models.TextField('Наименование', null=True, blank=True)
    date_reg = models.DateField('Дата регистрации', null=True, blank=True)
    address = models.ForeignKey(City, verbose_name='Адрес', on_delete=models.CASCADE, null=True, blank=True)
    inn_entity = models.ForeignKey('Entity', verbose_name='Организация/ИП', on_delete=models.CASCADE, null=True, blank=True, default='2724163941')

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.inn)

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Учредитель'
        verbose_name_plural = 'Учредители'


class Exec_Proc(models.Model):
    """Модель ИсполнительныХ производств."""

    exec_proc = models.ForeignKey('Entity', verbose_name='ИНН', on_delete=models.CASCADE, blank=True)
    date = models.DateField('Дата', blank=True)
    article = models.CharField('Статья', max_length=20, blank=True)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.article)

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Negative(models.Model):
    """Негативные показатели."""

    text = models.TextField('Негативные показатели', blank=True)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.text)

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Негативный показатель'
        verbose_name_plural = 'Негативные показатели'


class Balance(models.Model):
    """Модель Бух баланс за год."""

    inn = models.ForeignKey('Entity', verbose_name='Организация', on_delete=models.CASCADE, blank=True)
    year = models.PositiveSmallIntegerField('Год', blank=True)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.inn) + ' ' + str(self.year)

    class Meta:
        """Мета класс модели."""

        unique_together = (('inn', 'year'),)
        verbose_name = 'Бух баланс'
        verbose_name_plural = 'Бух балансы'


class Sum(models.Model):
    """Модель Суммы за год."""
    id = models.CharField('Код баланса', max_length=4, primary_key=True)
    year = models.ForeignKey('Balance', verbose_name='Год', on_delete=models.CASCADE, blank=True)
    sum = models.IntegerField('Сумма', blank=True)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.sum)

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Сумма за год'
        verbose_name_plural = 'Суммы за года'


class Branch(models.Model):
    """Модель Филиалы."""

    name = models.CharField('Наименование', max_length=40, blank=True)
    address = models.ForeignKey(City, verbose_name='Адрес', on_delete=models.CASCADE, blank=True)
    entity = models.ForeignKey('Entity', verbose_name='ЮР лицо', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.name)

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'


class Leader(models.Model):
    """Модель Руководитель."""

    inn = models.CharField('ИНН руководителя', primary_key=True, max_length=12, blank=True)
    surname = models.CharField('Фамилия', max_length=20, blank=True)
    name = models.CharField('Имя', max_length=20, blank=True)
    patronymic = models.CharField('Отчество', max_length=20, blank=True)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.surname) + ' ' + str(self.name)

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'


class Activity(models.Model):
    """Модель Деятельности."""

    id = models.CharField('ОКВД', primary_key=True, max_length=15)
    name = models.TextField('Наименование деятельности', blank=True)
    base = models.BooleanField('Основной вид деятельности')
    activity = models.ManyToManyField('Entity', verbose_name='Организация', related_name='activity_entity', blank=True)

    def __str__(self):
        """Метод строкового представления модели."""
        return str(self.name)

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельность'


class License(models.Model):
    """Модель Лицензии."""

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

    series = models.CharField('Серия', primary_key=True, max_length=20)
    date_start = models.DateField('Дата начала', blank=True)
    date_end = models.DateField('Дата конца', blank=True)
    inn = models.ForeignKey('Entity', verbose_name='Лицензия', on_delete=models.CASCADE, default='2724163941')
    activity = models.TextField('Вид деятельности', default=' ')

    def __str__(self):
        """Метод строкового представления модели."""
        return 'Серия: ' + str(self.series)


class Stop_Params(models.Model):
    """Модель соответствия ФЗ44."""

    class Meta:
        """Мета класс модели."""

        verbose_name = 'Соответствие'
        verbose_name_plural = 'Соответствия'

    license = models.BooleanField('Лиценизия действующая')
    bankrupt = models.BooleanField('Банкрот')
    acting = models.BooleanField('Действующий')
    debt = models.BooleanField('Задолженность')
    criminal = models.BooleanField('Судимость')
    rights = models.BooleanField('Права')
    relatives = models.BooleanField('Родственники')
    ofhor = models.BooleanField('Офшорная компания')
