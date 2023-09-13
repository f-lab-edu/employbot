from fastapi import FastAPI
import uvicorn
from SlackAPI import *
import slack_tokens

app = FastAPI()

@app.post("/")
async def post_message():
    query = "테스트입니다."
    text = "네 확인했습니다."
    slack_client = SlackAPI(token=slack_tokens.BOT_TOKEN)
    message_ts = slack_client.get_message(slack_tokens.CHANNEL_ID, query=query)
    result = slack_client.post_comment(slack_tokens.CHANNEL_ID, message_ts=message_ts, text=text)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    