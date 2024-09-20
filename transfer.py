
from PIL import Image
import os

# 이미지들이 저장되어 있는 디렉토리
path = 'assignment_img/'

# 처리할 이미지 확장자 목록
valid_extensions = ('.png', '.jpg', '.jpeg')  # 필요에 따라 확장자 추가합니다

# path 디렉토리에 있는 이미지 파일 리스트 받아옵니다 (이미지 확장자만 필터링)
img_files = [os.path.join(path, img) for img in os.listdir(path) if img.lower().endswith(valid_extensions)]

# 이미지를 읽어들임 (모두 RGB 모드로 변환)
image_list = [Image.open(img).convert('RGB') for img in img_files]

# 과제로 낼 때 이름 바꾸기 귀찮으니까, 만들 때부터 입력하고 만듭시다. .pdf 는 안붙여도 됨.
pdf_path = input("Input your filename : ")
pdf_path = f'{pdf_path}.pdf'

# 첫 번째 이미지를 기준으로 PDF 파일로 저장하고, 나머지 이미지는 추가합니다.
image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])
