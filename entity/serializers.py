from rest_framework import serializers


from .models import Entity, Exec_Proc, Negative, Balance, Sum, Branch, Leader, Founders, Activity, License, Stop_Params


class Negative_Serializer(serializers.ModelSerializer):
    """Сериализатор Негативных полей."""

    params = serializers.SerializerMethodField('param')

    @staticmethod
    def param(obj):
        """Регулярное выражение для парсинга нарушений"""
        import re

        text = re.sub(r'\([^()]*\)', '', str(list(obj)[0].text))
        return text.split(';')

    class Meta:
        """Метакласс сериализатора."""

        model = Negative
        fields = ['id', 'params']


class Branch_Serializer(serializers.ModelSerializer):
    """Сериализация Фелиалов."""

    class Meta:
        """Метакласс сериализатора."""

        model = Branch
        fields = ('name', 'entity')


class Exec_Serializer(serializers.ModelSerializer):
    """Сериализация Статей."""

    class Meta:
        """Метакласс сериализатора."""

        model = Exec_Proc
        fields = ('inn', 'date', 'article',)


class Sum_Serializer(serializers.ModelSerializer):
    """Сериализатор Cуммы."""

    class Meta:
        """Метакласс сериализатора."""

        model = Sum
        fields = ('year', 'sum')


class Balance_Serializer(serializers.ModelSerializer):
    """Сериализатор баланса."""
    sums = serializers.SerializerMethodField('_get_sums')

    @staticmethod
    def _get_sums(obj):
        """Получение всех детей модели Статьи."""
        serializer = Sum_Serializer(
            Sum.objects.filter(year=obj), many=True)
        return serializer.data

    class Meta:
        """Метакласс сериализатора."""

        model = Balance
        fields = ('inn', 'year', 'sums')


class Activity_Serializer(serializers.ModelSerializer):
    """Сериализатор деятельности."""

    class Meta:
        """Метакласс сериализатора."""

        model = Activity
        fields = ['id', 'name', 'base', 'activity']


class Founders_Serializer(serializers.ModelSerializer):
    """Сериализатор учредителей."""

    class Meta:
        """Метакласс сериализатора."""

        model = Founders
        fields = ['inn', 'type', 'sur_ip', 'name_ip', 'pat_ip', 'name', 'date_reg', 'inn_entity']


class License_Serializer(serializers.ModelSerializer):
    """Сериализатор лицензий."""

    class Meta:
        """Метакласс сериализатора."""

        model = License
        fields = ['series', 'date_start', 'date_end', 'inn']


class Entity_Serializer(serializers.ModelSerializer):
    """Сериализация  юр лиц."""

    exec_proc = serializers.SerializerMethodField('_get_exec')
    balance = serializers.SerializerMethodField('_get_balance')
    branch = serializers.SerializerMethodField('_get_branch')
    founders = serializers.SerializerMethodField('_get_founders')
    activity = serializers.SerializerMethodField('_get_activity')
    licenses = serializers.SerializerMethodField('_get_licenses')
    negative_par = serializers.SerializerMethodField('_get_negative_par')
    stop_params = serializers.SerializerMethodField('_get_stop')

    @staticmethod
    def _get_exec(obj):
        """Получение всех детей модели Статьи."""
        serializer = Exec_Serializer(
            Exec_Proc.objects.filter(exec_proc=obj), many=True)
        return serializer.data

    @staticmethod
    def _get_balance(obj):
        """Получение всех детей модели Баланс."""
        serializer = Balance_Serializer(
            Balance.objects.filter(inn=obj), many=True)
        return serializer.data

    @staticmethod
    def _get_branch(obj):
        """Получение всех детей модели Филиалы."""
        serializer = Branch_Serializer(
            Branch.objects.filter(entity=obj), many=True)
        return serializer.data

    @staticmethod
    def _get_founders(obj):
        """Получение всех детей модели Учредители."""
        serializer = Founders_Serializer(
            Founders.objects.filter(inn_entity=obj), many=True)
        return serializer.data

    @staticmethod
    def _get_licenses(obj):
        """Получение всех детей модели Лицензии."""
        serializer = License_Serializer(
            License.objects.filter(inn=obj), many=True)
        return serializer.data

    @staticmethod
    def _get_negative_par(obj):
        """Получение всех детей модели Лицензии."""
        serializer = Negative_Serializer(
            Negative.objects.filter(entity=obj))
        return serializer.data

    @staticmethod
    def _get_activity(obj):
        """Получение всех детей модели Лицензии."""
        serializer = Activity_Serializer(
            Activity.objects.filter(activity=obj), many=True)
        return serializer.data

    @staticmethod
    def _get_stop(obj):
        """Получение всех детей модели Требований."""
        serializer = Stop_Serializer(obj.stop)
        return serializer.data

    class Meta:
        """Метакласс сериализатора."""

        model = Entity
        fields = ('inn', 'exec_proc', 'balance', 'branch', 'name_entity', 'founders', 'form', 'activity', 'licenses',
                  'ogrn', 'kpp', 'sur_ip', 'name_ip', 'pat_ip', 'date_reg', 'status', 'date_stat', 'date_term',
                  'capital', 'address', 'leader', 'black_list', 'number_stuff', 'negative_par', 'stop_params')


class Leader_Serializer(serializers.ModelSerializer):
    """Сериализатор владельца."""

    companys = serializers.SerializerMethodField('_get_companys')

    @staticmethod
    def _get_companys(obj):
        """Получение всех детей модели Лицензии."""
        serializer = Entity_Serializer(
            Entity.objects.filter(entity=obj))
        return serializer.data

    class Meta:
        """Метакласс сериализатора."""

        model = Leader
        fields = ['inn', 'surname', 'name', 'patronymic', 'companys']


class Stop_Serializer(serializers.ModelSerializer):

    class Meta:
        """Метакласс сериализатора."""
        model = Stop_Params
        fields = ['license', 'bankrupt', 'acting', 'debt', 'criminal', 'rights', 'ofhor']