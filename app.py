from urllib.parse import parse_qs
from mitmproxy import http

json_file_path = "requests.json"
base_url = "realmofthemadgod.com/account/verify"
verify = False

def compute(accessToken, clientToken):
    with open('output.txt', 'w') as file:
        file.write(f"{accessToken}:{clientToken}")
    return

def request(flow: http.HTTPFlow) -> None:
    if base_url in flow.request.url:
        
        content_dict = parse_qs(flow.request.content.decode("utf-8"))
        content_formatted = {key: value[0] for key, value in content_dict.items()}
        request_data = {
            "url": flow.request.url,
            "method": flow.request.method,
            "headers": dict(flow.request.headers),
            "content": content_formatted,
        }
        try:
            accessToken = request_data["content"]["accessToken"]
            clientToken = request_data["content"]["clientToken"]

            compute(accessToken,clientToken)
        except:
            print(".")
