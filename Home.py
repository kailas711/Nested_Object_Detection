"""This is the main file of the project that contains the streamlit app
   This file defines the layout of the application which includes the 
   image uploader , video uploader , an interface etc"""

import streamlit as st

# Setting page layout
st.set_page_config(
    page_title="Object Detection using YOLOv8",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Main page heading
content = """ # YoloV8_Nested_Object_Detection
My first end-to-end computer vision project, starting from data collection to deployment in a webapp.
The project involves 5 steps 
- Data Collection 
- Data cleaning and procesing 
- Model Buidling and training 
- Deployment 

### 1.Data Collection 
I utilized the Selenium library in Python for automating web scraping. The scraping process posed challenges due to frequent Chrome updates that hindered traditional methods. The most demanding aspect involved configuring the chromedriver to navigate through thumbnails and identify the image source to prevent downloading of the thumbnails.

[Code for scrapping](https://github.com/kailas711/YoloV5_Nested_Object_Detection/blob/main/Data_Collection.py)


![Data_collection](https://github.com/kailas711/YoloV5_Nested_Object_Detection/assets/89206677/21f41239-620c-4706-ac3b-db86154de4cb)



### 2.Data Cleannig and Processing
Around 175 images were carefully selected and manually inspected. To ensure consistent input dimensions for the YOLO model, resizing was performed on all images. Roboflow was utilized to manually draw bounding boxes. Additionally, image augmentation techniques were employed to expand the training dataset, enhancing the model's learning capabilities.

![Annotation](https://github.com/kailas711/YoloV5_Nested_Object_Detection/assets/89206677/2257ed62-02ab-4a8b-8f04-a9553b00e2b4)


### 3.Model Buidling and training
The Ultralytics YoloV8 nano model custom trained on dataset via Roboflow API dairectly on T4 GPU in Google Colab.

[YoloV8n model](https://github.com/kailas711/YoloV5_Nested_Object_Detection/blob/main/YoloV8%20Training.ipynb)


### 4.Deployment 
"![image](https://learn.g2.com/hubfs/G2CM_FI264_Learn_Article_Images_%5BObject_detection%5D_V1a.png)"
"""

st.markdown(content)