from django import forms


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by task name",
                   "class": "form-control search-bar-short",
                   "id": "topbarInputIconLeft",
                   "aria-label": "Search",
                   "aria-describedby": "search-button",
                   "style": "max-width: 250px; width: 100%;"
                   }
        )
    )


class TaskTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by task type",
                   "class": "form-control search-bar-short",
                   "id": "topbarInputIconLeft",
                   "aria-label": "Search",
                   "aria-describedby": "search-button",
                   "style": "max-width: 250px; width: 100%;"
                   }
        )
    )


class TagSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by tag name",
                   "class": "form-control search-bar-short",
                   "id": "topbarInputIconLeft",
                   "aria-label": "Search",
                   "aria-describedby": "search-button",
                   "style": "max-width: 250px; width: 100%;"
                   }
        )
    )
