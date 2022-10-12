# Smart Surveillance Camera
A project for NUS ESP3902 by Group 1


## Run instruction

### Go to the project directory
```sh
cd esp3902-group-1
```

### Create virtual environment
```sh
python3 -m venv env
```

### Activate virtual environment
#### MacOS/Linux
```sh
source env/bin/activate
```
#### Windows
```sh
env/Scripts/activate
```

### Install the required packages
```sh
pip3 install -r requirements.txt
```

### Run inference
```sh
python3 src/main/main.py
```
When running on live video, press 'q' or do a KeyboardInterrupt to stop the video stream

## References
- https://docs.ultralytics.com/
- https://towardsdatascience.com/how-i-built-a-face-mask-detector-for-covid-19-using-pytorch-lightning-67eb3752fd61
- https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset