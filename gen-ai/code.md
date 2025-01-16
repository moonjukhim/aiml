### 청크 사이즈의 변경

```python
from langchain.text_splitter import CharacterTextSplitter

# 문서 내용 예시
text = """
LangChain은 LLM 애플리케이션 개발을 돕는 강력한 도구입니다.
이 도구를 사용하면 문서를 다양한 방식으로 처리할 수 있습니다.
"""

# 청크 크기와 중첩 범위 설정
chunk_size = 50             # 청크 크기
chunk_overlap = 10          # 청크 간 중첩

# TextSplitter 초기화
text_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separator="\n"          # 문단별로 나누고 싶다면 '\n' 사용
)

# 문서를 청크로 분할
chunks = text_splitter.split_text(text)

# 결과 확인
for i, chunk in enumerate(chunks):
    print(f"청크 {i+1}:")
    print(chunk)
    print("-" * 50)
```
