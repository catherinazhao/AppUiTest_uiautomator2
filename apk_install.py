import uiautomator2 as u2

d = u2.connect()
print(d.device_info)

# url = "http://p.gdown.baidu.com/ebbdc794b5444ce378ce6e74b6da8f226f499216ca419efdb70236fac2e1f617a2731ed0aca0a8664aed0958d2a95ffdc2c33f9e24321d09235999787bac7185c1250aa4f4faf971651534a6ec18b1b8eaa6f4dd18df7dfa583cc46dda77ce461999bc2fbdc03da09624cf28858bc922c6fe5b3b4d8c1ad2e3c690602aa1b6d0416b5755ee1d44af97964328fc37ee12161c93663a76fb63ab56799819e8ed1ab8420f96f1a4d67c"
# d.app_install(url)