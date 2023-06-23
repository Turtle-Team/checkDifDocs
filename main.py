import cv2
import PyPDF2
pdf1_path = 'path/to/first_document.pdf'
pdf2_path = 'path/to/second_document.pdf'

pdf1 = open(pdf1_path, 'rb')
pdf2 = open(pdf2_path, 'rb')

reader1 = PyPDF2.PdfReader(pdf1)
reader2 = PyPDF2.PdfReader(pdf2)

images1 = [cv2.imread(page) for page in reader1.pages]
images2 = [cv2.imread(page) for page in reader2.pages]
diff_pages = []

for page_num, (image1, image2) in enumerate(zip(images1, images2), start=1):
    difference = cv2.subtract(image1, image2)
    b, g, r = cv2.split(difference)
    if cv2.countNonZero(b) > 0 or cv2.countNonZero(g) > 0 or cv2.countNonZero(r) > 0:
        diff_pages.append(page_num)
if diff_pages:
    print("Отличия обнаружены на следующих страницах:")
    print(diff_pages)
else:
    print("Документы идентичны.")
pdf1.close()
pdf2.close()
