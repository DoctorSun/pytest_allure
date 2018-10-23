# coding:utf-8

import pytest
import allure
import time
from selenium import webdriver


class Test():

    paras = {'测试环境': '小峰峰本地机器'}
    # 报告中的环境参数，可用于必要环境参数的说明，相同的参数以后者为准
    allure.environment(host="172.0.0.1", test_vars=paras)

    @allure.severity("blocker")
    @allure.issue("http://www.panda.tv")
    @allure.testcase("测试用例：test1")
    @allure.feature("小峰峰测试功能")
    @allure.story("小峰峰功能1")
    # @pytest.mark.parametrize("x", ["this"], ids=["学习1"])
    @allure.step("运算:x+y")
    def test_1(self):
        """测试用例1"""
        x = 2
        y = 4
        paras = vars()
        allure.attach("用例参数", "{0}".format(paras))
        allure.attach("返回结果", "{0}".format(6))
        assert 6 == x + y, 6

    @allure.severity("blocker")
    @allure.issue("http://www.panda.tv")
    @allure.testcase("测试用例：test2")
    @allure.feature("小峰峰测试功能")
    @allure.story("小峰峰功能2")
    def test_2(self):
        """打开pandatv首页"""
        driver = webdriver.Firefox()
        driver.get('https://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('hello')
        driver.find_element_by_id('su').click()
        time.sleep(5)
        driver.save_screenshot("./report/b.png")
        f = open('./report/b.png', 'rb').read()
        allure.attach('this is a img', f, allure.attach_type.PNG)

        driver.quit()


if __name__ == '__main__':

    pytest.main()
