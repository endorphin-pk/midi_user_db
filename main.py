#pyinstaller --onefile main.py
import firebase
import secret
import os

version="1.1a"

#print(f"{os.environ['temp']}\\secret.json")
f=open(f"{os.environ['temp']}\\secret.json","w")
f.write(secret.secret_json)
f.close()
firebase.setup(f"{os.environ['temp']}\\secret.json")
if(firebase.read("최신버전")!=version):
    print("업데이트 안 하셨죠?")
    print("https://github.com/endorphin-pk/midi_user_db")
    print("여기서 최신 버전을 다운받으세요.")
    print("만약 최신 버전이 없거나 계속 에러가 나면, 디스코드 _엔돌핀#6772 에게 메시지주세요.")
    input("아무 키나 눌러 종료할게요.")
    exit()
while True:
    # noinspection PyBroadException
    try:
        raw=input("조회=1, 기록/수정=2, 삭제=3\n")
        if(raw=="2"):
            #write
            name=input("대상의 닉네임:")
            count=input("경고 횟수:")
            data={"경고":count}
            firebase.write(data,f"유저/{name}")
            print("\n")
            continue
        if(raw=="3"):
            name = input("대상의 닉네임:")
            firebase.delete(f"유저/{name}")
            print("\n")
            continue
        if(raw=="1"):
            data=firebase.read("유저")
            #data=json.dumps(data)
            try:
                for key,value in data.items():
                    print(f"{key} - {value['경고']}")
            except AttributeError:
                print("유저가 없습니다")
            finally:
                print("\n")
    except Exception as e:
        print("어어어어어...잠깐만요!")
        print("에러가 났어요.")
        print("이 메세지를 디스코드 _엔돌핀#6772 에게 보내주세요.")
        print(f"\n{e}")
        input("아무 키나 눌러서 종료하세요.")
        break