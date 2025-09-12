from pydantic import BaseModel, Field

from tools.fakers import fakers


class CreateUserSchema(BaseModel):
    name: str = Field(default_factory=fakers.fake_name)
    email: str = Field(default_factory=fakers.fake_email)
    password: str = Field(default_factory=fakers.fake_password)


class LoginUserSchema(BaseModel):
    email: str
    password: str


class UpdateUserSchema(BaseModel):
    name: str = Field(default_factory=fakers.fake_name)
    phone: str = Field(default_factory=fakers.fake_phone)
    company: str = Field(default_factory=fakers.fake_company)


class DataUserSchema(BaseModel):
    id: str
    name: str
    email: str
    token: str = None
    phone: str = None
    company: str = None


class UserSchema(BaseModel):
    status: int
    success: bool
    message: str
    data: DataUserSchema
