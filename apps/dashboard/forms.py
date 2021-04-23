from django.forms.models import ModelChoiceField
from apps.dashboard.models import Asset, AssignAsset, Category, Designation, Employee
from django import forms
# from searchableselect.widgets import SearchableSelect


class EmployeeForm(forms.ModelForm):  
    class Meta:
        model = Employee
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email' : forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),
            'designation': forms.Select(attrs={'class':'form-control','placeholder':'Designation'}),
            'phone' : forms.TextInput(attrs={'minlength': 10, 'maxlength': 15, 'required': True, 'type': 'number','class':'form-control'}), 
            'address' : forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
       }
        fields = "__all__"
        exclude =('status',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['designation'].queryset = Designation.objects.all()
        self.fields['designation'].empty_label = "------Select Designation------"
    
    # def clean_email(self):
    #       email = self.cleaned_data['email']
    #       print(email)
    #       if Employee.objects.filter(email=email).exists():
    #           raise forms.ValidationError("Already Exists")
    #       return email
        
class DesignationForm(forms.ModelForm):  
    
    class Meta:
        model = Designation
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}),  
        }
        fields = "__all__"
        

    
    
class AssetForm(forms.ModelForm):  
    class Meta:
        model = Asset
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Asset Name'}),
            'category' : forms.Select(attrs={'class':'form-control','placeholder':'Category'}),
            'model_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Model Number'}),
            'availability' : forms.CheckboxInput(attrs={'class':'form-check-input'}), 
            # 'employee' : forms.Select(attrs={'class':'form-control'}),
            # 'expire_date' : forms.TextInput(attrs={'class':'form-control','type': 'date'}),
       }
        fields = "__all__"
        exclude =('availability',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].empty_label = "------Select Category------"



class AssetUpdateForm(forms.ModelForm):  
    class Meta:
        model = Asset
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Asset Name'}),
            'category' : forms.Select(attrs={'class':'form-control','placeholder':'Category'}),
            'model_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Model Number'}),
            'availability' : forms.CheckboxInput(attrs={'class':'form-check-input'}), 
           
       }
        fields = "__all__"
        exclude =('employee','expire_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].empty_label = "------Select Category------"

        


class CategoryForm(forms.ModelForm):  
    
    class Meta:
        model = Category
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Category'}),  
        }
        fields = "__all__"



class AssignAssetForm(forms.ModelForm):  
    class Meta:
        model = AssignAsset
        widgets = {
            'employee' : forms.Select(attrs={'class':'form-control'}),
            'asset' : forms.Select(attrs={'class':'form-control'}),
            'expire_on' : forms.TextInput(attrs={'class':'form-control','type': 'date'}),
       }
        fields = "__all__"
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['asset'].queryset =Asset.objects.all()
            self.fields['asset'].empty_label = "------Select Asset------"
            self.fields['employee'].queryset = Employee.objects.all()
            self.fields['employee'].empty_label = "------Select Employee------"


