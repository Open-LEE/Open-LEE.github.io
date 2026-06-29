with open(r'D:\Task\近期工作\my-resmue\index.html','rb') as f:
    data = f.read()
idx = data.find(b'anytime')
if idx > 0:
    print(repr(data[idx:idx+40]))
