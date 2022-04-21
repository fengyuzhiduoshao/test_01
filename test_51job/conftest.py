import pytest


@pytest.fixture(scope="module")
def open_51(login):
    name, token = login
    print(f"\n###用户 {name} 打开51job网站###")

