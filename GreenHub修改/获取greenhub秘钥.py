# 获取greenhub秘钥
import requests

headers = {"Authorization": "Basic c2tfdGVzdF81MUxBT0RiS2s0SlNnMUM0MTNZY1FNUFlKckMwallBVmRDZFhYaUF3bDJPZ3FnZVR1dkdCZ2VyUjg4MlBKMFRBNHZqbjk0UlFiWVB1dmRhdDhUNHBHUkxkVTAwNURKYndxS3QK"}
result = requests.get("https://api.stripe.com/v1/customers", headers=headers).json()

license_code = [customer['metadata']['license_code'] for customer in result['data']]
print(license_code)

#获取前置：https://xn--vfv958a.com/2024/04/05/%E8%87%AA%E5%8A%A8%E8%8E%B7%E5%8F%96Greenhub%E6%BF%80%E6%B4%BB%E7%A0%81%EF%BC%9A%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90%E4%B8%8E%E8%84%9A%E6%9C%AC%E7%BC%96%E5%86%99/



#首先找到Greenhub根目录，只要在Greenhub的快捷方式上右键点击打开文件所在位置即可
# 然后找到resources文件夹，可以找到app.asar。我们从这里 下载7-zip插件，将下载后得到的压缩包解压，会有两个dll插件，一个32位，
# 一个64位，根据7-zip的位数自己选择，选好后粘贴到7-zip根目录的Formats文件夹中，如果不知道自己的7-zip是几位，就全部粘贴，
# 根目录没有Formats文件夹就创建一个。装好插件，我们直接右键app.asar，点击显示更多选项（Windows 10可以忽略这一步），找到7-zip，
# 点提取到”app\“，此时可能会报个错：Codec Load Error: …，无视它，点确定即可。解压后源码就在app\dist\electron中，
# 将其中的一大坨代码格式化一下，得到人能看的源码。

# 于是在renderer.js中通过搜索字符串寻找STRIPE_GET_ACTIVE_CODE ，
# var n = "dev" === process.env.APP_BUILD_TYPE ? "sk_test_此处为省略的秘钥" : "rk_live_此处为省略的秘钥";


# 因此，表达式 var n = “dev” === process.env.APP_BUILD_TYPE ? “sk_test_…” : “rk_live_…”; 是检测greenhub是否为dev版，
# 如果是，则使用字符串 sk_test_… ；如果不是，则使用 rk_live_… 。而我们所使用的版本大概率不是dev版，所以字符串应该是以 rk_live 开头的。

#直接将”sk_test_此处为省略的秘钥“或”rk_live_此处为省略的秘钥“进行base64解码，得到秘钥。
#将密钥粘贴到第4行authorization变量中，运行代码，得到秘钥。
