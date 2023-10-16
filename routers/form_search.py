from routers import *

@router.post('/form')
async def search_detail_job():
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
			"block_id": "sectionBlockWithRadioButtons",
			"text": {
				"type": "mrkdwn",
				"text": "*직무 선택*"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "👨‍💻 개발,데이터",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "🎨 디자인",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "🗓️ 기획, 전략",
							"emoji": True
						},
						"value": "value-2"
					}
				],
				"action_id": "radio_buttons-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*지역 선정*"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Location"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "서울"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "경기"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "인천"
						},
						"value": "value-2"
					}
				]
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*경력 선택*"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Career"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "경력 무관"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "신입"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "경력"
						},
						"value": "value-2"
					}
				]
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*학력 선택*"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "EduLevel"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "학력 무관"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "대학교 졸업(2,3년)"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "대학교 졸업(4년)"
						},
						"value": "value-2"
					},
					{
						"text": {
							"type": "plain_text",
							"emoji": True,
							"text": "대학원 석사졸업"
						},
						"value": "value-2"
					}
				]
			}
		},
		{
			"type": "input",
			"element": {
				"type": "checkboxes",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "💷 적절한 보상",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "⏰ 유연근무제",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "🔥 인기 많은 공고",
							"emoji": True
						},
						"value": "value-2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "🌎 외국계 기업",
							"emoji": True
						},
						"value": "value-3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "💎 탄탄한 기업",
							"emoji": True
						},
						"value": "value-4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "📈 스톡옵션 제공",
							"emoji": True
						},
						"value": "value-5"
					}
				],
				"action_id": "checkboxes-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Label",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "추가 검색어를 입력해주세요.",
				"emoji": True
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "직무 검색"
					},
					"value": "click_me_123"
				}
			]
		}
	]
    result = slack_client.post_message(channel_id=CHANNEL_ID, text="디테일검색", blocks=blocks)
    return