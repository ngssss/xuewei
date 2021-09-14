from aip import AipBodyAnalysis
import cv2
import utils.getPoints
import utils.getAngel
import math
from PIL import Image, ImageDraw, ImageFont
import numpy as np

body_parts1 = ''
body_parts2 = ''

flag = ""


class Point:
    """
    2D坐标点
    """

    def __init__(self, x, y):
        self.X = x
        self.Y = y


class Line:
    def __init__(self, point1, point2):
        """
        初始化包含两个端点
        :param point1:
        :param point2:
        """
        self.Point1 = point1
        self.Point2 = point2


"""
    读取数据
"""


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


"""
    人体特征点识别
"""


def feature_point_recognition(path1, path2):
    # 接口相关数据
    # APP_ID = '24022985'
    # API_KEY = 'HhqTlx9D4p9etNR2qFMxsEGr'
    # SECRET_KEY = 'wETvF3lhV20MDa2GxlUk0klGMHgGbHZo'
    APP_ID = '24836918'
    API_KEY = 'YVcnRdb92tAfhZOx0g2vXUAF'
    SECRET_KEY = 'EvWlKWXtnsgvWDcCIYAFFfuez9nOsKAz'
    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

    print("关键点识别中")
    # 读取图像数据
    image1 = get_file_content(path1)
    image2 = get_file_content(path2)

    # 把接口返回数据存入字典
    global body_parts1
    dic1 = client.bodyAnalysis(image1)
    body_parts1 = dic1['person_info'][0]['body_parts']
    print(dic1)

    global body_parts2
    dic2 = client.bodyAnalysis(image2)
    body_parts2 = dic2['person_info'][0]['body_parts']
    print(dic2)

    # list_x_y = []
    # for key, value in body_parts2.items():
    #     list_x_y.append((int(value['x']), int(value['y'])))
    # img = cv2.imread(path2, cv2.IMREAD_COLOR)
    # for i in range(len(list_x_y)):
    #     cv2.circle(img, center=list_x_y[i], radius=5, color=(0, 255, 0), thickness=5)
    # cv2.imwrite('../Scale/body.png', img)
    return body_parts1, body_parts2


"""
    人体正面穴位识别
"""


