# Trackmania Bot

  This bot will play Trackmania (2020 edition) on Windows. 

  To use, run main.py in virtualenv while Trackmania is open in windowed mode. The program will record your WASD keypresses and the screen and store it in data.npy once you close the program by pressing q.

  Data format in data.npy: The dataset is a 2d array. Each 1d array element contains the inputs as the first four integers(w,a,s,d in that order can be 0 for off or 1 for on), then it contains a flattened version of the screenshot. The screenshot is flattened with np.reshape() and is in grayscale