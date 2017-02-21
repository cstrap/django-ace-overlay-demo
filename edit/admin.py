from django.contrib import admin

from .models import Edit
from django import forms
from ace_overlay.widgets import AceOverlayWidget


class EditAdminForm(forms.ModelForm):
    text = forms.CharField(widget=AceOverlayWidget(mode='html', wordwrap=False, theme='twilight', width="850px", height="800px", showprintmargin=True), required=False)
    class Meta:
        model = Edit
        fields = '__all__'


@admin.register(Edit)
class EditAdmin(admin.ModelAdmin):
    form = EditAdminForm
