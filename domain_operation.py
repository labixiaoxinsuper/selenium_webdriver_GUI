#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class Testconsole():

    def __init__(self, chrome_dir, username, passwd, i, domain_name, domain_number, service_type):
        self.chrome_dir = chrome_dir
        self.username = username
        self.passwd = passwd
        self.i = i
        self.domain_name = domain_name
        self.domain_number = domain_number
        self.service_type = service_type

    def initial_conditions(self):
        global driver
        driver = webdriver.Chrome(self.chrome_dir)
        # http://chromedriver.storage.googleapis.com/index.html
        driver.get("http://xxxxxxx")
        # 登录
        login_username = driver.find_element_by_css_selector('#app > div > div > div > div.r > div > div.form > form > div:nth-child(1) > div:nth-child(1) > input')
        #login_username = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/div[2]/form/div[1]/div[1]/input')
        login_username.clear()
        login_username.send_keys(self.username)
        login_passwd = driver.find_element_by_css_selector('input[placeholder="请输入您的密码"]')
        login_passwd.clear()
        login_passwd.send_keys(self.passwd)
        driver.find_element_by_css_selector("[type='button']").click()
        time.sleep(5)

    def end_conditions(self):
        driver.find_element_by_xpath('//*[@id="menu"]/div/div[4]/a[1]/span[1]').click()
        logout = driver.find_element_by_xpath('//*[@id="menu"]/div/div[4]/ul/li[6]/a/span[2]')
        logout.click()
        driver.quit()

    def add_domain(self):
        j = int(self.i)
        for j in range(j):
            time.sleep(1)
            # 点击“概览”
            summary_cl = driver.find_element_by_xpath('//*[@id="sidebar"]/div/div[2]/a')
            summary_cl.click()
            time.sleep(3)

            # 点击“添加域名”
            domain_add = driver.find_element_by_xpath('//*[@id="topbtn"]/a[1]/button')
            domain_add.click()

            # 添加的域名信息
            # 添加加速域名
            domain_add_name = driver.find_element_by_xpath('// *[@id="domainsAdd"]/form/div[1]/div/div/input')
            n = str(j)
            domain_first_para = domain_name.split(i)[0]
            domain_second_para = domain_name.split(i)[1]
            domain_add_name.send_keys(domain_first_para + n + domain_second_para)
            # domain_add_name.send_keys(self.domain_name)

            # 添加备案号
            domain_add_number = driver.find_element_by_xpath('//*[@id="domainsAdd"]/form/div[2]/div/div[1]/input')
            domain_add_number.send_keys(self.domain_number)

            domain_add_type = driver.find_element_by_xpath('//*[@id="domainsAdd"]/form/div[3]/div/div/div/input')
            domain_add_type.click()
            time.sleep(1)

            # 选择业务类型
            global domain_add_type_choose
            if self.service_type == "直播加速":
                domain_add_type_choose = domain_add_type.find_element_by_xpath('/html/body/div[' + str(j+2) + ']/div[1]/div[1]/ul/li[1]')  # 直播加速
                domain_add_type_choose.click()
            elif self.service_type == "点播加速":
                domain_add_type_choose = domain_add_type.find_element_by_xpath('/html/body/div[' + str(j+2) + ']/div[1]/div[1]/ul/li[2]') # 点播加速
                domain_add_type_choose.click()

            # 点击“确认提交”
            submit_cl = driver.find_element_by_xpath('//*[@id="domainsAdd"]/form/div[4]/div/button[2]/span')
            submit_cl.click()
            time.sleep(1)
            # 点击“核对无误，确认提交”
            submit_verify = driver.find_element_by_css_selector('#domainsAdd_checkDialog > div > div.el-dialog__footer > div > button.el-button.el-button--success > span')
            submit_verify.click()
            time.sleep(3)

            # 判断
            try:
                # 根据是否有“确定”弹出按钮来click，来断定域名是否存在。
                driver.find_element_by_xpath('/ html / body / div[3] / div / div[3] / button').click()
                # 没有“确定”弹出按钮，就可以
            except NoSuchElementException:
                print "新建域名" + domain_first_para + n + domain_second_para + "成功"

            else:
                print "域名" + domain_first_para + n + domain_second_para + "已存在"
                time.sleep(1)
                # 因为域名存在，所以点击“返回”按钮。
                driver.find_element_by_xpath('//*[@id="domainsAdd_checkDialog"]/div/div[3]/div/button[1]/span').click()
                time.sleep(2)
                continue

    def delete_domain(self):
        # 点击“域名管理”,此处注意一定要在点击“概览”之后执行这一步。直接执行这一步会报错。
        domain_manger = driver.find_element_by_xpath('// *[ @ id = "sidebar"] / div / div[3] / a')
        domain_manger.click()
        time.sleep(3)

        j = int(self.i)
        for j in range(j):
            # 删除
            domain_delete = driver.find_element_by_xpath('//*[@id="domainsList"]/div[2]/div[1]/div[3]/table/tbody/tr[4]/td[6]/div/button/span')
            domain_delete.click()
            time.sleep(5)
            domain_delete_verify = driver.find_element_by_xpath('/ html / body / div[2] / div / div[3] / button[2] / span')
            domain_delete_verify.click()
            print "删除域名"




if __name__ == "__main__":
    chrome_dir = "D:\software\chromedriver.exe"
    username = "17709816196@163.com"
    passwd = "xxxxxxx"
    i = "2"                                  # 代表想要新建的域名的个数
    domain_name = "teste" + i + ".cn"       # 可以更改test和.cn这两个字符串
    domain_number = u"xxxxxx"   # 将nicode转换成普通的Python字符串:"编码(encode)".u“xxx”是属于unicode类型.
    service_type = "点播加速"
    run = Testconsole(chrome_dir, username, passwd, i, domain_name, domain_number,service_type)
    run.initial_conditions()
    run.add_domain()
    run.delete_domain()
    run.end_conditions()

