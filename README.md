# parking_spot_detector_and_counter_using_opencv_and_scikit-learn
This project is aimed at developing a parking spot detection system using computer vision techniques. It can analyze video footage from a parking lot and determine the availability of parking spots in real-time.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction

The goal of this project is to assist in monitoring parking lots, helping drivers find available spots quickly and efficiently. The system detects whether each parking spot is occupied or empty by analyzing video frames captured by a surveillance camera.

The main components of the project include:

- **Background Masking**: A pre-defined mask of the parking lot is used to isolate the region of interest from the video frames.
- **Connected Components Analysis**: It identifies individual parking spots within the masked region.
- **Spot Status Classification**: Each parking spot gets masked and then classified using machine learning classifier whose source code can be found [here](https://github.com/umairsiddique3171/Machine-Learning-Projects/tree/main/car_parking_spot_empty_or_non-empty_classification).
- **Performance Optimization**: By comparing consecutive frames, the system determines whether each spot is occupied or empty.
- **Real-time Visualization**: The results are displayed in real-time, indicating the availability of parking spots.

## Installation

1. Clone this repository:

```
git clone https://github.com/umairsiddique3171/parking_spot_detector_and_counter_using_opencv_and_scikit-learn.git
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Ensure that the video dataset is placed in the data directory and the background mask is saved as mask.png.
2. Run the main script:
```
python main.py
```
The system will process the video frames and display real-time visualizations of parking spot availability.

## Results

The system outputs a video file (results.mp4) where each frame indicates the status of parking spots. Occupied spots are marked in green rectangles, while empty spots are marked in red. Additionally, the total number of available spots is displayed in the corner of the video frame.

https://github.com/umairsiddique3171/parking_spot_detector_and_counter_using_opencv_and_scikit-learn/assets/148565997/5eb2de84-c002-494c-a202-6114229a0dcf

## License
[MIT License](https://github.com/umairsiddique3171/parking_spot_detector_and_counter_using_opencv_and_scikit-learn/blob/main/LICENSE)

## Author
[@umairsiddique3171](https://github.com/umairsiddique3171)
