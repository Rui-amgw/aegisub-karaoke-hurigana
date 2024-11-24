import re

# 原始歌词文本路径
with open("lyrics.txt", "r", encoding="utf-8") as f:
    lyrics = f.read()

# 常见的小写字符：ぁぃぅぇぉゃゅょっァィゥェォャュョッん
# 小写字符的Unicode编码
all_lower = ["\u3041","\u3043","\u3045","\u3047","\u3049","\u3083","\u3085","\u3087","\u3063","\u30a1","\u30a3","\u30a5","\u30a7","\u30a9","\u30e3","\u30e5","\u30e7","\u30c3","\u3093"]
p = re.compile(r"[(](.*?)[)]")


# 将假名注音按音节分开
def split_hurigana(str):
    allstr = list(str)
    sylbs = []
    for s in allstr:
        if s not in all_lower:
            sylbs.append(s)
        else:
            j = sylbs[-1] + s
            sylbs.pop()
            sylbs.append(j)
    huritext = "#|<".join(sylbs)
    huritext = "|" + huritext
    return huritext


# 主程序
if __name__ == '__main__':
    all_huri = re.findall(p, lyrics)
    no_huri = re.sub(p, "", lyrics)
    holder_huri = re.sub(p, "$", lyrics)
    all_split = [split_hurigana(i) for i in all_huri]
    while len(all_split) != 0:
        holder_huri = holder_huri.replace("$", all_split[0], 1)
        all_split = all_split[1:]

    # 保存aegisub卡拉OK格式的歌词文本
    with open("aeg_hurigana_lyrics.txt", "w", encoding="utf-8") as f:
        f.write(holder_huri)

    # 保存无假名的歌词文本
    with open("no_hurigana_lyrics.txt", "w", encoding="utf-8") as f:
        f.write(no_huri)
