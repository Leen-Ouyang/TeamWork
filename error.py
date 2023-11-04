error_codes= {
101 :"未提交文件！",
102: "未输入用户名!",
103: "未输入密码！",
104: "文件格式错误！",
301:"JSON文件错误.",
302:"JSON文件不存在.",
303:"不是有效的JSON文件.",
304:"读取文件错误.",
305:"科目和成绩数量不匹配",
}
def get_error_message(error_code):
    return error_codes.get(error_code, "未知错误")
print(get_error_message())