def check_brackets(input_string):
    """
    检查括号匹配情况，并返回对应的输出字符串。

    Parameters:
    input_string (str): 输入的字符串，包含括号和其他字符。

    Returns:
    str: 表示括号匹配情况的输出字符串。其中，空格表示匹配成功的括号，"?"表示没有匹配的右括号，
         "x"表示没有匹配的左括号。
    """
    # 初始化栈和输出字符串
    stack = []
    output = ""

    # 遍历输入字符串中的每个字符
    for char in input_string:
        if char == '(':
            # 如果是左括号，则将其位置及可能的输出位置加入栈中，并在输出字符串中添加空格
            stack.append((char, len(output)))
            output += " "
        elif char == ')':
            if stack:
                # 如果是右括号且栈不为空，则匹配成功，将对应的左括号出栈，并在输出字符串中添加空格
                stack.pop()
                output += " "
            else:
                # 如果是右括号且栈为空，则表示没有匹配的左括号，将在输出字符串中添加问号
                output += "?"
        else:
            # 对于除括号外的其他字符，在输出字符串中添加空格
            output += " "

    # 处理栈中剩余的左括号，将在输出字符串中对应位置添加"x"
    while stack:
        _, index = stack.pop()
        output = output[:index] + "x" + output[index + 1:]

    return output


if __name__ == '__main__':
    
    # 测试用例
    test_cases = [
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()"
    ]
    # 对每个测试用例进行检查并输出结果
    for test_case in test_cases:
        print(test_case)
        print(check_brackets(test_case))

    '''输出结果
    bge)))))))))
    ?????????
    ((IIII))))))
            ????
    ()()()()(uuu
            x   
    ))))UUUU((()
    ????    xx    
    '''