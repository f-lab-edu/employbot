from fastapi import FastAPI, Body, APIRouter, Request
import json
import os

from SlackAPI import *

router = APIRouter(
    prefix="/search",
)
slack_client = SlackAPI(token=SLACK_APP_TOKEN)

@router.post("/")
async def select_menu():
    elements_list = [
        {
            "text" : "통합 검색",
            "value" : "total",
            "url" : "",
        },
        {
            "text" : "세부 검색",
            "value" : "detail",
            "url" : "",
        }
    ]
    slack_client.post_message(CHANNEL_ID, text="select_menu", blocks=slack_client.action_buttons(elements_list))
    return

