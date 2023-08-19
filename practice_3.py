from pydantic import BaseModel, Field, ValidationError, field_validator
from pprint import pprint
from typing_extensions import Annotated


Contact = Annotated[str, Field(min_length=3, max_length=30)]


class Letter(BaseModel):
    sender: Contact
    recipient: Contact
    index: str = Field(min_length=6, max_length=6)


try:
    letter = Letter(sender=6, recipient='Ci', index='64')
except ValidationError as e:
    pprint(e.errors())
    print(e.error_count())
