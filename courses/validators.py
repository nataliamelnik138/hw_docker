from rest_framework.serializers import ValidationError


class LinkToVideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if not ('youtube.com' in tmp_val):
            raise ValidationError('You can only add links to videos on youtube.com')
