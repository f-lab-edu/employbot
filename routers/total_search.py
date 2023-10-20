from routers import *

@router.post("/total")
async def search_job():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    with open("./assets/blocks/total/search_total.json", "r") as f:
        blocks = json.load(f)
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="직업검색", blocks=blocks)
    return 



async def get_job(query):
    if query == None:
        result = slack_client.post_message(channel_id=CHANNEL_ID, text="아무것도 입력하지 않았습니다.")
        return
    else:
        query = query.replace(" ", "%20")
        texts = f"https://www.jobkorea.co.kr/OnePick/JobList?Keyword={query}"
        with open("./assets/blocks/total/get_total.json", "r") as f:
            blocks = json.loads(f.read())
            for i in range(2, len(blocks)):
                blocks[i]["accessory"]['url'] = blocks[i]["accessory"]['url'].replace('QUERY_STRING', query)
        result = slack_client.post_message(channel_id=CHANNEL_ID, text=texts, blocks=blocks)
        return 
