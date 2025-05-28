0. OpenWeatherMap API 사용
   - 1. OpenWeatherMap에 회원가입
   - 2. APK key 생성

---

### AWS

1. Agent 생성

2. Agent의 속성을 설정

  - Instructions for the Agent

```text
당신은 날씨 전문가 역할을 수행하는 에이전트입니다. 요청하는 위치의 날씨를 친절하게 알려주세요.
```

3. Action Group을 추가

4. Action Group에서 사용하는 Lambda 함수 생성

[함수의 구조, 반환 결과값의 구조](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html)


```bash
pip install requests -t ./my_lambda_package
cp lambda_function.py my_lambda_package/
cd my_lambda_package
zip -r my_lambda_function.zip .
```