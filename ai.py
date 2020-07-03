import cv2
import shutil
import os

FRAMES_DIR = "./data/frames/"

# Splits video into frames
def FrameCapture(path):
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success:   
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
  
        if (success):
          # Saves the frames with frame-count 
          cv2.imwrite("frame%d.jpg" % count, image) 
  
        count += 1
        
    MoveFrames()

# Moves the frames to the data/frames folder
def MoveFrames():
    print ("Moving the frames into the data folder")
    
    try:
      os.mkdir(FRAMES_DIR)
    except OSError:
      print ("Creation of the directory %s failed" % FRAMES_DIR)
    
    files = os.listdir("./")
    for f in files:
      if (f.startswith("frame")):
        shutil.move(f, FRAMES_DIR)

# Delete all frames
def DeleteAllFrames():
    shutil.rmtree(FRAMES_DIR)

# Driver Code 
if __name__ == '__main__': 
  if (os.path.isdir(FRAMES_DIR)):
    print("Deleting the directory: %s" % FRAMES_DIR)
    DeleteAllFrames()
  else: 
    print("Splitting the video into frames")
    FrameCapture("./data/vids/evo-game2.mp4")

