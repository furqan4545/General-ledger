from django import forms
from basic_app.models import Post, People


class PostForm(forms.ModelForm):

    # we need to connect this meta class to the model we r using.  and then we also wanna connect the field that we want to edit in this form. 
    class Meta():
        model = Post
        fields = ('com_name', 'total_price', 'quantity', 'unit', 'create_date')


        # UNIT_CHOICES = [
        #     ('kg', 'kilogram'),
        #     ('gm', 'gram')
        # ]
        # unit = forms.CharField(label="Choose units", widget=forms.RadioSelect(choices=UNIT_CHOICES))
        
        
class PeopleForm(forms.ModelForm):

    class Meta():
        model = People
        fields = ('name', 'total_bill', 'paid_money', 'item_name', 'date')

        # let's add the widget.

        # widgets = {
        #     'com_name': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})  # so text widget is connected to 3 css classes. 
        # }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['com_name'].label = "Product Name"
        #     self.fields['price'].label = "Single Product Price"
        #     self.fields['quantity'].label = "Quantity"
            



