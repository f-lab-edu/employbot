from slack_sdk import WebClient
import slack_tokens

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
        result = self.client.conversations_history(channel=channel_id)
        # 채널 내 메세지 정보 리스트
        messages = result.data['messages']
        # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
        message = list(filter(lambda m: m['text'] == query, messages))[0]
        # 해당 메세지ts를 파싱
        message_ts = message["ts"]
        return message_ts
    
    def post_message(self, channel_id, text):
        """
        ### 슬랙 채널 내 메세지 포스팅
        - parameter : `channel_id`, `text`
        - return : `result`
        """
        result = self.client.chat_postMessage(
            channel = channel_id,
            text = text,
        )
        return result
    
    def post_comment(self, channel_id, message_ts, text):
        """
        ### 슬랙 채널 내 메세지의 Thread에 댓글 달기
        - parameter : `channel_id`, `message_ts`, `text`
        - return : `result`
        """
        result = self.client.chat_postMessage(
            channel = channel_id,
            text = text,
            thread_ts = message_ts
        )
        return result




    
