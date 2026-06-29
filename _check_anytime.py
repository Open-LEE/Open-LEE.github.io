with open(r'D:\Task\近期工作\my-resmue\index.html','r',encoding='utf-8') as f:
    content = f.read()
# Search for "anytime"
idx = content.find("anytime")
if idx > 0:
    print(repr(content[idx-10:idx+80]))
