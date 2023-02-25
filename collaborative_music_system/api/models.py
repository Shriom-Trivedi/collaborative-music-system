from django.db import models
import string
import random

# Generate unique code for rooms.
def generate_unique_code() -> string:
    length: int = 6

    while True:
        # Below code generates random code which will contain uppercase ascii characters only.
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        # Compare code with all the codes present in Room to check whether it is unique or not.
        if Room.objects.filter(code=code).count() == 0:
            break

    return code


# Create your models here.
# In django you should have thin views and fat models.
# Put most of your logic in models.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    # One host for one room. One host cannot have multiple rooms at a time.
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
