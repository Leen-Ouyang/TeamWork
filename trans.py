import pandas as pd
import json
from gui import excelfile,jsonfile
# 读取Excel文件
df = pd.read_excel(excelfile, engine='openpyxl', skiprows=1, usecols="B:I")

# 将数据转换为JSON格式
json_data = df.to_json(orient='records',  force_ascii=False)

# 解析JSON数据
data = json.loads(json_data)

# 创建字典来嵌套数据
nested_data = {}
i=-1
for item in data:
    student_id = item['学号']
    student_name = item['姓名']
    nested_data_str = str(nested_data)
    if str(student_id) not in nested_data_str:
        i=i+1
        nested_data[i] = [student_id, student_name, []]
    nested_data[i][2].append([
        item['课程名称'],
        item['学分'],
        item['百分成绩'],
        item['五分成绩'],
        item['考试类型'],
        item['选修类型']
    ])

# 将嵌套数据转换为JSON格式
nested_json_data = json.dumps(nested_data, ensure_ascii=False)

# 将嵌套JSON数据写入文件
with open(jsonfile, 'w', encoding='utf-8') as f:
    f.write(nested_json_data)