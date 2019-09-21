from selenium import  webdriver

options=webdriver.ChromeOptions()#实例化opthons
options.add_argument("--proxy-server=http://代理ip：端口")#添加代理

driver_path=r"D:\chromedriver\chromedriver.exe"# 浏览器路径
driver=webdriver.Chrome(driver_path,chrome_options=options)#实例化时加入代理

driver.get("https://www.baidu.com/")#打开网页