twentytab-tcked
===============

A django application that use cked as texteditor. It update RichTextField with config parameter

## Installation

Use the following command: <b><i>pip install twentytab-tcked</i></b>


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
