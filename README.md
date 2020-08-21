# Raspberry_Pi_based_mask_detector

## Installing dependencies:

#### First of all, we need to install opencv for image processing and tflite_runtime to load our face_mask_detection model. The remaining dependencies can be installed directly via pip or pip3.

Step 1. Installing tflite_runtime.
  
  a. Go to https://www.tensorflow.org/lite/guide/python.
  
  b. Select the appropriate package for installed python version on your Raspberry Pi ( In case you don’t know then open the terminal and execute “python3 --version”).
  
  c. Copy the URL and install the package using pip3. For example, if you have Raspberry Pi that's running Raspbian Buster (which has Python 3.7), install the Python wheel by executing:

    
    pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl

   

This will install the tflite_runtime on your Raspberry Pi. You can always check the installed packages by running “pip3 list” in the terminal.

 

 

Step 2. Installing OpenCV.

 a. Install OpenCV 4 dependencies

    sudo apt-get update && sudo apt-get upgrade
    sudo apt-get install build-essential cmake unzip pkg-config
    sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
    sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
    sudo apt-get install libxvidcore-dev libx264-dev
    sudo apt-get install libgtk-3-dev


    sudo apt-get install libcanberra-gtk*
    sudo apt-get install libatlas-base-dev gfortran
    sudo apt-get install python3-dev

 
 b. Download OpenCV 4

    cd ~
    wget -O opencv.zip https://github.com/opencv/opencv/archive/4.3.0.zip
    wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.3.0.zip
    unzip opencv.zip
    unzip opencv_contrib.zip
    mv opencv-4.0.0 opencv
    mv opencv_contrib-4.0.0 opencv_contrib

 
 c. Install Numpy

    pip install numpy

 
 d. CMake and compile OpenCV 4

    cd ~/opencv
    mkdir build
    cd build
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
       -D CMAKE_INSTALL_PREFIX=/usr/local \
       -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
       -D ENABLE_NEON=ON \
       -D ENABLE_VFPV3=ON \
       -D BUILD_TESTS=OFF \
       -D OPENCV_ENABLE_NONFREE=ON \
       -D INSTALL_PYTHON_EXAMPLES=OFF \
       -D BUILD_EXAMPLES=OFF ..
    make -j4


    sudo make install
    sudo ldconfig


Now, you have successfully installed OpenCV 4.0 on your Raspberry Pi. 
 

 
## Setting up the environment:

Now, we will clone the repository from github. But before this make sure that you have git installed locally in your system.

 

Step 1. Clone the repository using the git clone and then open the directory.

    git clone https://github.com/Shikhar-SRJ/rpi_based_mask_detector_new.git
    cd rpi_based_mask_detector 

 

Step 2. Install the project requirements using pip3.

    pip3 install -r requirements.txt

 

Step 3. Run the project.

    flask run --host=0.0.0.0

 

Step 4. Accessing the application through browser by serarching "<ip address of your raspberry pi>:5000". For example:

    192.168.42.101:5000



## CNN Model

The model is already built and saved in "tf_lite" directory.

The [notebooks](https://github.com/Shikhar-SRJ/face_mask_detection_model.git) are also available in case someone wants to use a new dataset or increase the model accuracy.

For dataset [click here](https://drive.google.com/drive/folders/1e6cSXUrhGrYAv6FbLCFM627BPnFXYz4G?usp=sharing)
