import io
from uuid import uuid4

from PIL import Image
from django.core.files import File
from django.db import models


class ResizeImageField(models.ImageField):
    """
        Auto resize image field
        :param size: The requested size in pixels, as a 2-tuple:
    """

    def __init__(self, size, **kwargs):
        super(ResizeImageField, self).__init__(**kwargs)

        self.size = size

    def to_python(self, value):
        image = Image.open(value.file).resize(size=self.size)
        output = io.BytesIO()
        image.save(fp=output, format='JPEG')
        output.seek(0)

        return File(output, f'{uuid4().hex.upper()[0:6]}.jpg')

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['size'] = self.size
        return name, path, args, kwargs
