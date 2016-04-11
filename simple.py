#coding:utf-8
'''
Created on 2015年12月17日

@author: 201510260176
'''
from splinter import  Browser
with Browser() as browser:
    #vist url
    url = "http://www.baidu.com"
    browser.visit(url)
    browser.fill('wd', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_value('百度一下')
    # Interact with elements
    button.click()
    if browser.is_text_present('splinter.readthedocs.org'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")
if __name__ == '__main__':
    browser
    pass