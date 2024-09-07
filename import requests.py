# 获取greenhub秘钥
import requests

headers = {"Authorization": "Basic c2tfdGVzdF81MUxBT0RiS2s0SlNnMUM0MTNZY1FNUFlKckMwallBVmRDZFhYaUF3bDJPZ3FnZVR1dkdCZ2VyUjg4MlBKMFRBNHZqbjk0UlFiWVB1dmRhdDhUNHBHUkxkVTAwNURKYndxS3QK"}
result = requests.get("https://api.stripe.com/v1/customers", headers=headers).json()

license_code = [customer['metadata']['license_code'] for customer in result['data']]
print(license_code)