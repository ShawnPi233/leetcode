def min_subseq(source, target):
    '''
    生成target的最小子序列数量
    params: source: str, target: str
    return: int
    '''
    # 初始化指针和结果
    source_ptr = 0
    target_ptr = 0
    result = 0
    match_list = []
    
    while target_ptr < len(target):
        if target[target_ptr] not in source: # 如果target中有source中没有的字符，直接返回-1
            return -1
        if source_ptr >= len(source): # 如果source_ptr超出source的长度，重置source_ptr并增加结果
            source_ptr = 0
            result += 1
            continue
        if target[target_ptr] == source[source_ptr]: # 如果source和target的字符相等，将字符加入匹配列表
            match_list.append(target[target_ptr])
            target_ptr += 1
            source_ptr += 1
            if source_ptr == len(source): 
                # 如果source_ptr到达source的末尾或者target的下一个字符不等于source的下一个字符，重置source_ptr并增加结果
                result += 1
                source_ptr = 0 
            continue
        else:
            source_ptr += 1
            
    match_seq = "".join(match_list)
    if match_seq == target:
        return result
    else:
        return -1


if __name__ == '__main__':
    # 测试样例
    print(min_subseq("abc", "abcbc")) # Output: 2
    print(min_subseq("abc", "acdbc")) # Output: -1
    print(min_subseq("xyz", "xzyxz")) # Output: 3
    print(min_subseq("xxyzz", "xxxyzz")) # Output: 2
    print(min_subseq("xxyzz", "xxayzz")) # Output: -1



 










