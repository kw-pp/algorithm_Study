import json

# 사전 자료형(dict) 데이터 선언
user = {
  "id": "gildong",
  "password": "123456",
  "age": 30,
  "hobby": ["football","programming"]
}
# 인코딩: 파이썬 변수를 JSON 객체로 변환(띄어쓰기 네 칸 들여쓰기 적용)
json_data = json.dumps(user, indent=4)
print(json_data)

# 디코딩: JSON 객체를 파이썬 변수로 변환
data = json.loads(json_data)
print(data)

# JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
  json.dump(user, file, indent=4)