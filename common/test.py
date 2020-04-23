#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/101718qiong/")

title = EC.title_is(u"Silence&QH - 博客园")
print(title)


print(title(driver))

















