from django import forms
from crispy_forms.helper import FormHelper
from .validators import validate_file_size, validate_file_extension
from django.utils.translation import gettext_lazy as _

class OrderForm(forms.Form):
    PRINT_OPTIONS = (
        ('Full Colour', 'Full Colour'),
        ('Black & White', 'Black & White'),
    )

    PAGE_OPTIONS = (
        ('Normal Paper (70GSM)', 'Normal Paper (70GSM)'),
        ('Normal Paper (75GSM)', 'Normal Paper (75GSM)'),
        ('Bond Paper (80GSM)', 'Bond Paper (80GSM)'),
        ('Glossy Paper (180GSM)', 'Glossy Paper (180GSM)'),
    )

    COVER_OPTIONS = (
        ('No Cover', 'No Cover'),
        ('Thick Colored Cover', 'Thick Colored Cover'),
        ('Cover with Design', 'Cover with Design'),
    )

    BINDING_OPTIONS = (
        ('No Binding', 'No Binding'),
        ('Corner Staple', 'Corner Staple'),
        ('Full Staple', 'Full Staple'),
        ('Spiral Bind', 'Spiral Bind'),
    )

    name = forms.CharField(label = 'Name', max_length = 100)
    mobno = forms.CharField(label = 'Mobile No. (WhatsApp No.)', max_length = 100)
    email = forms.CharField(label = 'Email ID', max_length = 100)
    address = forms.CharField(label = 'Full Address & PIN Code', max_length = 300)
    docupload = forms.FileField(label = 'Upload Document', validators=[validate_file_size, validate_file_extension])
    printcolour = forms.CharField(label = 'Print Colour', max_length = 200, widget = forms.Select(choices = PRINT_OPTIONS))
    pagetype = forms.CharField(label = 'Page Type', max_length = 200, widget = forms.Select(choices = PAGE_OPTIONS))
    coveroption = forms.CharField(label = 'Cover Option', max_length = 200, widget = forms.Select(choices = COVER_OPTIONS))
    bindingoption = forms.CharField(label = 'Binding Option', max_length = 200, widget = forms.Select(choices = BINDING_OPTIONS))
    extracomment = forms.CharField(label = 'Extra Comments', max_length = 300, required = False)
    pagecount = forms.IntegerField(label = 'Page Count (For Non PDF)', max_value = 500, initial = 0)
    copies = forms.IntegerField(label = 'Number of Copies', max_value = 500, initial = 1)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 