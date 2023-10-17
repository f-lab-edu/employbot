from routers import *

@router.post("/total")
async def search_job():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    blocks = [
		{
			"dispatch_action": True,
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "total_search",
				"placeholder": {
					"type": "plain_text",
					"text": "파이썬 신입"
				}
			},
			"label": {
				"type": "plain_text",
				"text": "기업명, 공고명등 검색해보세요.",
				"emoji": True
			}
		}
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="직업검색", blocks=blocks)
    return 



async def get_job(query):
    if query == None:
        result = slack_client.post_message(channel_id=CHANNEL_ID, text="아무것도 입력하지 않았습니다.")
        return
    else:
        query = query.replace(" ", "%20")
        texts = f"""
		💡 관련 직무를 찾아보세요.
		잡코리아 : https://www.jobkorea.co.kr/OnePick/JobList?Keyword={query}
		원티드 : https://www.wanted.co.kr/search?query={query}
		사람인 : https://www.saramin.co.kr/zf_user/search?searchword={query}
		"""
        blocks = [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"emoji": True,
				"text": "입력하신 검색어의 통합 결과를 확인하세요."
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*원티드(Wanted)*"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"emoji": True,
					"text": "Search"
				},
				"value": "wanted_result",
                "url": f"https://www.wanted.co.kr/search?query={query}",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*잡코리아(JobKorea)*"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"emoji": True,
					"text": "Search"
				},
                "value": "jobkorea_result",
                "url": f"https://www.jobkorea.co.kr/OnePick/JobList?Keyword={query}",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*사람인(Saram in)*"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"emoji": True,
					"text": "Search"
				},
                "value": "saramin_result",
                "url": f"https://www.saramin.co.kr/zf_user/search?searchword={query}",
				"action_id": "button-action"
			}
		}
		]
        result = slack_client.post_message(channel_id=CHANNEL_ID, text=texts, blocks=blocks)
        return 