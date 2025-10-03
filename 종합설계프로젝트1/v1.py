import re
from collections import Counter

# 간단한 감정어휘 사전 (예시)
emotion_dict = {
    "기쁨": ["행복", "즐겁", "재밌", "좋"],
    "슬픔": ["슬프", "눈물", "우울", "외롭"],
    "분노": ["화", "짜증", "싫", "미워"],
    "불안": ["걱정", "긴장", "두렵", "불안"]
}

def analyze_emotion(text):
    results = Counter()
    for category, keywords in emotion_dict.items():
        for word in keywords:
            matches = re.findall(word, text)
            results[category] += len(matches)
    return results

# 예시 텍스트
student_text = "요즘 학업이 힘들고 불안해서 걱정이 많아요. 친구들이랑 있으면 잠시 재밌긴 해요."

print(analyze_emotion(student_text))
