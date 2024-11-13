from PIL import Image
import tkinter as tk
from tkinter import filedialog

root =tk.Tk()
root.withdraw()

img_files = filedialog.askopenfilenames(
    title="Select image files",
    filetypes=[("Image Files","*.png;*.jpg;*jpeg")],
)

if not img_files:
    print("File is not selected!")
    exit()

# 이미지를 읽어들임 (모두 RGB 모드로 변환)
image_list = [Image.open(img).convert('RGB') for img in img_files]

# 과제로 낼 때 이름 바꾸기 귀찮으니까, 만들 때부터 입력하고 만듭시다. .pdf 는 안붙여도 됨.
pdf_path = input("Input your filename : ")
pdf_path = f'{pdf_path}.pdf'

# 첫 번째 이미지를 기준으로 PDF 파일로 저장하고, 나머지 이미지는 추가합니다.
image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])
