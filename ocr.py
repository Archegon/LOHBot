import easyocr
import cv2


class Ocr:
    reader = easyocr.Reader(['en'])
    font = cv2.QT_FONT_NORMAL

    def __init__(self):
        self.result = None
        self.img = None
        self.result_path = 'images/ocr_result.png'

    def read(self, img, visualize=False):
        self.img = img
        self.img = cv2.imread(self.img)
        self.result = Ocr.reader.readtext(self.img)

        if visualize:
            for item in self.result:
                top_left = tuple([int(val) for val in item[0][0]])
                bottom_right = tuple([int(val) for val in item[0][2]])
                text = item[1]

                self.img = cv2.rectangle(self.img, top_left, bottom_right, (0, 255, 0), 2)
                self.img = cv2.putText(self.img, text, top_left, self.font, 1, (35, 169, 247), 2, cv2.LINE_AA)

            cv2.imwrite(self.result_path, self.img)
            cv2.imshow('Result', self.img)
            cv2.waitKey(0)

        return self.result
