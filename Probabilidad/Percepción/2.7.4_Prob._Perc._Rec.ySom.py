"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Percepción---> Reconocimiento de Objetos"""
import cv2
import numpy as np

def match_and_draw(image, template_paths, threshold=0.8):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_rgb_copy = img_rgb.copy()

    for template_path in template_paths:
        template = cv2.imread(template_path, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb_copy, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    return img_rgb_copy

template_paths = ['T_ojos.jpg', 'orejachida.jpg']
result_image = match_and_draw('Yoda.jpg', template_paths)

cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()