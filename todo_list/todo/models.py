from django.db.models import Model, CharField, DateField, BooleanField
# Create your models here.

class task(Model):
    name = CharField(max_length=64)
    date_created = DateField()
    is_done = BooleanField(default=False)


    def __str__(self):
        return self.name


from django.forms import CharField, DateField, BooleanField, Form

class TaskForm(Form):
    name_task = CharField(max_length=64)
    date_created_task = DateField()
