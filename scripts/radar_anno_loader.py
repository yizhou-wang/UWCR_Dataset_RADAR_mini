import os
import numpy as np
import pandas as pd
import json

from .mappings import confmap2ra, labelmap2ra

radar_configs = {
    'ramap_rsize': 128,             # RAMap range size
    'ramap_asize': 128,             # RAMap angle size
    'frame_rate': 30,
    'crop_num': 3,                  # crop some indices in range domain
    'n_chirps': 255,                # number of chirps in one frame
    'sample_freq': 4e6,
    'sweep_slope': 21.0017e12,
    'data_type': 'RISEP',           # 'RI': real + imaginary, 'AP': amplitude + phase
    'ramap_rsize_label': 122,       # TODO: to be updated
    'ramap_asize_label': 121,       # TODO: to be updated
    'ra_min_label': -60,            # min radar angle
    'ra_max_label': 60,             # max radar angle
    'rr_min': 1.0,                  # min radar range
    'rr_max': 25.0,                 # max radar range
    'ra_min': -90,                  # min radar angle
    'ra_max': 90,                   # max radar angle
    'ramap_folder': 'WIN_HEATMAP',
}

class_ids = {
    'pedestrian': 0,
    'cyclist': 1,
    'car': 2,
    'noise': -1000,
}


def find_nearest(array, value):
    """
    Find nearest value to 'value' in 'array'
    :param array:
    :param value:
    :return:
    """
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx, array[idx]


def read_ra_labels_csv(seq_path):

    label_csv_name = os.path.join(seq_path, 'ramap_labels.csv')
    data = pd.read_csv(label_csv_name)
    n_row, n_col = data.shape
    obj_info_list = []
    cur_idx = -1

    range_grid = confmap2ra(radar_configs, name='range')
    angle_grid = confmap2ra(radar_configs, name='angle')
    range_grid_label = labelmap2ra(radar_configs, name='range')
    angle_grid_label = labelmap2ra(radar_configs, name='angle')

    for r in range(n_row):
        filename = data['filename'][r]
        frame_idx = int(filename.split('.')[0].split('_')[-1])
        if cur_idx == -1:
            obj_info = []
            cur_idx = frame_idx
        if frame_idx > cur_idx:
            obj_info_list.append(obj_info)
            obj_info = []
            cur_idx = frame_idx

        region_count = data['region_count'][r]
        region_id = data['region_id'][r]

        if region_count != 0:
            region_shape_attri = json.loads(data['region_shape_attributes'][r])
            region_attri = json.loads(data['region_attributes'][r])

            cx = region_shape_attri['cx']
            cy = region_shape_attri['cy']
            distance = range_grid_label[cy]
            angle = angle_grid_label[cx]
            rng_idx, _ = find_nearest(range_grid, distance)
            agl_idx, _ = find_nearest(angle_grid, angle)
            class_str = region_attri['class']
            try:
                class_id = class_ids[class_str]
            except:
                if class_str == '':
                    print("no class label provided!")
                    raise ValueError
                else:
                    class_id = -1000
                    print("Warning class not found! %s %010d" % (seq_path, frame_idx))
            obj_info.append([rng_idx, agl_idx, class_id])

    obj_info_list.append(obj_info)

    return obj_info_list


if __name__ == '__main__':
    seq_path = 'data/2019_04_09/2019_04_09_cms1000'
    obj_info_list = read_ra_labels_csv(seq_path)