def scaleZ(path, body_parts1, body_parts2):
    # 得到 标准图 和 测试图 的高点和低点的长度，计算一个比例
    top1 = body_parts1['top_head']['y']
    low1 = body_parts1['right_ankle']['y']
    top2 = body_parts2['top_head']['y']
    low2 = body_parts2['right_ankle']['y']

    left1 = body_parts1['left_shoulder']['x']
    right1 = body_parts1['right_shoulder']['x']
    left2 = body_parts2['left_shoulder']['x']
    right2 = body_parts2['right_shoulder']['x']

    ratio1 = (top2 - low2) / (top1 - low1)
    print("高低比例： ", ratio1)
    ratio2 = (left2 - right2) / (left1 - right1)
    print("长宽比例: ", ratio2)

    # 按照比例的对测试图的穴位坐标进行缩放
    test_head_point = head_point = utils.getPoints.head_point("need_a_img")
    test_body_list = body_list = utils.getPoints.body_point("need_a_img")
    test_big_arm_point = big_arm_point = utils.getPoints.big_arm_list("need_a_img")
    test_small_arm_point = big_arm_point = utils.getPoints.small_arm_point("need_a_img")
    test_hand_point = hand_point = utils.getPoints.hand_point("need_a_img")
    test_leg_point = leg_point = utils.getPoints.leg_point("need_a_img")
    test_foot_point = foot_point = utils.getPoints.foot_point("need_a_img")

    body_parts1['top_head']['x'] *= ratio2
    body_parts1['top_head']['y'] *= ratio2

    diff1 = top2 - body_parts1['top_head']['y'] + 15
    diff2 = body_parts2['top_head']['x'] - body_parts1['top_head']['x']

    man_point1 = [test_head_point,test_body_list,test_big_arm_point,test_small_arm_point,test_hand_point,test_leg_point,test_foot_point]
    for each in man_point1:
        for key, value in each.items():
            value['y'] = ratio1 * value['y'] + diff1
            value['x'] = ratio2 * value['x'] + diff2

    man_point2 = [test_head_point, test_body_list, test_leg_point, test_foot_point]
    list_x_y = []
    for each in man_point2:
        for key, value in each.items():
            list_x_y.append((int(value['x']), int(value['y'])))

    qx = test_big_arm_point['曲泽']['x']
    qy = test_big_arm_point['曲泽']['y']
    a = body_parts2['left_elbow']['x'] - qx
    b = body_parts2['left_elbow']['y'] - qy

    man_point3 = [test_big_arm_point, test_small_arm_point, test_hand_point]
    for each in man_point3:
        for key, value in each.items():
            value['x'] += a
            value['y'] += b

    point11 = int(body_parts2['left_elbow']['x'])  # 获取左肘的坐标
    point12 = int(body_parts2['left_elbow']['y'])

    point21 = int(body_parts2['left_wrist']['x'])  # 获取左手腕的坐标
    point22 = int(body_parts2['left_wrist']['y'])

    point51 = int(body_parts2['left_shoulder']['x'])  # 获取左肩的坐标
    point52 = int(body_parts2['left_shoulder']['y'])

    point31 = int(test_hand_point['劳宫']['x'])  # 手掌心的穴位坐标
    point32 = int(test_hand_point['劳宫']['y'])

    point41 = int(test_big_arm_point['肩胛']['x'])  # 肩膀的穴位坐标
    point42 = int(test_big_arm_point['肩胛']['y'])

    # 得到两直线之间的角度
    line1 = Line(Point(point51, point52), Point(point11, point12))
    line2 = Line(Point(point41, point42), Point(point11, point12))
    res1 = utils.getAngel.GetAngle(line2, line1) - 5

    line3 = Line(Point(point11, point12), Point(point21, point22))
    line4 = Line(Point(point11, point12), Point(point31, point32))
    res2 = utils.getAngel.GetAngle(line3, line4)
    # 获取的是角度
    print("res1: ", res1)
    print("res2: ", res2)
    res1 = math.radians(res1)
    res2 = math.radians(res2)
    # 转换成弧度
    print("res1: ", res1)
    print("res2: ", res2)

    man_point4 = [test_big_arm_point, test_hand_point, test_small_arm_point]

    for index, each in enumerate(man_point4):
        if index == 0:
            for key, value in each.items():
                value['x'] = (value['x'] - point11) * math.cos(res1) + (value['y'] - point12) * math.sin(res1) + point11
                value['y'] = (value['y'] - point12) * math.cos(res1) - (value['x'] - point11) * math.sin(res1) + point12
                list_x_y.append((int(value['x']), int(value['y'])))
        else:
            for key, value in each.items():
                value['x'] = (value['x'] - point11) * math.cos(res2) + (value['y'] - point12) * math.sin(res2) + point11
                value['y'] = (value['y'] - point12) * math.cos(res2) - (value['x'] - point11) * math.sin(res2) + point12
                list_x_y.append((int(value['x']), int(value['y'])))

    # 肩胛 坐标
    test_big_arm_point["肩胛"]["x"] = (int(test_big_arm_point["肩胛"]["x"])+int(test_body_list["肩胛"]["x"]))/2
    test_big_arm_point["肩胛"]["y"] = (int(test_big_arm_point["肩胛"]["y"])+int(test_body_list["肩胛"]["y"]))/2
    print(test_big_arm_point)
    del(test_body_list["肩胛"])

    img = cv2.imread(path, cv2.IMREAD_COLOR)

    def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=15):
        if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # 创建一个可以在给定图像上绘图的对象
        draw = ImageDraw.Draw(img)
        # 字体的格式
        fontStyle = ImageFont.truetype(
            "simsun.ttc", textSize, encoding="utf-8")
        # 绘制文本
        draw.text(position, text, textColor, font=fontStyle)
        # 转换回OpenCV格式
        return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

    for each in man_point1:
        for key, value in each.items():
            img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 15)
            cv2.circle(img, (int(value['x']), int(value['y'])), radius=2, color=(0, 0, 255), thickness=1)

    cv2.imwrite('tomarkZ.png', img)


"""
    人体背面穴位识别
"""


