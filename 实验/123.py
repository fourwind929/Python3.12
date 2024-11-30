import re

# Windows 路径正则表达式
windows_pattern = r'^[A-Za-z]:\$[^\\:*?"<>|]+\$*[^\\:*?"<>|]*$'

# Unix/Linux 路径正则表达式
unix_pattern = r'^(/[^/]+)+/?$'

# 测试字符串
test_strings = [
    "C:\\Users\\Username\\Documents\\file.txt",
    "D:\\path\\to\\file",
    "C:\\path\\to\\file:",
    "/home/username/documents/file.txt",
    "/path/to/file",
    "/path/to/file/"
]

for s in test_strings:
    if re.match(windows_pattern, s) or re.match(unix_pattern, s):
        print(f"'{s}' 匹配")
    else:
        print(f"'{s}' 不匹配")
