from rest_framework import serializers, fields

from foster.models import Angel, ANIMAL


class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))


class AngelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Angel
        fields = (
            'id',
            'about_home',
            'full_name',
            'email',
            'phone',
            'call_at_night',
            'address',
            'dob',
            'comment',
            'animals',
            'foster_at_home',
            'home_with_garden',
            'have_car',
            'can_pay_food',
            'can_pay_medicine',
            'can_handle_sick',
            'can_handle_bad_behaviour',
            'can_handle_aggressive',
            'agree_to_no_time_limit',
            'agree_to_no_transfer',
            'agree_to_pay',
            'agree_to_week',
            'agree_to_take',
            'agree_to_photo',
            'agree_to_bring',
            'accept_terms',
        )

    animals = CustomMultipleChoiceField(choices=ANIMAL)
    agree_to_no_time_limit = fields.BooleanField(required=True)
    agree_to_no_transfer = fields.BooleanField(required=True)
    agree_to_pay = fields.BooleanField(required=True)
    agree_to_week = fields.BooleanField(required=True)
    agree_to_take = fields.BooleanField(required=True)
    agree_to_photo = fields.BooleanField(required=True)
    agree_to_bring = fields.BooleanField(required=True)
    accept_terms = fields.BooleanField(required=True)

    def validate_agree_to_no_time_limit(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value

    def validate_agree_to_no_transfer(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value

    def validate_agree_to_pay(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value

    def validate_agree_to_week(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value

    def validate_agree_to_take(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value

    def validate_agree_to_photo(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value

    def validate_agree_to_bring(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value

    def validate_accept_terms(self, value):
        if not value:
            raise serializers.ValidationError("Validation error")
        return value
