import re
with open(r'D:\Task\近期工作\my-resmue\index.html','r',encoding='utf-8') as f:
    content = f.read()
idx = content.find('id="about"')
if idx > 0:
    print(repr(content[idx:idx+1200]))