def scaleB(path, body_parts1, body_parts2):
    # 得到 标准图 和 测试图 的高点和低点的长度，计算一个比例
    top1 = body_parts1['top_head']['y']
    low1 = body_parts1['left_ankle']['y']
    top2 = body_parts2['top_head']['y']
    low2 = body_parts2['left_ankle']['y']

    left1 = body_parts1['left_shoulder']['x']
    right1 = body_parts1['right_shoulder']['x']
    left2 = body_parts2['left_shoulder']['x']
    right2 = body_parts2['right_shoulder']['x']

    ratio1 = (top2 - low2) / (top1 - low1)
    ratio2 = (left2 - right2) / (left1 - right1)

    # 按照比例的对测试图的穴位坐标进行缩放
    test_head_point = utils.getPoints.back_head_point('need_pic')
    test_body_list = utils.getPoints.back_body_point('need_pic')
    test_big_arm_point = utils.getPoints.back_big_arm_point('need_pic')
    test_small_hand_arm_point = utils.getPoints.back_small_arm_hand_point('need_pic')
    test_leg_foot_point = utils.getPoints.back_leg_foot_point('need_pic')
    body_parts1['neck']['x'] *= ratio2
    body_parts1['neck']['y'] *= ratio2

    diff1 = body_parts2['neck']['y'] - body_parts1['neck']['y'] - 32
    diff2 = body_parts2['neck']['x'] - body_parts1['neck']['x']

    man_back_point1 = [test_head_point, test_body_list, test_big_arm_point, test_small_hand_arm_point, test_leg_foot_point]
    for each in man_back_point1:
        for key, value in each.items():
            value['y'] = ratio1 * value['y'] + diff1
            value['x'] = ratio2 * value['x'] + diff2

    list_x_y = []
    man_back_point2 = [test_head_point, test_body_list, test_leg_foot_point]
    for each in man_back_point2:
        for key, value in each.items():
            list_x_y.append((int(value['x']), int(value['y'])))


    a = body_parts2['right_elbow']['x'] - test_big_arm_point['天井']['x']
    b = body_parts2['right_elbow']['y'] - test_big_arm_point['天井']['y']
    man_back_point3 = [test_big_arm_point, test_small_hand_arm_point]
    for each in man_back_point3:
        for key, value in each.items():
            value['x'] += a
            value['y'] += b


    point11 = int(body_parts2['right_elbow']['x'])
    point12 = int(body_parts2['right_elbow']['y'])

    point21 = int(body_parts2['right_wrist']['x'])
    point22 = int(body_parts2['right_wrist']['y'])

    point31 = int(test_small_hand_arm_point['中褚']['x'])
    point32 = int(test_small_hand_arm_point['中褚']['y'])

    point41 = int(test_body_list['肩髎']['x'])
    point42 = int(test_body_list['肩髎']['y'])

    point51 = int(body_parts2['right_shoulder']['x'])
    point52 = int(body_parts2['right_shoulder']['y'])

    # 得到两直线之间的角度
    line1 = Line(Point(point51, point52), Point(point11, point12))
    line2 = Line(Point(point41, point42), Point(point11, point12))
    res1 = utils.getAngel.GetAngle(line2, line1) + 22

    line3 = Line(Point(point11, point12), Point(point21, point22))
    line4 = Line(Point(point11, point12), Point(point31, point32))
    res2 = utils.getAngel.GetAngle(line3, line4) - 8

    res1 = math.radians(res1)
    res2 = math.radians(res2)

    for key, value in test_big_arm_point.items():
        value['x'] = (value['x'] - point11) * math.cos(res1) + (value['y'] - point12) * math.sin(res1) + point11
        value['y'] = (value['y'] - point12) * math.cos(res1) - (value['x'] - point11) * math.sin(res1) + point12
        list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_small_hand_arm_point.items():
        value['x'] = (value['x'] - point11) * math.cos(res2) + (value['y'] - point12) * math.sin(res2) + point11
        value['y'] = (value['y'] - point12) * math.cos(res2) - (value['x'] - point11) * math.sin(res2) + point12
        list_x_y.append((int(value['x']), int(value['y'])))


    img = cv2.imread(path, cv2.IMREAD_COLOR)

    def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
        if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # 创建一个可以在给定图像上绘图的对象
        draw = ImageDraw.Draw(img)
        # 字体的格式
        fontStyle = ImageFont.truetype(
            "simsun.ttc", textSize, encoding="utf-8")
        # 绘制文本
        draw.text(position, text, textColor, font=fontStyle)
        # 转换回OpenCV格式
        return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

    for each in man_back_point1:
        for key, value in each.items():
            img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 15)
            cv2.circle(img, (int(value['x']), int(value['y'])), radius=2, color=(0, 0, 255), thickness=2)

    cv2.imwrite('tomarkB.png', img)


