from pydantic import BaseModel

class LoginModel(BaseModel):
    username: str
    password: str


class SignupModel(BaseModel):
    username: str
    password: str


class ForgotPassModel(BaseModel):
    username: str
    password: str
