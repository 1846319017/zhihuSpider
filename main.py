import time
import requests
import json

# 敏感信息
headers = {}

# 获取api地址
def Api():
    api = 'https://www.zhihu.com/api/v4/questions/265490367/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=5&offset='    
    for num in range(5, 600, 5):
        yield api+str(num)

# 转换json中的时间格式
def Time(updated_time):
    local = time.localtime(int(updated_time))
    #转换成新的时间格式(2016-05-05 20:28:54)
    return time.strftime("%Y-%m-%d %H:%M:%S", local)


if __name__ == '__main2__':
    # 存放爬取结果的表格
    newfile = open('ans.xls', 'w')
    # 先写上表头
    newfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % ('作者', '时间', "包含‘易烊千玺’", '包含‘yyqx’', '点赞' ,'评论', '时间戳', '内容'))
    # 已经获取的回答数量
    nnn = 0
    # “易烊千玺”出现次数
    howmany_yiyangqianxi1 = 0
    # “yyqx”出现次数
    howmany_yiyangqianxi2 = 0
    # 开始爬取每个api
    for api in Api():
        res = requests.get(api, headers=headers)
        thejson = json.loads(res.text)

        is_end = thejson.get('paging').get('is_end')
        if is_end:
            break
        else:
            is_end = thejson.get('paging').get('is_end')
            # 解析json内容
            ans5 = thejson.get('data')
            for eachans in ans5:
                content = eachans.get('content')
                authorname = eachans.get('author').get('name')
                voteup_count = eachans.get('voteup_count')
                comment_count = eachans.get('comment_count')
                updated_time = eachans.get('updated_time')
                thetime = Time(updated_time)
                if "易烊千玺" in content:
                    howmany_yiyangqianxi1 += 1
                if 'yyqx' in content or 'YYQX' in content:
                    howmany_yiyangqianxi2 += 1
                nnn += 1
                print("已经爬取", nnn)
                # 写入表格数据
                newfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (authorname, thetime, "易烊千玺" in content, 'yyqx' in content, voteup_count, comment_count, updated_time, content[:20]))
    newfile.close()
