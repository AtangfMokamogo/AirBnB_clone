#!/usr/bin/python3
"the base classs for our airbnb clone"

from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Instantiates the BaseModel class
        Note:
            If a dictionary is provided, dictionary values are used
        Attributes:
            id (str): will be assigned with uuid.uuid4() converted to string
            created_at: will be assigned datetime
            updated_at: assigned with datetime each object is changed
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

            if "id" not in kwargs:
                setattr(self, "id", str(uuid.uuid4()))

            time = datetime.now()

            if "created_at" not in kwargs:
                setattr(self, "created_at", time)

            if "updated_at" not in kwargs:
                setattr(self, "updated_at", time)

        else:
            setattr(self, "id", str(uuid.uuid4()))

            time = datetime.now()
            setattr(self, "created_at", time)
            setattr(self, "updated_at", time)
            models.storage.new(self)

    def __str__(self):
        """
        prints string representation of class.
        Format: [<class name>] (<class id>) <class dict>
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
