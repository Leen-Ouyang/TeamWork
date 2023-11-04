import tkinter as tk

error_codes= {
101 :"未提交文件！",
102: "未输入用户名!",
103: "未输入密码！",
104: "文件格式错误！",
200: "找不到文件",
201: "文件读取错误",
202: "转换出错",
203: "文件生成错误",
301:"JSON文件错误.",
302:"JSON文件不存在.",
303:"不是有效的JSON文件.",
304:"读取文件错误.",
305:"科目和成绩数量不匹配",
}
def get_error_message(error_code):
    return error_codes.get(error_code, "未知错误")

# 错误提示
def show_error_info(errorCode):
    # 创建新的窗口
    new_window = tk.Toplevel()
    new_window.title("错误提示")

    # 在新窗口中显示返回的值
    error_label = tk.Label(new_window, text=get_error_message(errorCode))
    error_label.pack(padx=20, pady=20)

    # 运行新窗口的事件循环
    new_window.mainloop()

def show_error(errorCode):
    show_error_info(errorCode)