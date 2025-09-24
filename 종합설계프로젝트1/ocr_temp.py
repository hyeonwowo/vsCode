import pytesseract
import os
from PIL import Image
from PIL import ImageEnhance
from pathlib import Path

# !! 일단 리포트 데이터 부분만 잘라내어 png 파일로 저장 후 인풋으로 사용
# !! 전처리를 통해 인식률 향상 필요(특히 % 인식)
# !! json 형식 저장 필요

# Tesseract 설치 필요
# Tesseract 경로 설정 (본인 환경에 맞게 수정)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # 'which tesseract'로 찾은 경로 입력

# 이미지 설정
image_path = Path(__file__).parent / 'test.png'
out_dir = Path(os.path.dirname(__file__)) / "ocr_right_panel_out"
out_dir.mkdir(parents=True, exist_ok=True)


# -----------------------------
# 1) OCR 실행
# -----------------------------
def run_ocr(pil_img):
    # --oem 3: Tesseract 5의 LSTM 엔진 사용
    # --psm 6: 단일 균일 텍스트 블록으로 간주
    # -l kor+eng: 한글과 영어를 동시에 인식
    config = "--oem 3 --psm 6 -l kor+eng"
    return pytesseract.image_to_string(pil_img, config=config)


# -----------------------------
# 2) 전처리: 이미지 크기 확대
# -----------------------------
def resize_image(pil_img, scale_factor=2):
    """
    OCR 정확도를 높이기 위해 이미지 크기를 확대합니다.
    """
    width, height = pil_img.size
    new_size = (width * scale_factor, height * scale_factor)
    # LANCZOS 필터는 고품질의 축소/확대 시 사용
    return pil_img.resize(new_size, Image.LANCZOS)


# -----------------------------
# 3) 메인
# -----------------------------
def main():
    try:
        # 원본이 팔레트(P)일 수 있으므로 RGB로 통일
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print(f"오류: 파일 '{image_path}'를 찾을 수 없습니다.")
        return

    W, H = img.size
    print(f"원본 이미지 크기: {W}x{H}")

    # ====== 특정 영역(픽셀 좌표)으로 자르기 ======
    # 정서 데이터 오른쪽 텍스트 영역
    p1_right_box = (1055, 672, 1460, 1104)
    # 뇌파 데이터 오른쪽 텍스트 영역
    p2_right_box = (1055, 1594, 1460, 2009)

    # 첫 번째 영역 잘라내기
    p1_right = img.crop(p1_right_box)
    # 두 번째 영역 잘라내기
    p2_right = img.crop(p2_right_box)

    # 디버그용으로 최종 ROI를 저장
    p1_right.save(out_dir / "_debug_emotion_cropped.png")
    p2_right.save(out_dir / "_debug_eeg_cropped.png")

    # ====== 전처리: 크기 확대 ======
    p1_right_resized = resize_image(p1_right)
    p2_right_resized = resize_image(p2_right)

    # 확대된 이미지 저장
    p1_right_resized.save(out_dir / "_debug_emotion_resized.png")
    p2_right_resized.save(out_dir / "_debug_eeg_resized.png")
    print("\n이미지를 2배 확대한 후 OCR을 진행합니다.")

    print("\n--- emotion OCR ---")
    text1 = run_ocr(p1_right_resized)
    print(text1)

    print("\n--- eeg OCR ---")
    text2 = run_ocr(p2_right_resized)
    print(text2)

    # 결과 텍스트 파일로 저장
    (out_dir / "emotion_text.txt").write_text(text1, encoding="utf-8")
    (out_dir / "eeg_text.txt").write_text(text2, encoding="utf-8")
    print(f"\n저장 완료: {out_dir/'emotion_text.txt'}, {out_dir/'eeg_text.txt'}")


if __name__ == "__main__":
    main()
