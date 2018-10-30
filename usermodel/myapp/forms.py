from django import forms;
from django.contrib.auth.forms import ReadOnlyPasswordHashField;
from django.contrib.auth.models import Group;
from django.contrib.auth import get_user_model,authenticate;
from django.db.models import Q;
MyUser=get_user_model();
class UserLoginForm(forms.Form):
    query=forms.CharField(max_length=256,label="Username/Email");
    password=forms.CharField(max_length=256,widget=forms.PasswordInput,label="Password");
    def clean(self,*args,**kwargs):
        query=self.cleaned_data.get('query');
        password=self.cleaned_data.get('password');
        value=MyUser.objects.filter(
            Q(username__iexact=query)|Q(email__iexact=query)
        ).distinct().first();
        #value=value.distinct().first();
        result=authenticate(username=value,password=password);
        if not result:
            raise forms.ValidationError("In Valid Login Settinges");
        # query=self.cleaned_data.get('query');
        # password=self.cleaned_data.get('password');
        # # username=MyUser.objects.filter(username__iexact=query).first();
        # # email=MyUser.objects.filter(email__iexact=query).first();
        # # if username.ex
        # # password=self.cleaned_data.get('password');
        # result=MyUser.objects.filter(Q(username__iexact=query)|Q(email__iexact=query)).distinct();
        # if not result.exists() and result.count() !=1:
        #     raise forms.ValidationError("Username or email Not Found");
        # # elif result.first().check_password(password):
        # #     raise forms.ValidationError("In Valid password");
        # fresult=result.first();
        # if not fresult:
        #     raise forms.ValidationError("Invalid Credintionales");
        # if not fresult.check_password(password):
        #     raise forms.ValidationError("Invalid Password");
        # return super(UserLoginForm,self).clean(*args,**kwargs);

        # user=authenticate(username=username,password=password);
        # if not user:
        #     raise form.ValidationError("Invalid Credinales");
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username','first_name','last_name','email');

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('username','first_name','last_name','password', 'is_staff', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
