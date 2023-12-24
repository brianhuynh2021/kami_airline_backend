# utils.py (You can create a new file or put this in an existing one like models.py)

from .models import Airplane

def airplane_exists(airplane_id):
    """
    Check if an airplane with the given ID already exists in the database.

    :param airplane_id: The ID of the airplane to check.
    :return: True if an airplane with the given ID exists, False otherwise.
    """
    return Airplane.objects.filter(id=airplane_id).exists()
