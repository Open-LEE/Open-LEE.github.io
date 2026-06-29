with open(r'D:\Task\近期工作\my-resmue\index.html','r',encoding='utf-8') as f:
    content = f.read()

# Show section structures
import re
sections = re.findall(r'<section[^>]*>.*?</section>', content, re.DOTALL)
for i, s in enumerate(sections):
    # Get id
    id_match = re.search(r'id="(\w+)"', s)
    label_match = re.search(r'<span class="label">(.*?)</span>', s)
    section_id = id_match.group(1) if id_match else "?"
    label = label_match.group(1) if label_match else "?"
    length = len(s)
    first_200 = s[:200].replace('\n', ' ').replace('  ', '')
    print(f"Section {i}: id={section_id}, label={repr(label)}, len={length}")
    print(f"  Starts: {s[:100]}")
    print()
