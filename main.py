import os

from fastapi import FastAPI
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.socket_mode.aiohttp import AsyncSocketModeHandler
import uvicorn

from SlackAPI import *
import slack_tokens

app = FastAPI()
slack_app = AsyncApp(token=slack_tokens.SLACK_APP_TOKEN)
socket_handler = AsyncSocketModeHandler(slack_app, os.environ["SLACK_APP_TOKEN"])


@app.post("/")
async def post_message():
    query = "테스트입니다."
    text = "네 확인했습니다."
    slack_client = SlackAPI(token=slack_tokens.SLACK_APP_TOKEN)
    message_ts = slack_client.get_message(slack_tokens.CHANNEL_ID, query=query)
    result = slack_client.post_comment(slack_tokens.CHANNEL_ID, message_ts=message_ts, text=text)
    return result


@slack_app.command("searchapp")
async def search_job():
    slack_client = SlackAPI(token=slack_tokens.SLACK_APP_TOKEN)
    search_text = """
    - 잡코리아 : https://www.jobkorea.co.kr
    - 사람인 : https://www.saramin.co.kr/
    - 원티드 : https://www.wanted.co.kr/
    """
    result = slack_client.post_message(slack_tokens.CHANNEL_ID, text=search_text)

    return "result"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    
