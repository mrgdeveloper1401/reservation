from typing import Any
from django.db.models import CharField, Model
from django.core .exceptions import ValidationError


class CombindField(CharField):
    description = 'Combind field for flight'
    
    def __init__(self,  *args: Any, **kwargs: Any):
        kwargs['max_length'] = 10
        super().__init__(*args, **kwargs)
        
    def validate(self, value: Any, model_instance: Model):
        if not value.startswith('air'):
            raise ValidationError('Field must start with air')
        if len(value) >= 4 and  not value[3:].isdigit():
            raise ValidationError('Field must number')
        return super().validate(value, model_instance)