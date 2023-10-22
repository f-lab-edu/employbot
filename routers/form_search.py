from routers import *


@router.post('/form')
async def search_jobform():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    blocks = open_json("./assets/blocks/forms/search_job_form.json")
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return 

async def search_form(path):
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    blocks = open_json(path)
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return 

async def get_form(forms, path):
    # 옵션에 대한 설정
	## 옵션이 하나만 있을 때
    if len(forms['Filter']) == 1:
        filters = ''.join(forms['Filter'])
    ## 옵션이 존재하지 않을 때
    elif len(forms['Filter']) == 0:
        filters = ''
    ## 옵션이 2개 이상일 때
    else:
        filters = '%2C'.join(forms['Filter'])
    filters  ='%'.join(forms['Filter'])
    
    keyword = forms['keyword'].replace(" ","%20")
    edulevel = forms['EduLevel'].replace("0","")
    careerType = forms['CareerType'].replace("0","")
    text = f"https://www.jobkorea.co.kr/OnePick/JobList?Keyword={keyword}&Ord=GcmCodeAmtDesc&DutyCtgr={forms['DutyCtgr']}&Local={forms['Local']}&CareerType={careerType}&EduLevel={edulevel}&Filter={filters}"
    
    blocks = open_json(path)
    blocks[2]["accessory"]['url'] = text
    
    result = slack_client.post_message(channel_id=CHANNEL_ID,text = text, blocks=blocks)
    return 