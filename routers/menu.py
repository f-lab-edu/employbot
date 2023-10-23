from routers import *
from routers.form_search import *
from routers.total_search import search_job, get_job


@router.post("/interactive")
async def post_interactive(request: Request):
    form_data = await request.form()
    payload = json.loads(form_data.get("payload"))
    query=payload["actions"][0]
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    print(query)
    if query:
        if query['action_id'] == "total_search":
            await get_job(query['value'])
            return
        
        if query['type'] == "button":
            if query['value'] == "total":
                await search_job() 
                return
            if query['value'] == "detail":
                await search_jobform() 
                return
    
    # forms = {'job':'', 'location':'', 'career':'', 'edulevel':'', 'option':'', 'text':''}
    if query['action_id'].split('_')[0] == 'form':
        if query['action_id'].split('_')[1] == '1':
            global forms
            forms = dict()
            forms['DutyCtgr'] = query['selected_option']['value']
            path = f"{route}/assets/blocks/forms/search_location_form.json"
            await search_form(path)
            return
        if query['action_id'].split('_')[1] == '2':
            forms['Local'] = query['selected_option']['value']
            path = f"{route}/assets/blocks/forms/search_career_form.json"
            await search_form(path)
            return
        if query['action_id'].split('_')[1] == '3':
            forms['CareerType'] = query['selected_option']['value']
            path = f"{route}/assets/blocks/forms/search_edulevel_form.json"
            await search_form(path)
            return
        if query['action_id'].split('_')[1] == '4':
            forms['EduLevel'] = query['selected_option']['value']
            path = f"{route}/assets/blocks/forms/search_filter_form.json"
            await search_form(path)
            return
        if query['action_id'].split('_')[1] == '5':
            forms['Filter'] = []
            for option in query['selected_options']:
                    forms['Filter'].append(option['value'])
            path = f"{route}/assets/blocks/forms/search_keyword_form.json"
            await search_form(path)
            return
        if query['action_id'] == "form_search":
            forms['keyword'] = query['value']
            path = f"{route}/assets/blocks/forms/get_form.json"
            await get_form(forms, path)
            return

    return