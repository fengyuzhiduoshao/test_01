from log import log



class TestWeibo:
    def test_case1_01(self, open_weibo):
        print("查看微博热搜")

    def test_case1_02(self, open_weibo):

        try:
            log.info("开始执行")
            print("查看微博范冰冰")
            assert 1==2
        except Exception as e:
            log.error(e)
            log.info("执行完毕")
