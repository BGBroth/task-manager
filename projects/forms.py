from django import forms


class ProjectSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by project name",
                   "class": "form-control search-bar-short",
                   "id": "topbarInputIconLeft",
                   "aria-label": "Search",
                   "aria-describedby": "search-button",
                   "style": "max-width: 250px; width: 100%;"
                   }
        )
    )


class TeamSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by team name",
                   "class": "form-control search-bar-short",
                   "id": "topbarInputIconLeft",
                   "aria-label": "Search",
                   "aria-describedby": "search-button",
                   "style": "max-width: 250px; width: 100%;"
                   }
        )
    )