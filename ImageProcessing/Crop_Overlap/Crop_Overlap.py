import cv2
import os


def save_img(crop_img, cnt, file, r_path):
    save_path = r_path + "crop_" + str(cnt) + "_" + os.path.basename(file)
    cv2.imwrite(save_path, crop_img)

def make_Folder(result_path):
    print()
    print("================ make folder ================")

    try:
        if not os.path.exists(result_path):
            os.makedirs((result_path), exist_ok=True)
    except OSError:
        print('Error: Creating directory. ' + result_path)

def Crop_Overlap( file, crop_w, crop_h, overlap, r_path ):
    # parameter
    # file      : image file path
    # crop_w    : width crop size
    # crop_h    : height crop size
    # overlap   : crop overlap size

    # crop_w, crop_h 를 기준으로 이미지를 crop 한다. 이때, 이미지를 overlap 크기만큼 겹치면서 계속해서 crop 한다.
    # 좌상단 부터 crop 을 시작하고, 각 행 또는 열 마다 마지막 이미지의 경우 이미지의 크기가 매우 작아질수 있기 때문에,
    # 마지막 행, 열의 crop 된 이미지는 이미지의 끝점을 기준으로 crop_w, crop_h 만큼 crop 한다.

    img = cv2.imread(file)

    w = img.shape[1]
    h = img.shape[0]

    w_cnt = (w - crop_w) / (crop_w - overlap ) + 1
    h_cnt = (h - crop_h) / (crop_h - overlap ) + 1

    crop_cnt = 0
    for y_idx in range( int(h_cnt)):
        for x_idx in range( int(w_cnt)):

            start_x = x_idx * (crop_w - overlap)
            start_y = y_idx * (crop_h - overlap)

            cropped_img = img [ start_y: start_y + crop_h, start_x : start_x + crop_w ]

            crop_cnt += 1
            save_img(cropped_img, crop_cnt, file, r_path)

        if int(w_cnt) < w_cnt:      # 이미지 우측 마지막 이미지
            start_y = y_idx * (crop_h - overlap)
            cropped_img = img [ start_y: start_y + crop_h,  w - crop_w: w]
            crop_cnt += 1
            save_img(cropped_img, crop_cnt, file, r_path)

    if int(h_cnt) < h_cnt:      # 이미지 하단 마지막 줄
        for x_idx in range(int(w_cnt)):
            start_x = x_idx * (crop_w - overlap)
            cropped_img = img[ h - crop_h: h , start_x: start_x + crop_w]
            crop_cnt += 1
            save_img(cropped_img, crop_cnt, file, r_path)

        cropped_img = img[h - crop_h: h, w - crop_w: w]
        crop_cnt += 1
        save_img(cropped_img, crop_cnt, file, r_path)



def main():
    result_path = './result/'

    file = 'original.jpg'

    make_Folder(result_path)

    Crop_Overlap(file, crop_w= 300, crop_h= 200 , overlap= 50, r_path= result_path)

if __name__ == "__main__":
	main()