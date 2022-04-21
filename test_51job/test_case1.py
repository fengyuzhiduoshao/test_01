import allure,pytest


data = [{
    "name":"小王",
    "age":15
},
    {
        "name":"小红",
        "age":19
    }]

@allure.description("""这是51job中的allure的描述信息""")
def test_2_01(open_51):
    print("51job，列出所有职位用例")


@allure.link(url="www.baidu.com", name="百度搜索")
@allure.title("""allure的title：{dict}""")
@pytest.mark.parametrize("dict",data)
def test_case2_02(open_51,dict):
    print("51job，找出所有python岗位")
    print(f"参数化的数据：name：{dict['name']},age:{dict['age']}")
