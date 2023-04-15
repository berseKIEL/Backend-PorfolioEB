from datetime import datetime
from pydantic import validator

def validate_date_not_in_future(cls, v):
    if v > datetime.now():
        raise ValueError('Date cannot be in the future')
    return v