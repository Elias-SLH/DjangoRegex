from django import forms


class RegexForm(forms.Form):
    TYPE_CHOICES = [('findall', 'findall'),
                ('sub', 'sub'),
                ('split', 'split')]

    FLAG_CHOICES = [('i', 'ignorecase'),
                ('m', 'multiline'),
                ('s', 'dotall')]

    regex_type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect(), initial="findall")
    regex_flag = forms.MultipleChoiceField(choices=FLAG_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False)
    regex = forms.CharField(max_length=200)
    substitution = forms.CharField(max_length=200, required=False)
    test_string = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(RegexForm, self).__init__(*args, **kwargs)

        self.fields['regex_type'].widget.attrs['id'] = 'regex_type'
        self.fields['regex_type'].widget.attrs['onchange'] = 'regexType()'
        self.fields['regex'].widget.attrs['class'] = 'form-control'
        self.fields['regex'].widget.attrs['style'] = 'width:970px'
        self.fields['regex'].widget.attrs['placeholder'] = 'Insert your regular expression here'
        self.fields['substitution'].widget.attrs['class'] = 'form-control'
        self.fields['substitution'].widget.attrs['style'] = 'width: 970px; display: none; margin-bottom: 25px;'
        self.fields['substitution'].widget.attrs['placeholder'] = 'Insert your substitution value here'
        self.fields['substitution'].widget.attrs['id'] = 'substitution'
        self.fields['test_string'].widget.attrs['class'] = 'form-control'
        self.fields['test_string'].widget.attrs['style'] = 'width:970px'
        self.fields['test_string'].widget.attrs['placeholder'] = 'Insert your test string here'
        self.fields['test_string'].widget.attrs['id'] = 'test_string'
