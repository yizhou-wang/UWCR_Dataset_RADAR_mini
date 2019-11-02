# UWCR Dataset - RADAR MINI

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

### Metadata Parser
