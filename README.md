twentytab-tcked
===============

A django application that use cked as texteditor. It update RichTextField with config parameter

## Installation

Use the following command: <b><i>pip install twentytab-tcked</i></b>

and

<b><i>pip install -e hg+https://bitbucket.org/ssbb/django-cked#egg=django-cked</i></b>

For more informations about django-cked follow this link: https://bitbucket.org/ssbb/django-cked/overview


## Configuration

- settings.py

```py
INSTALLED_APPS = {
    ...,
    'cked',
    'tcked',
    ...
}
```

- urls.py

```py
urlpatterns = patterns('',
    ... ,
     url(r'^cked/', include('cked.urls')),
    ...
)

```

- Static files

Run collectstatic command or map static directory. If you use uWSGI you can map static files:

```ini
static-map = /static/cked/=%(path_to_site_packages)/cked/static/cked
```


## Usage

```py
from django.db import models
from tcked.fields import RichTextField

EASY_CKE = {
    'height': 200,
    'width':400,
    'forcePasteAsPlainText': True,
    'toolbar': [['Bold', 'Italic', 'Underline', '-',
                 'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                 'JustifyBlock', '-', 'Link', 'Unlink', '-', 'Source']],
}
class Entry(models.Model):
    text = RichTextField(config=EASY_CKE)

```
