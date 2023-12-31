# update_html.py

input_file_path = 'path/to/your/input/file.txt'
output_html_path = 'path/to/your/output/index.html'
special_marker = '<!-- Custom Marker -->'

with open(input_file_path, 'r') as input_file:
    file_content = input_file.read()

# 读取 HTML 文件内容
with open(output_html_path, 'r') as html_file:
    html_content = html_file.read()

# 查找特殊标记
marker_index = html_content.find(special_marker)

# 如果找到了特殊标记，则在特殊标记后面添加文件内容
if marker_index != -1:
    updated_html_content = (
        html_content[:marker_index + len(special_marker)] +
        f'\n<div>{file_content}</div>\n' +
        html_content[marker_index + len(special_marker):]
    )
else:
    # 如果没有找到特殊标记，则在文件末尾添加文件内容
    updated_html_content = html_content + f'\n<div>{file_content}</div>\n'

# 写入更新后的 HTML 内容
with open(output_html_path, 'w') as updated_html_file:
    updated_html_file.write(updated_html_content)