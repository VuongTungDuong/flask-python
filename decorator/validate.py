from flask import request
from pydantic import BaseModel


def validate(data_check: type[BaseModel]):
  def decorator(f):
    def decorator_func(*agrs, **kagrs):
      kagrs["data"] = data_check(**request.json)

      return f(*agrs, **kagrs)

    return decorator_func

  return decorator
