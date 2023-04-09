from pydantic import BaseSettings, Field


class Conf(BaseSettings):
    test: str = Field(..., env='teststr')
    test_two: str = Field('zxc', env='teststr_two')
