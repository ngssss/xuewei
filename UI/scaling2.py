from aip import AipBodyAnalysis
import cv2
import utils.getPoints
import utils.getAngel
import math
from PIL import Image, ImageDraw, ImageFont
import numpy as np

body_parts1 = ''

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
    APP_ID = '24022985'
    API_KEY = 'HhqTlx9D4p9etNR2qFMxsEGr'
    SECRET_KEY = 'wETvF3lhV20MDa2GxlUk0klGMHgGbHZo'
    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

    print("关键点识别中")
    # 读取图像数据
    image1 = get_file_content(path1)
    image2 = get_file_content(path2)

    # 把接口返回数据存入字典
    dic1 = client.bodyAnalysis(image1)
    global body_parts1
    body_parts1 = dic1['person_info'][0]['body_parts']
    print(dic1)

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
    ratio2 = (left2 - right2) / (left1 - right1)

    # 按照比例的对测试图的穴位坐标进行缩放
    test_head_point = head_point = utils.getPoints.head_point('D:/MyStudy/gp_picture/4.jpg')
    test_body_list = body_list = utils.getPoints.body_point('D:/MyStudy/gp_picture/4.jpg')
    test_big_arm_point = big_arm_point = utils.getPoints.big_arm_list('D:/MyStudy/gp_picture/4.jpg')
    test_small_arm_point = big_arm_point = utils.getPoints.small_arm_point('D:/MyStudy/gp_picture/4.jpg')
    test_hand_point = hand_point = utils.getPoints.hand_point('D:/MyStudy/gp_picture/4.jpg')
    test_leg_point = leg_point = utils.getPoints.leg_point('D:/MyStudy/gp_picture/4.jpg')
    test_foot_point = foot_point = utils.getPoints.foot_point('D:/MyStudy/gp_picture/4.jpg')

    body_parts1['top_head']['x'] *= ratio2
    body_parts1['top_head']['y'] *= ratio2

    diff1 = top2 - body_parts1['top_head']['y']
    diff2 = body_parts2['top_head']['x'] - body_parts1['top_head']['x']

    for key, value in test_head_point.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_body_list.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_leg_point.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_foot_point.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_hand_point.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_big_arm_point.items():
        value['x'] = ratio2 * value['x'] + diff2
        value['y'] = ratio1 * value['y'] + diff1
    for key, value in test_small_arm_point.items():
        value['x'] = ratio2 * value['x'] + diff2
        value['y'] = ratio1 * value['y'] + diff1

    list_x_y = []
    for key, value in test_head_point.items():
        list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_body_list.items():
        list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_leg_point.items():
        list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_foot_point.items():
        list_x_y.append((int(value['x']), int(value['y'])))
    # for key, value in test_arm_point.items():
    #     list_x_y.append((int(value['x']), int(value['y'])))
    # for key, value in test_hand_point.items():
    #     list_x_y.append((int(value['x']), int(value['y'])))

    qx = test_big_arm_point['曲泽']['x']
    qy = test_big_arm_point['曲泽']['y']
    a = body_parts2['left_elbow']['x'] - qx
    b = body_parts2['left_elbow']['y'] - qy
    for key, value in test_big_arm_point.items():
        value['x'] += a
        value['y'] += b
        # list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_small_arm_point.items():
        value['x'] += a
        value['y'] += b
        # list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_hand_point.items():
        value['x'] += a
        value['y'] += b
        # list_x_y.append((int(value['x']), int(value['y'])))

    point11 = int(body_parts2['left_elbow']['x'])
    point12 = int(body_parts2['left_elbow']['y'])

    point21 = int(body_parts2['left_wrist']['x'])
    point22 = int(body_parts2['left_wrist']['y'])

    point31 = int(test_hand_point['劳宫']['x'])
    point32 = int(test_hand_point['劳宫']['y'])

    point41 = int(test_big_arm_point['肩胛']['x'])
    point42 = int(test_big_arm_point['肩胛']['y'])

    point51 = int(body_parts2['left_shoulder']['x'])
    point52 = int(body_parts2['left_shoulder']['y'])

    # 得到两直线之间的角度
    line1 = Line(Point(point51, point52), Point(point11, point12))
    line2 = Line(Point(point41, point42), Point(point11, point12))
    res1 = utils.getAngel.GetAngle(line2, line1) - 5

    line3 = Line(Point(point11, point12), Point(point21, point22))
    line4 = Line(Point(point11, point12), Point(point31, point32))
    res2 = utils.getAngel.GetAngle(line3, line4) - 5

    res1 = math.radians(res1)
    res2 = math.radians(res2)
    for key, value in test_big_arm_point.items():
        value['x'] = (value['x'] - point11) * math.cos(res1) + (value['y'] - point12) * math.sin(res1) + point11
        value['y'] = (value['y'] - point12) * math.cos(res1) - (value['x'] - point11) * math.sin(res1) + point12
        list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_hand_point.items():
        value['x'] = (value['x'] - point11) * math.cos(res2) + (value['y'] - point12) * math.sin(res2) + point11
        value['y'] = (value['y'] - point12) * math.cos(res2) - (value['x'] - point11) * math.sin(res2) + point12
        list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_small_arm_point.items():
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

    for key, value in test_head_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_body_list.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_big_arm_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_small_arm_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_leg_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_foot_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_hand_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)

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
    ratio2 = (right2 - left2) / (left1 - right1)

    # 按照比例的对测试图的穴位坐标进行缩放
    test_head_point = utils.getPoints.back_head_point('D:/MyStudy/gp_picture/5.jpg')
    test_body_list = utils.getPoints.back_body_point('D:/MyStudy/gp_picture/5.jpg')
    test_big_arm_point = utils.getPoints.back_big_arm_point('D:/MyStudy/gp_picture/5.jpg')
    test_small_hand_arm_point = utils.getPoints.back_small_arm_hand_point('D:/MyStudy/gp_picture/5.jpg')
    test_leg_foot_point = utils.getPoints.back_leg_foot_point('D:/MyStudy/gp_picture/5.jpg')
    body_parts1['neck']['x'] *= ratio2
    body_parts1['neck']['y'] *= ratio2

    diff1 = body_parts2['neck']['y'] - body_parts1['neck']['y']
    diff2 = body_parts2['neck']['x'] - body_parts1['neck']['x']

    for key, value in test_head_point.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_body_list.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_leg_foot_point.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_small_hand_arm_point.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2
    for key, value in test_big_arm_point.items():
        value['y'] = ratio1 * value['y'] + diff1
        value['x'] = ratio2 * value['x'] + diff2

    list_x_y = []
    for key, value in test_head_point.items():
        list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_body_list.items():
        list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_leg_foot_point.items():
        list_x_y.append((int(value['x']), int(value['y'])))
    # for key, value in test_small_hand_arm_point.items():
    #     list_x_y.append((int(value['x']), int(value['y'])))
    # for key, value in test_arm_point.items():
    #      list_x_y.append((int(value['x']), int(value['y'])))
    # for key, value in test_hand_point.items():
    #      list_x_y.append((int(value['x']), int(value['y'])))

    a = body_parts2['right_elbow']['x'] - test_big_arm_point['天井']['x']
    b = body_parts2['right_elbow']['y'] - test_big_arm_point['天井']['y']
    for key, value in test_big_arm_point.items():
        value['x'] += a
        value['y'] += b
        # list_x_y.append((int(value['x']), int(value['y'])))
    for key, value in test_small_hand_arm_point.items():
        value['x'] += a
        value['y'] += b
        # list_x_y.append((int(value['x']), int(value['y'])))

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
    res1 = utils.getAngel.GetAngle(line2, line1) + 5

    line3 = Line(Point(point11, point12), Point(point21, point22))
    line4 = Line(Point(point11, point12), Point(point31, point32))
    res2 = utils.getAngel.GetAngle(line3, line4) - 10

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

    for key, value in test_head_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_big_arm_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_body_list.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_small_hand_arm_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)
    for key, value in test_leg_foot_point.items():
        img = cv2AddChineseText(img, key, (int(value['x']), int(value['y'])), (0, 255, 0), 30)
        cv2.circle(img, (int(value['x']), int(value['y'])), radius=5, color=(0, 255, 0), thickness=5)

    cv2.imwrite('tomarkB.png', img)


"""
    主函数入口
"""


def scale(imageZ, imageB):
    # 数据路径
    path1 = 'D:/MyStudy/1.png'  # 标准背面图路径
    path2 = 'D:/MyStudy/2.jpg'  # 标准背面图路径

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
