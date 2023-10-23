from slack_sdk import WebClient
from dotenv import load_dotenv
import os 

# load .env
load_dotenv()
SLACK_APP_TOKEN = os.environ.get('SLACK_APP_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

class SlackAPI:
    """
    Slack API Handler
    """
    def __init__(self, token):
        """
        ### `WebClient`
        - `self.client` : `token`(OAuth Token)을 받아 Slack과 상호작용을 허락합니다.
        """
        self.client = WebClient(token)

    def get_message(self, channel_id, query):
        """
        ### 슬랙 채널 메세지 조회
        - parameter : `channel_id`, `query`
        - return : `message_ts`
        """
        result = self.client.conversations_history(channel=CHANNEL_ID)
        # 채널 내 메세지 정보 리스트
        messages = result.data['messages']
        # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
        message = list(filter(lambda m: m['text'] == query, messages))[0]
        # 해당 메세지ts를 파싱
        message_ts = message["ts"]
        return message_ts
    
    def post_message(self, channel_id, text, blocks = None):
        """
        ### 슬랙 채널 내 메세지 포스팅
        - parameter : `channel_id`, `text`
        - return : `result`
        """
        response = self.client.conversations_list()
        channels = response["channels"]
        channel_id = None
        for channel in channels:
            if channel['name'] == 'employbot':
                channel_id = channel["id"]
                break
            

        if channel_id is not None:
            args = {"channel": channel_id, "text": text, "blocks" : blocks}
            return self.client.chat_postMessage(**args)
    
    def post_comment(self, channel_id, message_ts, text):
        """
        ### 슬랙 채널 내 메세지의 Thread에 댓글 달기
        - parameter : `channel_id`, `message_ts`, `text`
        - return : `result`
        """
        args = {"channel":channel_id, "text":text, "thread_ts":message_ts}
        return self.client.chat_postMessage(**args)

    def action_buttons(self, elements: list):
        """
        #### Menu 내 세부 블록 가져오기
        - parameter : `elements`
        - return : `blocks`
        """
        blocks = [		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "🤖 안녕하세요. 취업봇입니다.",
				"emoji": True
			}
		},
		{
			"type": "rich_text",
			"elements": [
				{
					"type": "rich_text_section",
					"elements": [
						{
							"type": "text",
							"text": """
                            여러분의 취업 성공을 위해 제작되었습니다.원하시는 메뉴를 선택해주세요.
또한, `Slash-Command`를 이용해서 입력하실 수 있습니다.
                            """
						}
					]
				}
			]
		},
		{
			"type": "divider"
		},
        {
            "type":"actions",
            "elements": [],
        }]

        for row in elements:
            blocks[3]['elements'].append(
                                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": row["text"],
                    },
                    "value": row["value"],
                }
            )

        return blocks



    
