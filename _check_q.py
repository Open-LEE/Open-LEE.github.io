with open(r'D:\Task\近期工作\my-resmue\index.html','r',encoding='utf-8') as f:
    content = f.read()
# Find all ? occurrences
import re
for m in re.finditer(r'[?]', content):
    start = max(0, m.start()-60)
    end = min(len(content), m.end()+60)
    context = content[start:end]
    print(f"Position {m.start()}: ...{repr(context)}...")
