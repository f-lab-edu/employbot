from routers import *

@router.post('/form')
async def search_detail_job():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)

    blocks = [

    ]