# This is a sample Python script.
from pydoc import text

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    output_data = [] # 最终输出2维数组

    Course_Dict = {}
    driver = webdriver.Chrome()
    driver.get(url = 'https://my.sa.ucsb.edu/gold') #gold登录界面

    # 第一次登录点击操作
    login_click_path ='/html/body/div[2]/form/section/div/main/div/div/div[1]/div/div[3]/ input'
    driver.find_element(By.XPATH, login_click_path).click()

    # 账号密码登录
    user_name_path ='/html/body/main/div/div[1]/div/div/div[2]/form/section[1]/div/input' # 密码x-path
    password_path = '/ html/body/main/div/div[1]/div/div/div[2]/form/section[2]/div/input' # 账号x-path
    login_click_path_2 ='/html/body/main/div/div[1]/div/div/div[2]/form/input[4]' # 登录x-path
    driver.find_element(By.XPATH, user_name_path).send_keys('minxing')  # 选定用户名位置并输入
    my_password = input('password:')
    driver.find_element(By.XPATH, password_path).send_keys(my_password) # 选定密码位置并输入
    driver.find_element(By.XPATH, login_click_path_2).click()

    print('请手动进行duo验证')
    time.sleep(10)

    # 进入find course搜索界面
    find_course_path = '/html/body/div[2]/form/header/div/div[2]/nav/nav/ul/li[2]/a'
    driver.find_element(By.XPATH, find_course_path).click()
    time.sleep(2)

    # 开始循环爬取所有课程
    index = 1
    for i in range(83):  # 遍历所有科目
        box_path = '/html/body/div[2]/form/section/div[2]/main/div/div/div[2]/div[3]/div/div[2]/select'
        # anth_path = '/html/body/div[2]/form/section/div[2]/main/div/div/div[2]/div[3]/div/div[2]/select/option[1]'
        select_ele = Select(driver.find_element(By.XPATH, box_path))
        select_ele.select_by_index(index)
        click_search_path = '/html/body/div[2]/form/section/div[2]/main/div/div/div[3]/div/div/input[2]'
        driver.find_element(By.XPATH, click_search_path).click()
        time.sleep(2)

        # 获取课程信息的相关元素
        course_info_path ='/html/body/div[2]/form/section/div[2]/main/div[2]/div[4]/div[1]'
        course_item = driver.find_element(By.XPATH, course_info_path).text
        course_list = course_item.strip().split('\n')
        output_data.append(course_list)

        # 完成单次爬取，回到find course 界面
        driver.find_element(By.XPATH, find_course_path).click()
        index += 1

    print(output_data)
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # 创建 CSV writer 对象
        csv_writer = csv.writer(csvfile)

        # 写入一行字符串数据
        csv_writer.writerows(output_data)

    print(f'CSV 文件已成功创建：data.csv')











