import json
from GlobalSetting import jsonfile
from error import show_error

def load_data(jsonfile):
    try:
        # 从本地文件读取 JSON 数据
        with open(jsonfile, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        show_error(303)  # 处理文件不存在错误
        return None
    except json.JSONDecodeError:
        show_error(300)  # 处理JSON解析错误
        return None

number_of_students = 3

def generate_report(student_id):
    global number_of_students
    try:
        # 获取指定学号的学生成绩信息
        data = load_data(jsonfile)
        number_of_students = len(data)
        student_info = data.get(str(student_id))

        if not student_info:
            return show_error(301)  # 处理学号不存在错误

        student_name = student_info[1]
        courses = student_info[2]

        # 创建学生成绩通知的文本
        student_report = f"亲爱的{student_name}同学:\n\n"
        student_report += "祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。\n\n"

        # 循环遍历课程信息
        for course in courses:
            course_name = course[0]
            percent_grade = course[2]
            student_report += f"{course_name}: {percent_grade}\n"

        student_report += "\n"
        student_report += "希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。"
        student_report += "如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。"
        student_report += "我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。"
        student_report += "请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。\n\n"
        student_report += "再次恭喜您，祝您学习进步、事业成功！\n\n"
        student_report += "教务处"

        return student_report
    except KeyError:
        show_error(302)  # 处理学号无效错误
        return None
