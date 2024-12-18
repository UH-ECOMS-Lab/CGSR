import os
import argparse
import numpy as np
import cv2
from scipy.signal import find_peaks
from collections import Counter

def retain_periodic_elements(arr, tolerance=5):
    intervals = np.diff(arr)
    interval_counts = Counter(intervals)
    most_common_interval, _ = interval_counts.most_common(1)[0]

    filtered_indices = [0]
    for i in range(1, len(intervals)):
        if abs((intervals[i-1] % most_common_interval)) < tolerance or abs((most_common_interval % intervals[i-1])) < tolerance:
            filtered_indices.append(i)

    return arr[filtered_indices]

def retain_valid_lines(mask, min_length=10):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=8)
    valid_mask = np.zeros_like(mask)

    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        x, y, w, h = stats[i, cv2.CC_STAT_LEFT], stats[i, cv2.CC_STAT_TOP], stats[i, cv2.CC_STAT_WIDTH], stats[i, cv2.CC_STAT_HEIGHT]

        if max(w, h) >= min_length:
            valid_mask[labels == i] = 255

    return valid_mask

def process_image(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    r_channel = image[:, :, 2]

    row_sums = np.sum(r_channel == 255, axis=1)
    col_sums = np.sum(r_channel == 255, axis=0)

    row_peaks, _ = find_peaks(row_sums, height=0, distance=10, prominence=10)
    col_peaks, _ = find_peaks(col_sums, height=0, distance=10, prominence=10)

    row_peaks = retain_periodic_elements(row_peaks)
    col_peaks = retain_periodic_elements(col_peaks)

    mask = np.zeros_like(r_channel, dtype=np.uint8)

    for row in row_peaks:
        mask[row, :] = 255

    for col in col_peaks:
        mask[:, col] = 255

    valid_mask = retain_valid_lines(r_channel & mask, min_length=10)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    closing = cv2.morphologyEx(valid_mask, cv2.MORPH_CLOSE, kernel)
    valid_r_channel = retain_valid_lines(r_channel ^ valid_mask, min_length=10)

    image[:, :, 2] = valid_r_channel

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    base_filename = os.path.basename(image_path)
    output_filepath = os.path.join(output_path, base_filename)

    cv2.imwrite(output_filepath, image)

def main():
    parser = argparse.ArgumentParser(description='Enhance trace images')
    parser.add_argument('--input_path', type=str, required=True, help='Path to input images')
    parser.add_argument('--output_path', type=str, required=True, help='Path to save enhanced images')

    args = parser.parse_args()

    input_dir = args.input_path
    output_dir = args.output_path

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.bmp') or filename.endswith('.jpg'):
            input_filepath = os.path.join(input_dir, filename)
            process_image(input_filepath, output_dir)
            print(f'Processed {input_filepath} -> {output_dir}')

if __name__ == "__main__":
    main()