"""
    主函数入口
"""


def scale(imageZ, imageB):
    # 数据路径
    path1 = './1.png'  # 标准背面图路径
    path2 = './2.png'  # 标准背面图路径

    path3 = imageZ  # 标准背面图路径
    path4 = imageB

    print(path1)
    print(path2)
    print(path3)
    print(path4)
    # 特征点识别
    print("穴位识别中")
    body_parts1, body_parts2 = feature_point_recognition(path1, path3)
    print(1, body_parts1)
    print(2, body_parts2)
    body_parts3, body_parts4 = feature_point_recognition(path2, path4)
    print(3, body_parts3)
    print(4, body_parts4)

    scaleZ(path3, body_parts1, body_parts2)
    print("正面识别结束")

    scaleB(path4, body_parts3, body_parts4)
    print("背面识别结束")

    print("穴位识别结束")
    global flag
    flag = 58


if __name__ == '__main__':
    imageZ = './7.jpg'
    imageB = './6.jpg'
    scale(imageZ, imageB)
    """正面测试结果"""
    # dic1 = {'person_num': 1, 'person_info': [{'body_parts': {'nose': {'score': 0.8655760884284973, 'x': 237.2900390625, 'y': 88.2822265625}, 'right_knee': {'score': 0.8212782740592957, 'x': 196.3232421875, 'y': 612.6572265625}, 'left_hip': {'score': 0.8003217577934265, 'x': 261.8701171875, 'y': 432.4033203125}, 'right_ankle': {'score': 0.8505286574363708, 'x': 204.5166015625, 'y': 776.5244140625}, 'right_wrist': {'score': 0.9192712903022766, 'x': 81.6162109375, 'y': 440.5966796875}, 'left_eye': {'score': 0.885526716709137, 'x': 245.4833984375, 'y': 71.8955078125}, 'left_mouth_corner': {'score': 0.9034730792045593, 'x': 245.4833984375, 'y': 112.8623046875}, 'right_elbow': {'score': 0.87157142162323, 'x': 114.3896484375, 'y': 325.8896484375}, 'left_knee': {'score': 0.8086779713630676, 'x': 253.6767578125, 'y': 612.6572265625}, 'neck': {'score': 0.8903869390487671, 'x': 220.9033203125, 'y': 145.6357421875}, 'top_head': {'score': 0.8872942328453064, 'x': 220.9033203125, 'y': 30.9287109375}, 'right_ear': {'score': 0.8708834648132324, 'x': 188.1298828125, 'y': 88.2822265625}, 'left_ear': {'score': 0.8469434976577759, 'x': 261.8701171875, 'y': 88.2822265625}, 'left_elbow': {'score': 0.8557606935501099, 'x': 327.4169921875, 'y': 325.8896484375}, 'right_shoulder': {'score': 0.8743875026702881, 'x': 138.9697265625, 'y': 186.6025390625}, 'right_eye': {'score': 0.8685464859008789, 'x': 212.7099609375, 'y': 71.8955078125}, 'right_mouth_corner': {'score': 0.8905836939811707, 'x': 220.9033203125, 'y': 112.8623046875}, 'left_ankle': {'score': 0.8045106530189514, 'x': 245.4833984375, 'y': 776.5244140625}, 'right_hip': {'score': 0.8069294691085815, 'x': 179.9365234375, 'y': 432.4033203125}, 'left_wrist': {'score': 0.7986640930175781, 'x': 368.3837890625, 'y': 432.4033203125}, 'left_shoulder': {'score': 0.8709250092506409, 'x': 311.0302734375, 'y': 186.6025390625}}, 'location': {'score': 0.9950040578842163, 'top': 17.85858154296875, 'left': 26.26214599609375, 'width': 398.0912780761719, 'height': 838.8831176757812}}], 'log_id': 1435568745125275505}
    # body_parts1 = dic1['person_info'][0]['body_parts']
    # dic2 = {'person_num': 1, 'person_info': [{'body_parts': {'nose': {'score': 0.8856082558631897, 'x': 755.4521484375, 'y': 309.5283203125}, 'right_knee': {'score': 0.8566831946372986, 'x': 646.8779296875, 'y': 1449.5576171875}, 'left_hip': {'score': 0.8207518458366394, 'x': 827.8349609375, 'y': 1105.7392578125}, 'right_ankle': {'score': 0.876239001750946, 'x': 664.9736328125, 'y': 1757.1845703125}, 'right_wrist': {'score': 0.8530470728874207, 'x': 321.1552734375, 'y': 979.0693359375}, 'left_eye': {'score': 0.8798708915710449, 'x': 791.6435546875, 'y': 273.3369140625}, 'left_mouth_corner': {'score': 0.8748537302017212, 'x': 773.5478515625, 'y': 345.7197265625}, 'right_elbow': {'score': 0.8569175004959106, 'x': 484.0166015625, 'y': 852.3994140625}, 'left_knee': {'score': 0.8377569317817688, 'x': 827.8349609375, 'y': 1449.5576171875}, 'neck': {'score': 0.865025520324707, 'x': 755.4521484375, 'y': 472.3896484375}, 'top_head': {'score': 0.8877031803131104, 'x': 755.4521484375, 'y': 182.8583984375}, 'right_ear': {'score': 0.8467347621917725, 'x': 664.9736328125, 'y': 309.5283203125}, 'left_ear': {'score': 0.8470625877380371, 'x': 845.9306640625, 'y': 309.5283203125}, 'left_elbow': {'score': 0.8751459121704102, 'x': 1063.0791015625, 'y': 834.3037109375}, 'right_shoulder': {'score': 0.8708342909812927, 'x': 574.4951171875, 'y': 580.9638671875}, 'right_eye': {'score': 0.8796384334564209, 'x': 719.2607421875, 'y': 273.3369140625}, 'right_mouth_corner': {'score': 0.8779944181442261, 'x': 719.2607421875, 'y': 345.7197265625}, 'left_ankle': {'score': 0.8444924354553223, 'x': 791.6435546875, 'y': 1757.1845703125}, 'right_hip': {'score': 0.824525773525238, 'x': 646.8779296875, 'y': 1105.7392578125}, 'left_wrist': {'score': 0.8552646040916443, 'x': 1207.8447265625, 'y': 979.0693359375}, 'left_shoulder': {'score': 0.8694669008255005, 'x': 918.3134765625, 'y': 562.8681640625}}, 'location': {'score': 0.9980697631835938, 'top': 134.7055053710938, 'left': 149.9456176757812, 'width': 1230.149658203125, 'height': 1852.733642578125}}], 'log_id': 1435568748604622709}
    # body_parts2 = dic2['person_info'][0]['body_parts']
    # print(body_parts1)
    # print(body_parts2)
    # scaleZ(imageZ, body_parts1, body_parts2)

    # """背面测试结果"""
    # dic3 = {'person_num': 1, 'person_info': [{'body_parts': {'nose': {'score': 0.6920953392982483, 'x': 208.7861328125, 'y': 50.00685882568359}, 'right_knee': {'score': 0.7427210807800293, 'x': 223.4150390625, 'y': 540.0751953125}, 'left_hip': {'score': 0.5811174511909485, 'x': 157.5849609375, 'y': 393.7861328125}, 'right_ankle': {'score': 0.8750768899917603, 'x': 216.1005859375, 'y': 693.6787109375}, 'right_wrist': {'score': 0.5540376305580139, 'x': 325.8173828125, 'y': 386.4716796875}, 'left_eye': {'score': 0.6892638206481934, 'x': 208.7861328125, 'y': 42.69240570068359}, 'left_mouth_corner': {'score': 0.695743203163147, 'x': 208.7861328125, 'y': 71.9502182006836}, 'right_elbow': {'score': 0.7317761182785034, 'x': 281.9306640625, 'y': 276.7548828125}, 'left_knee': {'score': 0.7345156669616699, 'x': 172.2138671875, 'y': 547.3896484375}, 'neck': {'score': 0.8440950512886047, 'x': 186.8427734375, 'y': 108.5224761962891}, 'top_head': {'score': 0.8311025500297546, 'x': 186.8427734375, 'y': 20.74904632568359}, 'right_ear': {'score': 0.6954385042190552, 'x': 208.7861328125, 'y': 64.6357650756836}, 'left_ear': {'score': 0.6913790106773376, 'x': 150.2705078125, 'y': 71.9502182006836}, 'left_elbow': {'score': 0.6571182012557983, 'x': 99.06934356689453, 'y': 276.7548828125}, 'right_shoulder': {'score': 0.6907981634140015, 'x': 267.3017578125, 'y': 152.4091949462891}, 'right_eye': {'score': 0.7359294891357422, 'x': 201.4716796875, 'y': 42.69240570068359}, 'right_mouth_corner': {'score': 0.6360546350479126, 'x': 201.4716796875, 'y': 71.9502182006836}, 'left_ankle': {'score': 0.7651001214981079, 'x': 179.5283203125, 'y': 700.9931640625}, 'right_hip': {'score': 0.5954819917678833, 'x': 230.7294921875, 'y': 386.4716796875}, 'left_wrist': {'score': 0.6857736110687256, 'x': 62.49707794189453, 'y': 371.8427734375}, 'left_shoulder': {'score': 0.6294926404953003, 'x': 113.6982498168945, 'y': 159.7236480712891}}, 'location': {'score': 0.9930480718612671, 'top': 1.554443359375, 'left': 4.090606689453125, 'width': 373.7305297851562, 'height': 748.543212890625}}], 'log_id': 1436921679082379913}
    # dic4 = {'person_num': 1, 'person_info': [{'body_parts': {'nose': {'score': 0.708717942237854, 'x': 739.005859375, 'y': 297.208984375}, 'right_knee': {'score': 0.8293030858039856, 'x': 890.705078125, 'y': 1325.392578125}, 'left_hip': {'score': 0.7887223958969116, 'x': 739.005859375, 'y': 988.283203125}, 'right_ankle': {'score': 0.8502972722053528, 'x': 873.849609375, 'y': 1662.501953125}, 'right_wrist': {'score': 0.8664886355400085, 'x': 1261.525390625, 'y': 836.583984375}, 'left_eye': {'score': 0.7517776489257812, 'x': 755.861328125, 'y': 263.498046875}, 'left_mouth_corner': {'score': 0.6446660161018372, 'x': 772.716796875, 'y': 314.064453125}, 'right_elbow': {'score': 0.825346052646637, 'x': 1109.826171875, 'y': 668.029296875}, 'left_knee': {'score': 0.83477383852005, 'x': 755.861328125, 'y': 1342.248046875}, 'neck': {'score': 0.8589598536491394, 'x': 823.283203125, 'y': 364.630859375}, 'top_head': {'score': 0.8543825745582581, 'x': 823.283203125, 'y': 162.365234375}, 'right_ear': {'score': 0.7838075160980225, 'x': 890.705078125, 'y': 280.353515625}, 'left_ear': {'score': 0.8167355060577393, 'x': 755.861328125, 'y': 280.353515625}, 'left_elbow': {'score': 0.8735425472259521, 'x': 503.029296875, 'y': 617.462890625}, 'right_shoulder': {'score': 0.8461540937423706, 'x': 974.982421875, 'y': 465.763671875}, 'right_eye': {'score': 0.6794562935829163, 'x': 755.861328125, 'y': 263.498046875}, 'right_mouth_corner': {'score': 0.6204714775085449, 'x': 755.861328125, 'y': 330.919921875}, 'left_ankle': {'score': 0.8196871280670166, 'x': 755.861328125, 'y': 1696.212890625}, 'right_hip': {'score': 0.7907102704048157, 'x': 907.560546875, 'y': 971.427734375}, 'left_wrist': {'score': 0.8992827534675598, 'x': 334.474609375, 'y': 769.162109375}, 'left_shoulder': {'score': 0.8251355886459351, 'x': 688.439453125, 'y': 448.908203125}}, 'location': {'score': 0.9985887408256531, 'top': 100.6543579101562, 'left': 165.0958251953125, 'width': 1266.116943359375, 'height': 1725.404296875}}], 'log_id': 1436921681501275919}
    # body_parts3 = dic3['person_info'][0]['body_parts']
    # body_parts4 = dic4['person_info'][0]['body_parts']
    # scaleB(imageB, body_parts3, body_parts4)

