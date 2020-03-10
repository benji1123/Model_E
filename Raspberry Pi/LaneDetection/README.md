Contents
--------
* __RPilaneDetection.py__: local script
* __RPilaneDetection_withTimeTest.py__: local script that also evaluates time taken by each function

Performance Test
---------------------
Time spent in each function (seconds):
* _detect_edges_:  0.007003
* _region_of_interest_:  0.0004969
* _detect_line_segments_:  0.0110026
* _make_points_: 1.81e-05
* _make_points_: 3.49e-05
* _average_slope_intercept_ : 0.0738952 <== key bottleneckw
* _detect_lane_:  0.1039518
* _compute_steering_angle_ : 2.09e-05
* _stabilize_steering_angle_ : 8.8e-06

Process
--------
Source-code by [David Tian](https://towardsdatascience.com/deeppicar-part-4-lane-following-via-opencv-737dd9e47c96)

The sequence of image-processing filters are shown programmatically by setting `_SHOW_IMAGE = True` 

1. input frame
2. blue-color filter
3. Canny Edge Detector
4. (un-pictured) mask that eliminates top-half of frame
5. Hough Line Transform
6. Derive lane-lines
7. Draw heading


![](images/test.PNG)
![](images/blue_mask.PNG)
![](images/edges.PNG)
![](images/line_segments.PNG)
![](images/lane_lines.PNG)
![](images/final.PNG)
