import re

from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import RegexForm


class RegexFormView(FormView):
    form_class = RegexForm
    template_name = 'regex_editor/index.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            regex_type = form.cleaned_data['regex_type']
            regex_flag = form.cleaned_data['regex_flag']
            regex = form.cleaned_data['regex']
            substitution = form.cleaned_data['substitution']
            test_string = form.cleaned_data['test_string']

            if regex_type == "findall":
                context = regex_options(form, re.findall, regex, test_string, regex_flag)
            elif regex_type == "sub":
                context = regex_options(form, re.subn, regex, test_string, regex_flag, substitution)
            elif regex_type == "split":
                context = regex_options(form, re.split, regex, test_string, regex_flag)

            return render(request, self.template_name, context)

        else:
            print(form.errors)

        return render(request, self.template_name, context)


def regex_options(form, regex_type, regex, test_string, flags=list(), substitution=None):
    """Design regex in function of user's choice"""
    if regex_type == re.subn:
        if flags:
            my_regex = regex_type(f"(?{''.join(flags)})" + regex, substitution, test_string)
        else:
            my_regex = regex_type(regex, substitution, test_string)
        if my_regex[1] != 0:
            context = {'form': form, 'result': [my_regex[0]], "match_count": my_regex[1]}
            return context
        else:
            context = {'form': form, 'result': "No results", "match_count": 0}
            return context
    else:
        if flags:
            my_regex = regex_type(f"(?{''.join(flags)})" + regex, test_string)
        else:
            my_regex = regex_type(regex, test_string)
        if my_regex:
            context = {'form': form, 'result': my_regex, "match_count": len(my_regex)}
            return context
        else:
            context = {'form': form, 'result': "No results", "match_count": 0}
            return context
