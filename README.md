# django
Project: 
core, which is created via ```django-admin.py startproject core .```
Apps:
**bold accounts**
    This app provide authentication, authorization and accounting.
    ``` python manage.py startapp accounts```

## User Model
There are two ways to extend the default User model without substituting your own model. If the changes you need are purely behavioral, and don’t require any change to what is stored in the database, you can create a proxy model based on User. This allows for any of the features offered by proxy models including default ordering, custom managers, or custom model methods.

If you wish to store information related to User, you can use a OneToOneField to a model containing the fields for additional information. This one-to-one model is often called a profile model, as it might store non-auth related information about a site user. For example you might create an Employee model

### Custom User Model / Substituting

The default User model in Django uses a username to uniquely identify a user during authentication. If you'd rather use an email address or phone number etc, you will need to create a custom User model by either subclassing AbstractUser or AbstractBaseUser.

Options:

* AbstractUser: Use this option if you are happy with the existing fields on the User model and just want to remove the username field.
* AbstractBaseUser: Use this option if you want to start from scratch by creating your own, completely new User model.

Creating our initial custom user model requires four steps:

* update settings.py
* create a new CustomUser model
* create new UserCreation and UserChangeForm
* update the admin

#### AbstractUser

accounts/models.py
```
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

accounts/admin.py
```from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```
core/settings.py
add the following line

```
AUTH_USER_MODEL = 'accounts.User'
```
and add 'accounts' to 'INSTALLED_APPS' list
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
]
```
### Profile model

### Referencing the User model¶
If you reference User directly (for example, by referring to it in a foreign key), your code will not work in projects where the AUTH_USER_MODEL setting has been changed to a different user model.

get_user_model()
Instead of referring to User directly, you should reference the user model using django.contrib.auth.get_user_model(). This method will return the currently active user model – the custom user model if one is specified, or User otherwise.

When you define a foreign key or many-to-many relations to the user model, you should specify the custom model using the AUTH_USER_MODEL setting.