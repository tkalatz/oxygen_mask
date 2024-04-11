# oxygen_mask


start the roscore

... logging to /root/.ros/log/e811fde2-f7d3-11ee-ad67-0bf8a3c89da0/roslaunch-ubuntu-94845.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://ubuntu:45181/
ros_comm version 1.16.0


SUMMARY
========

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.16.0

NODES

auto-starting new master
process[master]: started with pid [94857]
ROS_MASTER_URI=http://ubuntu:11311/

setting /run_id to e811fde2-f7d3-11ee-ad67-0bf8a3c89da0
process[rosout-1]: started with pid [94870]
started core service [/rosout]

------------------------------------------------------------------------------------------------------

t@ubuntu:~/workspace$ roslaunch usb_cam test_img_view.launch

... logging to /home/tkalatz/.ros/log/e811fde2-f7d3-11ee-ad67-0bf8a3c89da0/roslaunch-ubuntu-94877.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://ubuntu:34245/

SUMMARY
========

PARAMETERS
 * /image_view/autosize: True
 * /rosdistro: noetic
 * /rosversion: 1.16.0
 * /usb_cam/camera_frame_id: head_camera
 * /usb_cam/camera_info_url: 
 * /usb_cam/camera_name: head_camera
 * /usb_cam/camera_transport_suffix: image_raw
 * /usb_cam/color_format: yuv422p
 * /usb_cam/create_suspended: False
 * /usb_cam/framerate: 30
 * /usb_cam/full_ffmpeg_log: False
 * /usb_cam/image_height: 480
 * /usb_cam/image_width: 640
 * /usb_cam/intrinsic_controls/exposure_auto: 3
 * /usb_cam/intrinsic_controls/exposure_auto_priority: True
 * /usb_cam/intrinsic_controls/focus_auto: True
 * /usb_cam/intrinsic_controls/ignore: ['brightness', 'c...
 * /usb_cam/intrinsic_controls/power_line_frequency: 1
 * /usb_cam/intrinsic_controls/white_balance_temperature_auto: True
 * /usb_cam/io_method: mmap
 * /usb_cam/pixel_format: yuyv
 * /usb_cam/start_service_name: start_capture
 * /usb_cam/stop_service_name: stop_capture
 * /usb_cam/video_device: /dev/video0

NODES
  /
    image_view (image_view/image_view)
    usb_cam (usb_cam/usb_cam_node)

ROS_MASTER_URI=http://localhost:11311

process[usb_cam-1]: started with pid [94894]
process[image_view-2]: started with pid [94895]
[ INFO] [1712820126.950508350]: Initializing nodelet with 4 worker threads.
[ INFO] [1712820128.629401843]: Initializing ROS V4L USB camera 'head_camera' (/dev/video0) at 640x480 via mmap (yuyv) at 30 FPS

[ INFO] [1712820144.201933904]: Using transport "raw"
[ INFO] [1712820144.947547122]: using default calibration URL
[ INFO] [1712820144.947614748]: camera calibration URL: file:///home/tkalatz/.ros/camera_info/head_camera.yaml
[ INFO] [1712820144.962753135]: Unable to open camera calibration file [/home/tkalatz/.ros/camera_info/head_camera.yaml]
[ WARN] [1712820144.962807981]: Camera calibration file /home/tkalatz/.ros/camera_info/head_camera.yaml not found.
[ INFO] [1712820144.983381103]: Advertising std_srvs::Empty start service under name 'start_capture'
[ INFO] [1712820145.003499312]: Advertising std_srvs::Empty suspension service under name 'stop_capture'
[ INFO] [1712820145.048624126]: Advertising std_srvs::Trigger supported formats information service under name 'supported_formats'
[ INFO] [1712820145.048994066]: Advertising std_srvs::Trigger supported V4L controls information service under name 'supported_controls'
Opening streaming device /dev/video0
Video4Linux: IOCTL is not supported
Video4linux: Querying V4L2 driver for available controls (register base 0x980900, 0..99)
Sorting control names:
	focus_automatic_continuous
	auto_exposure
	white_balance_automatic
	brightness
	contrast
	saturation
	hue
	gamma
	gain
	power_line_frequency
	white_balance_temperature
	sharpness
	backlight_compensation
	camera_controls
	exposure_time_absolute
	exposure_dynamic_framerate
	focus_absolute
	iris_relative
[ WARN] [1712820149.492617096]: NOTE: the parameters generated for V4L intrinsic camera controls will be placed under namespace 'intrinsic_controls'

------------------------------------------------------------------------------------------------------

source devel/setup.bash

catkin_make

t@ubuntu:~/fdetectors$ rosrun oxygen_mask oxygen_detector.py



