from routers import *

@router.post("/total")
async def search_job():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    blocks = open_json("./assets/blocks/total/search_total.json")
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="직업검색", blocks=blocks)
    return 

async def get_job(query):
    if query == None:
        result = slack_client.post_message(channel_id=CHANNEL_ID, text="아무것도 입력하지 않았습니다.")
        return
    else:
        query = query.replace(" ", "%20")
        texts = f"https://www.jobkorea.co.kr/OnePick/JobList?Keyword={query}"
        blocks = open_json('./assets/blocks/total/get_total.json')
        for i in range(2, len(blocks)):
            blocks[i]["accessory"]['url'] = blocks[i]["accessory"]['url'].replace('QUERY_STRING', query)
        result = slack_client.post_message(channel_id=CHANNEL_ID, text=texts, blocks=blocks)
        return 
