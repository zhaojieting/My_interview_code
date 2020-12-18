"""
经纬恒润面试题
easy： 数字母数
"""


def count_word(s):
    word = list()
    num = list()
    index = 0
    cnt = 1
    if s:
        word.append(s[0])
        for i in range(len(s))[1:]:
            if s[i] == word[index]:
                cnt += 1
                if i == len(s)-1 :
                    num.append(cnt)
            else:
                index += 1
                word.append(s[i])
                num.append(cnt)
                cnt = 1
                if i == len(s)-1 :
                    num.append(cnt)
        result =''
        for j in range(len(word)):
            result += word[j] + str(num[j])
        return result
    else:
        return "input error"

if __name__ == "__main__":
    result = count_word("aaaaadddcccccccbba")
    print(result)