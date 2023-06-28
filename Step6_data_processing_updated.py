#!/usr/bin/env python
# coding: utf-8


import os
import cv2 as cv2
import numpy as np
import math
import mediapipe as mp

#hand detector tool
class HandDetector:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.7, minTrackCon=0.1):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.minTrackCon,
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img, draw=True):
        img_bone = np.ones((img.shape[0], img.shape[1], 3)) * 255
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_RGB)
        all_hands = []
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(
                self.results.multi_handedness, self.results.multi_hand_landmarks
            ):
                # if handType == 'Right':
                myHand = {}
                # lmList
                mylmList = []
                xList = []
                yList = []
                zList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py, pz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                    mylmList.append([px, py, pz])
                    xList.append(px)
                    yList.append(py)
                    zList.append(pz)
                # bbox
                x_min, x_max = min(xList), max(xList)
                y_min, y_max = min(yList), max(yList)
                boxW, boxH = x_max - x_min, y_max - y_min
                bbox = x_min, y_min, boxW, boxH

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["xList"] = xList
                myHand["yList"] = yList
                myHand["zList"] = zList
                all_hands.append(myHand)
                # draw
                if draw:
                    self.mpDraw.draw_landmarks(
                        img_bone, handLms, self.mpHands.HAND_CONNECTIONS
                    )
        if draw:
            return all_hands, img_bone
        else:
            return all_hands

#setup directory
folder_hand_path = "tempClassMay1"
output_folder_hand_path = "ClassImageMay1"
output_folder_bone_path = "ClassBoneMay1"
output_folder_point_path = "ClassPointMay1"
done_folder_path = "done"


for folder in os.listdir(folder_hand_path):
    # Create path
    child_folder_hand_path = os.path.join(folder_hand_path, folder)
    child_output_folder_hand_path = os.path.join(output_folder_hand_path, folder)
    child_output_folder_bone_path = os.path.join(output_folder_bone_path, folder)
    child_output_folder_point_path = os.path.join(output_folder_point_path, folder)

    # Read file
    for file_video in os.listdir(child_folder_hand_path):
        video_hand_path = os.path.join(child_folder_hand_path, file_video)
        print(file_video)
        file_name = file_video.rstrip(".mp4")
        cap = cv2.VideoCapture(video_hand_path)
        frame_total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(frame_total)
        detector = HandDetector(maxHands=2)
        offset = 40
        img_size = 300
        count = 0
        while count < (frame_total - 10):
            ret, frame = cap.read()
            if frame is not None:
                # frame = cv2.resize(frame, (frame.shape[0] * 2, frame.shape[1] * 2))
                img = frame
                try:
                    hands, img_bone = detector.findHands(img)
                except AttributeError:
                    pass
                if hands:
                    hand = hands[0]
                    try:
                        # output points
                        lm_list = hand["lmList"]
                        
                        x_list = hand["xList"]
                        y_list = hand["yList"]
                        z_list = hand["zList"]
                        x_min = min(x_list)
                        x_max = max(x_list)
                        y_min = min(y_list)
                        y_max = max(y_list)
                        z_min = min(z_list)
                        z_max = max(z_list)

                        lm_list = np.array(lm_list)
                        print (lm_list)
                        lm_list_normalize = []
                        for lm in lm_list:
                            lm = [
                                round((lm[0] - x_min) / (x_max - x_min), 2),
                                round((lm[1] - y_min) / (y_max - y_min), 2),
                                round(lm[2] / (z_max - z_min), 2),
                            ]
                            lm_list_normalize.append(lm)
                        
                        output_point_name = file_name + "_" + str(count) + ".txt"
                        output_point_path = os.path.join(
                            child_output_folder_point_path, output_point_name
                        )
                        # print(output_point_path)
                        np.savetxt(output_point_path, lm_list_normalize, fmt="%.2f")

                        # output hand
                        # print(hand["bbox"])
                        x, y, w, h = hand["bbox"]
                        # print(x, y, w, h)

                        if h >= w:
                            img_hand_crop = frame[
                                y - offset : y + h + offset, x - offset : x + h + offset
                            ]
                        else:
                            img_hand_crop = frame[
                                y - offset : y + w + offset, x - offset : x + w + offset
                            ]

                        img_hand_resize = cv2.resize(
                            img_hand_crop, [img_size, img_size]
                        )
                        output_hand_name = file_name + "_" + str(count) + ".jpg"
                        output_hand_path = os.path.join(
                            child_output_folder_hand_path, output_hand_name
                        )
                        cv2.imwrite(output_hand_path, img_hand_resize)

                        # output bone
                        img_bone_crop = img_bone[
                            y - offset : y + h + offset, x - offset : x + w + offset
                        ]
                        img_white = np.ones((img_size, img_size, 3), np.uint8) * 255

                        aspectRatio = h / w
                        if aspectRatio > 1:
                            k = img_size / h
                            wCal = math.ceil(k * w)
                            img_bone_resize = cv2.resize(
                                img_bone_crop, (wCal, img_size)
                            )
                            wGap = math.ceil((img_size - wCal) / 2)
                            img_white[:, wGap : wCal + wGap] = img_bone_resize
                        else:
                            k = img_size / w
                            hCal = math.ceil(k * h)
                            img_bone_resize = cv2.resize(
                                img_bone_crop, (img_size, hCal)
                            )
                            hGap = math.ceil((img_size - hCal) / 2)
                            img_white[hGap : hCal + hGap, :] = img_bone_resize
                        output_bone_name = file_name + "_" + str(count) + ".jpg"
                        output_bone_path = os.path.join(
                            child_output_folder_bone_path, output_bone_name
                        )
                        cv2.imwrite(output_bone_path, img_white)

                        print(count)
                        count += 1
                        # cv2.imshow("ImageHand", img_hand_resize)
                        # cv2.imshow("ImageBone", img_white)
                        # key = cv2.waitKey(1)
                        # cv2.imshow("test", img_white)
                        # cv2.imshow("img_white", img_hand_resize)
                        # cv2.waitKey(1)
                    except ValueError:
                        pass
        cap.release()
        print("done " + file_video)
