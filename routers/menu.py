from routers import *
from routers.form_search import search_detail_job
from routers.total_search import search_job, get_job

@router.post("/interactive")
async def post_interactive(request: Request):
    form_data = await request.form()
    payload = json.loads(form_data.get("payload"))
    query=payload["actions"][0]
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    
    if query:
        if query['type'] == "plain_text_input":
            await get_job(query['value'])
            return
        if query['type'] == "button":
            if query['value'] == "total":
                await search_job() 
                return
            if query['value'] == "detail":
                await search_detail_job() 
                return
    return