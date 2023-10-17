from routers import *

@router.post('/form')
async def search_form():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)

    blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":mag: 자세하게 *직무* 를 검색해드립니다."
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"block_id": "form_1",
			"text": {
				"type": "mrkdwn",
				"text": "원하시는 직무가 있을까요?🙂"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "👨‍💻 개발, 데이터",
							"emoji": True
						},
						"value": "10031"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "🎨디자인",
							"emoji": True
						},
						"value": "10032"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "🗓️기획, 전략",
							"emoji": True
						},
						"value": "10026"
					}
				],
				"action_id": "form_1"
			}
		},
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return 


async def search_form_loc():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)

    blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":mag: 그다음, 구직을 희망하시는 지역을 골라주세요."
			}
		},
		{
			"type": "divider"
		},
        {
			"type": "section",
			"block_id": "form_2",
			"text": {
				"type": "mrkdwn",
				"text": "지역 선정"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Location",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "서울",
							"emoji": True
						},
						"value": "I000"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "경기",
							"emoji": True
						},
						"value": "B000"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "인천",
							"emoji": True
						},
						"value": "K000"
					}
				],
				"action_id": "form_2"
			}
		}
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return 

async def search_form_car():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)

    blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":mag: 신입으로 지원하시나요? 아니면 경력으로 지원하시나요?"
			}
		},
		{
			"type": "divider"
		},
        {
			"type": "section",
			"block_id": "form_3",
			"text": {
				"type": "mrkdwn",
				"text": "경력 선택"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Career",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "무관",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "신입",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "경력",
							"emoji": True
						},
						"value": "2"
					}
				],
				"action_id": "form_3"
			}
		}
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return 

async def search_form_edulevel():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":mag: 학력을 선택해주세요."
			}
		},
		{
			"type": "divider"
		},
        {
			"type": "section",
			"block_id": "form_4",
			"text": {
				"type": "mrkdwn",
				"text": "학력 선택"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Edulevel",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "학력 무관",
							"emoji": True
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "대학교 졸업(2,3년)",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "대학교 졸업(4년)",
							"emoji": True
						},
						"value": "5"
					},
                    {
						"text": {
							"type": "plain_text",
							"text": "대학원 졸업(석사)",
							"emoji": True
						},
						"value": "6"
					}
				],
				"action_id": "form_4"
			}
		}
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return 

async def search_form_filter():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    blocks = [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":mag: 원하시는 옵션이 있을까요?"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"block_id": "form_5",
			"text": {
				"type": "mrkdwn",
				"text": "복수 선택 가능합니다."
			},
			"accessory": {
				"type": "multi_static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "옵션을 선택해주세요.",
					"emoji": True
				},
				"options": [
                    {
						"text": {
							"type": "plain_text",
							"text": "❌ 해당 없음",
							"emoji": True
						},
						"value": "0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "💷 적절한 보상",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⏰ 유연 근무제",
							"emoji": True
						},
						"value": "5"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "💎 단단한 회사",
							"emoji": True
						},
						"value": "7"
					}
				],
				"action_id": "form_5"
			}
		}
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return 

async def search_form_keyword():
    slack_client = SlackAPI(token=SLACK_APP_TOKEN)
    blocks = [
		{
			"type": "section",
            "block_id": "form_6",
			"text": {
				"type": "mrkdwn",
				"text": ":mag: 마지막으로 원하시는 추가 검색어를 입력하시면 알선 도와드리겠습니다."
			}
		},
		{
			"type": "divider"
		},
        {
			"dispatch_action": True,
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "form_search"
			},
			"label": {
				"type": "plain_text",
				"text": "추가로 원하시는 검색어가 있다면 입력해주세요.",
				"emoji": True
			}
		},
		{
			"type": "divider"
		}
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return    

async def get_form(forms):
    if len(forms['Filter']) == 1:
        filters = ''.join(forms['Filter'])
    elif len(forms['Filter']) == 0:
        filters = ''
    else:
        filters = '%2C'.join(forms['Filter'])
        
    filters  ='%'.join(forms['Filter'])
    keyword = forms['keyword'].replace(" ","%20")
    text = f"https://www.jobkorea.co.kr/OnePick/JobList?Keyword={keyword}&Ord=GcmCodeAmtDesc&DutyCtgr={forms['DutyCtgr']}&Local={forms['Local']}&CareerType={forms['CareerType']}&EduLevel={forms['EduLevel']}&Filter={filters}"
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
				"text": "*잡코리아*"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"emoji": True,
					"text": "Search"
				},
				"value": "wanted_result",
                "url": f"https://www.jobkorea.co.kr/OnePick/JobList?Keyword={keyword}&Ord=GcmCodeAmtDesc&DutyCtgr={forms['DutyCtgr']}&Local={forms['Local']}&CareerType={forms['CareerType']}&EduLevel={forms['EduLevel']}&Filter={filters}",
				"action_id": "button-action"
			}
		}
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID,text = text, blocks=blocks)
    return 