import mimetypes
from pathlib import Path

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.core.validators import RegexValidator
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class FileValidator(object):
    """
    Validator for files, checking the size, extension and mimetype.
    Initialization parameters:
        allowed_extensions: iterable with allowed file extensions
            ie. ('txt', 'doc')
        allowd_mimetypes: iterable with allowed mimetypes
            ie. ('image/png', )
        min_size: minimum number of bytes allowed
            ie. 100
        max_size: maximum number of bytes allowed
            ie. 24*1024*1024 for 24 MB
    Usage example::
        MyModel(models.Model):
            myfile = FileField(validators=[FileValidator(max_size=24*1024*1024)])

        2.5MB - 2621440
        5MB - 5242880
        10MB - 10485760
        20MB - 20971520
        50MB - 5242880
        100MB 104857600
        250MB - 214958080
        500MB - 429916160
    """
    # requires_context = True
    extension_message = _("Extension '%(extension)s' not allowed. Allowed extensions are: '%(allowed_extensions)s'")
    mime_message = _("MIME type '%(mimetype)s' is not valid. Allowed types are: %(allowed_mimetypes)s.")
    min_size_message = _('The current file %(size)s, which is too small. The minumum file size is %(allowed_size)s')
    max_size_message = _('The current file %(size)s, which is too large. The maximum file size is %(allowed_size)s')

    def __init__(self, *args, **kwargs):
        self.allowed_extensions = kwargs.pop('allowed_extensions', None)
        self.allowed_mimetypes = kwargs.pop('allowed_mimetypes', None)
        self.min_size = kwargs.pop('min_size', 0)
        self.max_size = kwargs.pop('max_size', None)

    def __call__(self, value: TemporaryUploadedFile):
        """
        Check the extension, content type and file size.
        """

        # Check the extension
        ext = Path(value.name).suffix[1:].lower()
        if self.allowed_extensions and ext not in self.allowed_extensions:
            raise ValidationError(self.extension_message,
                                  params={
                                      'extension': ext,
                                      'allowed_extensions': ', '.join(self.allowed_extensions)
                                  },
                                  code='invalid_extension'
                                  )

        # Check the content type
        mimetype = mimetypes.guess_type(value.name)[0]
        if self.allowed_mimetypes and mimetype not in self.allowed_mimetypes:
            raise ValidationError(self.mime_message,
                                  params={
                                      'mimetype': mimetype,
                                      'allowed_mimetypes': ', '.join(self.allowed_mimetypes)
                                  },
                                  code='invalid_mimetype'
                                  )

        # Check the file size
        if self.max_size and value.size > self.max_size:
            raise ValidationError(self.max_size_message,
                                  params={
                                      'size': filesizeformat(value.size),
                                      'allowed_size': filesizeformat(self.max_size)
                                  },
                                  code='invalid_max_size'
                                  )

        elif value.size < self.min_size:
            raise ValidationError(self.min_size_message,
                                  params={
                                      'size': filesizeformat(value.size),
                                      'allowed_size': filesizeformat(self.min_size)
                                  },
                                  code='invalid_min_size'
                                  )


validate_phone = RegexValidator(
    regex=r"^\+?998\d{9}$",
    message="Phone number must begin with 998 or (+998) and contain only 12 numbers",
)


def validate_json(value):
    if not isinstance(value, dict):
        raise ValidationError("This field must be an object.")
    if len(value) == 0:
        raise ValidationError("This field must not be empty.")


from rest_framework.exceptions import ValidationError


def img_check(value):
    if len(value) > 3:
        raise ValidationError('3 dan kop qoshib bolmidi')
    return value


class GalleryCreateSerializerValidator:
    def is_file_type_exist(self, args, **kwargs):

        if 'file_type' not in args and args.get('type') in (1,):
            raise ValidationError('File_type is required')
        elif args.get('file_type') in (3, 4) and 'url' not in args:
            raise ValidationError('Url is required when youtube or mover file added')

    def __call__(self, *args, **kwargs):
        self.is_file_type_exist(*args, **kwargs)
