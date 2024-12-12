from django import forms
from django.contrib.auth.forms import UserCreationForm

from workers.models import Worker


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
        )


class WorkerSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by worker name",
                "class": "form-control search-bar-short",
                "id": "topbarInputIconLeft",
                "aria-label": "Search",
                "aria-describedby": "search-button",
                "style": "max-width: 250px; width: 100%;"
            }
        )
    )



class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by position name",
                   "class": "form-control search-bar-short",
                   "id": "topbarInputIconLeft",
                   "aria-label": "Search",
                   "aria-describedby": "search-button",
                   "style": "max-width: 250px; width: 100%;"
                   }
        )
    )