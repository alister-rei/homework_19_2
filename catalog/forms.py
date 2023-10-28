from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price')

    def clean_name_description(self):
        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        cleaned_data = super().clean()

        name = self.cleaned_data['product_name']
        description = self.cleaned_data['product_description']

        for item in stop_list:
            if item in name.lower():
                raise forms.ValidationError(f'Слово "{item}" запрещено к использованию, выберите другое')

            if item in description.lower():
                raise forms.ValidationError(f'Слово "{item}" запрещено к использованию, выберите другое')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    ACTIVE_VERSIONS = []  # задаем список активных версий товара

    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_current(self):
        """
        Определяет количество активных версий товара
        """
        cleaned_data = super().clean()
        version = self.cleaned_data['is_current']

        if version:
            VersionForm.ACTIVE_VERSIONS.append(True)

        if len(VersionForm.ACTIVE_VERSIONS) > 1:
            print('>1')
            raise forms.ValidationError('Возможна лишь одна активная версия. Пожалуйста, активируйте только 1 версию.')

        return cleaned_data
