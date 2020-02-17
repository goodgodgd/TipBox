import urllib.request

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
speaker = "mijin"
url = "https://naveropenapi.apigw.ntruss.com/voice/v1/tts"


def text_to_voice(textfile, voicefile):
    with open(textfile, "rt", encoding="utf-8") as f:
        text = f.read()
    print("text:", text)
    voice = pull_voice(text)
    save_voice(voice, voicefile)


def pull_voice(text):
    enc_text = urllib.parse.quote(text)
    data = f"speaker={speaker}&speed=0&text={enc_text}"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID", client_id)
    request.add_header("X-NCP-APIGW-API-KEY", client_secret)
    request.add_header("Content-Type", "application/x-www-form-urlencoded")
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    assert rescode == 200, "Error Code:" + rescode
    return response.read()


def save_voice(voice, voicefile):
    print("음성 파일 저장:", voicefile)
    with open(voicefile, 'wb') as f:
        f.write(voice)


if __name__ == "__main__":
    text_to_voice("script.txt", "voice.mp4")
