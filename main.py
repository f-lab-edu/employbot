from fastapi import FastAPI, Body, Request
from pydantic.main import BaseModel
import uvicorn
import json

from SlackAPI import *
import slack_tokens

app = FastAPI()


# class SlackModel(BaseModel):
#     token: str
#     challenge: str
#     type: str

# @app.post("/")
# async def post_message(request_body: SlackModel = Body(...)):
#     response = {"challenge": request_body.challenge}
#     print(response)
#     return response

@app.post("/searchjob")
async def search_job():
    slack_client = SlackAPI(token=slack_tokens.SLACK_APP_TOKEN)
    blocks = [
		{
			"dispatch_action": True,
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action",
				"placeholder": {
					"type": "plain_text",
					"text": "파이썬 신입 개발자"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "원하시는 검색어를 입력하세요.",
				"emoji": True
			}
		}
	]
    result = slack_client.post_message(channel_id=slack_tokens.CHANNEL_ID, text="직업검색", blocks=blocks)
    return 


@app.post("/interactive")
async def get_job(request: Request):
    form_data = await request.form()
    payload = json.loads(form_data.get("payload"))
    query=payload["actions"][0]['value']
    slack_client = SlackAPI(token=slack_tokens.SLACK_APP_TOKEN)
    if query == None:
        result = slack_client.post_message(channel_id=slack_tokens.CHANNEL_ID, text="아무것도 입력하지 않았습니다.")
        return
    else:
        texts = f"""
		💡 {query} 관련 직무를 찾아보세요
		잡코리아 : https://www.jobkorea.co.kr/OnePick/JobList?Keyword={query}
		원티드 : https://www.wanted.co.kr/search?query={query}
		사람인 : https://www.saramin.co.kr/zf_user/search?searchword={query}
		"""
        result = slack_client.post_message(channel_id=slack_tokens.CHANNEL_ID, text=texts)
        return 


    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    
