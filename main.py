#!/usr/bin/env python3


import cv2
import io
import numpy as np
from os import remove
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image

ref = [[0] * 9 for i in range(9)]

url = "Website url"

def predict_digit(img):
    #### LOAD TRAINED MODEL ####
    samples = np.loadtxt("IA/generalsamples.data", np.float32)
    responses = np.loadtxt("IA/generalresponses.data", np.float32)
    responses = responses.reshape((responses.size, 1))

    model = cv2.ml.KNearest_create()
    model.train(samples, cv2.ml.ROW_SAMPLE, responses)
    ##########################

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, 1, 1, 11, 2)
    nbr = 0;
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt) > 50:
            [x, y, w, h] = cv2.boundingRect(cnt)
            if  h > 28:
                cv2.rectangle(img, (x, y), (x + w, y + h),(0, 255, 0), 2)
                roi = thresh[y:y + h, x:x + w]
                roismall = cv2.resize(roi,(10,10))
                roismall = roismall.reshape((1,100))
                roismall = np.float32(roismall)
                retval, results, neigh_resp, dists = model.findNearest(roismall, k = 1)
                nbr = int((results[0][0]))
    return nbr;

def main():
    # Code here 
    return 0


main()
