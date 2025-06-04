import cv2
import numpy as np
# بارگذاری تصویر
image = cv2.imread('F:/Project/buttons/54.jpg')
# تبدیل تصویر به خاکستری
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# اعمال بلور برای کاهش نویز
blurred = cv2.GaussianBlur(gray, (7, 7), 1.5)
# تشخیص لبه‌ها با استفاده از Canny
edges = cv2.Canny(blurred, 30, 150)
# پیدا کردن نقاط کلیدی با استفاده از HoughCircles
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=30)
# شمارش دکمه‌ها
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # رسم دایره برای هر دکمه شناسایی شده
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)  # دایره سبز
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)  # مرکز دایره قرمز
    # نمایش تصویر با دکمه‌های شناسایی شده
    cv2.imshow('Detected Buttons', image)
    # چاپ تعداد دکمه‌ها
    print(f"تعداد دکمه های شناسایی شده: {len(circles[0])}")
else:
    print("دکمه ای شناسایی نشد.")
# نگه‌داشتن پنجره‌ها
cv2.waitKey(0)
cv2.destroyAllWindows()