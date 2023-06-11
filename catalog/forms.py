from django import forms
from django.forms import formset_factory
from catalog.models import Blog, Product, Version
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper


class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'header',
            'slug',
            Submit('submit', 'Submit', css_class='btn-primary')
        )

    class Meta:
        model = Blog
        fields = ['header', 'slug']

        widgets = {
            'header': forms.TextInput(attrs={'placeholder': 'Enter header'})
        }

    def clean_header(self):
        header = self.cleaned_data.get('header')
        if len(header) < 3:
            raise forms.ValidationError('Слишком коротко')

        return header


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
            'category',
            'price_for_buy',
            'publication_sign',
            Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price_for_buy', 'publication_sign']

    def clean_name(self):
        stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                      'радар']
        name = self.cleaned_data.get('name')
        for i in stop_words:
            if i in name:
                raise forms.ValidationError('Эти товары запрещены')
            break

        return name


class ProductVersion(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'product',
            'version_number',
            'version_name',
            'version_sign',
            Submit('submit', 'Submit', css_class='btn-primary')
        )

    class Meta:
        model = Version
        fields = '__all__'
