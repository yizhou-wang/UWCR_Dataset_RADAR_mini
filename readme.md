# UWCR Dataset - RADAR MINI

## Download

Please download our dataset from the following link (4.3GB): https://drive.google.com/open?id=1K31JGj0LNVQvd4oHFqcKkaSK36CQVAhA

## Summary

There are 9 RaDAR sequences in this dataset. 
Each sequence has a framerate of 30 FPS, 255 chirps per frame, and length around 900 frames

The dataset stucture is shown below. 
```
━ UWCR_RADAR_MINI
    ┗ data
        ┗ 2019_04_09
            ┗ 2019_04_09_cms1000
                ┣ radar
                ┗ ramap_labels.csv
            ┗ ... (sequence names)
            ┗ 2019_04_09_pss1003
    ┗ scripts
```

For each data sequence, RaDAR data are in `radar` folder with `*.bin` format. 
Metadata annotations are stored in `*.csv` format. 

## Usages

### RaDAR Data Preprocessing

Written in MATLAB format in `parse_radar.m`.

### Metadata Parser

Metadata parser script is in Python format in scripts folder named `radar_anno_loader.py`.
Sequence path can be set inside the script. 
The result return from function `read_ra_labels_csv(seq_path)` can be described as follows:

- Return a list of object annotation with length of frame number.
- Each element of the list is `[range_idx, angle_idx, class_id]`. 
- The mapping function for range/angle index to real value is written in `mappings.py`.
