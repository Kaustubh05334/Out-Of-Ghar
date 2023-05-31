from django import forms
from django.core.exceptions import ValidationError

def validate_image_size(value):
    # Set the maximum file size (in bytes)
    max_size = 5 * 1024 * 1024  # 5 MB

    if value.size > max_size:
        raise ValidationError(f"The maximum file size allowed is {max_size}")
class BlogPostForm(forms.Form):
    title = forms.CharField(label='Title',max_length=100,widget=forms.TextInput(attrs={'class':'inptitle','name':'heading'}))
    location = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'id':'location-input','class':'inploc','name':'location'}))
    content = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpcontent','name':'content'}))
    thumbnail = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'thumbnail'}))

    # first subform (all fields are required)
    subheading1 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading1'}))
    subloc1 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc1'}))
    subimage1 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage1'}))
    subtext1 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext1'}))

    # second subform
    subheading2 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading2'}),required=False)
    subloc2 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc2'}),required=False)
    subimage2 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage2'}),required=False)
    subtext2 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext2'}),required=False)

    # third subform
    subheading3 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading3'}),required=False)
    subloc3 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc3'}),required=False)
    subimage3 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage3'}),required=False)
    subtext3 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext3'}),required=False)

    # fourth subform
    subheading4 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading4'}),required=False)
    subloc4 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc4'}),required=False)
    subimage4 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage4'}),required=False)
    subtext4 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext4'}),required=False)

    # fifth subform
    subheading5 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading5'}),required=False)
    subloc5 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc5'}),required=False)
    subimage5 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage5'}),required=False)
    subtext5 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext5'}),required=False)

    # sixth subform
    subheading6 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading6'}),required=False)
    subloc6 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc6'}),required=False)
    subimage6 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage6'}),required=False)
    subtext6 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext6'}),required=False)

    # seventh subform
    subheading7 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading7'}),required=False)
    subloc7 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc7'}),required=False)
    subimage7 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage7'}),required=False)
    subtext7 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext7'}),required=False)

    # eighth subform
    subheading8 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading8'}),required=False)
    subloc8 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc8'}),required=False)
    subimage8 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage8'}),required=False)
    subtext8 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext8'}),required=False)

    # ninth subform
    subheading9 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading9'}),required=False)
    subloc9 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc9'}),required=False)
    subimage9 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage9'}),required=False)
    subtext9 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext9'}),required=False)

    # tenth subform
    subheading10 = forms.CharField(label='Heading',max_length=100,widget=forms.TextInput(attrs={'class':'inpsubheading','name':'subheading10'}),required=False)
    subloc10 = forms.CharField(label='Location',max_length=50,widget=forms.TextInput(attrs={'class':'inpsubloc','name':'subloc10'}),required=False)
    subimage10 = forms.ImageField(validators=[validate_image_size],widget=forms.ClearableFileInput(attrs={'class': 'image','name':'subimage10'}),required=False)
    subtext10 = forms.CharField(label='Content',widget=forms.Textarea(attrs={'class':'inpsubtext','name':'subtext10'}),required=False)


class CommentForm(forms.Form):
    content = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))

class AdminCommentForm(forms.Form):
    CHOICES = [
        ('Approve', 'Approve'),
        ('Reject', 'Reject'),
    ]
    status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    content = forms.CharField(label ="",required=False, widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50,
    }))
