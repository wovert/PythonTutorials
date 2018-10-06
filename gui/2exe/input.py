import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

id = '13039334619'
pw = 'Am2r1c@nfb'

account = {id:'', pw:''}
url = 'https://www.facebook.com/'
search_url = 'https://www.facebook.com/?sk=ff'

def get_account(account):
    # 选择浏览器
    browser = webdriver.Chrome()
    browser.implicitly_wait(100)

    # browser.implicitly_wait(10)
    # browser.set_window_size(0,0)
    # 访问facebook网页
    browser.get('https://www.facebook.com/')
    # 输入账户密码
    browser.find_element_by_id('email').clear()
    browser.find_element_by_id('email').send_keys(account.id)
    browser.find_element_by_id('pass').clear()
    browser.find_element_by_id('pass').send_keys(account.pw)
    # 模拟点击登录按钮，两种不同的点击方法。。。

    try:
        browser.find_element_by_xpath('//input[@type="submit"]').send_keys(Keys.ENTER)
    except:
        browser.find_element_by_xpath('//button[@name="login"]').send_keys(Keys.ENTER)

    # time.sleep(10)
    browser.find_element_by_xpath('//a[@href="https://www.facebook.com/?ref=logo"]').send_keys(Keys.ENTER)

    # browser.file_detector_context('Facebook').send_keys(Keys.ENTER)
    # 获取cookie
    # cookies = browser.get_cookies()

    browser.get(search_url)

    itemAll = browser.find_elements_by_class_name('FriendRequestAdd')
    for x in range(len(itemAll)):
        item = itemAll[x]
        browser.execute_script('return arguments[0].click()', item)
        time.sleep(5)

    browser.close()

def loginCommandClicked():
    emailVal = email.get()
    passwordVal = password.get()
    print(emailVal)
    print(passwordVal)

    if emailVal and passwordVal:
        account = {id:emailVal,pw:passwordVal}
        get_account(account)



top = tk.Tk()

#设置窗口的大小宽x高+偏移量
top.geometry('500x300+500+200')

top.title("자동화[facebook]친구추가")
labelHello = tk.Label(top, text="facebook 친구추가", height=5, width=20, fg="blue")
labelHello.pack()

email = tk.Entry(top)
email.pack()

password = tk.Entry(top, show="*")
password.pack()

loginBtn = tk.Button(top, text="로그인", command=loginCommandClicked)
loginBtn.pack()

top.mainloop()