# pytest_allure
window10 Jenkins+pytest(包含selenium webdriver)+allure
一.下载jenkins
下载地址：http://Jenkins-ci.org/

二.安装
根据提示安装即可
三.登录
http://localhost:8080/




四.安装插件
左边默认即可



注：会遇到离线模式，无法运行webdriver
解决方法：

1. 打开-服务-jenkins-右键停止服务&启动类型选择（禁用）
2. 任意路径-新建jenkins_start.bat文件，内容如下：
    echo "Jenkins CI automation testting"
    java -jar "****jenkins安装路径下（本地安装路径）****\jenkins.war"
    pause
    
3. 运行bat文件
    此时可能遇到jenkins离线运行情况（无法自行安装插件），此问题为证书问题
    浏览器打开http://localhost:8080/pluginManager/advanced
    将升级站点中的https://...更换为http
4. 重新运行bat文件即可正常注册，更新插件

五.注册账户


  
六.Jenkins中安装Allure Jenkins Plugin
    系统管理-管理插件-可选插件-过滤Allure Jenkins Plugin（安装后重启）
七.Jenkins中配置Allure Commandline
    系统管理-全局工具管理-Allure Commandline
    两种方式：
    1. 本地安装（下载allure执行工具:https://github.com/allure-framework/allure1/releases/tag/allure-core-1.4.23并添加至环境变量）
    2.自动安装
八.Jenkins执行测试用例Job配

九.构建生成报告


