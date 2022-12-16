import cv2
from urllib import parse
import numpy as np


def get_new(path, ori_path):
    """
    获得图片备份

    参数:
        path: 图片路径 string
        ori_path: 原始图片路径 string
    返回:
        img: 图片
    """
    path = parse.unquote(path)
    ori_path = parse.unquote(ori_path)
    img = cv2.imread(ori_path)
    cv2.imwrite(path, img)
    return img


def trans2jpg(filePath):
    """
    将图片转换为jpg格式

    参数:
        filePath: 图片路径 string
    返回:
        filePath: 图片路径 string
    """
    path = parse.unquote(filePath)
    if (filePath.endswith('.jpg')):
        return filePath
    else:
        img = cv2.imread(path)
        cv2.imwrite(filePath[:-4] + '.jpg', img)
        return filePath[:-4] + '.jpg'


def judge_img_type(img):
    """
    判断图片类型

    参数:
        img: 图片
    返回:
        imgType: 图片类型:rgb/gray string
    """
    if img.ndim == 2:
        return 'gray'
    img0 = img[:, :, 0]
    img1 = img[:, :, 1]
    img2 = img[:, :, 2]
    if (img0 == img1).all() and (img0 == img2).all():
        imgType = 'gray'
    else:
        imgType = 'rgb'
    return imgType


def opera(op, dict):
    """
    操作图片

    参数:
        op: 操作函数名 string op='zoom'
        dict: 参数字典:dict {'Sx':1.5,'Sy':1.5,'filepath':'xxx.jpg'}
        其中dict['filepath']为图片路径

    返回:
        无返回值，直接修改图片
    """
    dict['filepath'] = parse.unquote(dict['filepath'])
    paradict = dict.copy()
    del (paradict['filepath'])
    print('op:', op)
    for i in paradict:
        print(i, paradict[i], type(paradict[i]))
    img = cv2.imread(dict['filepath'])
    imgType = judge_img_type(img)
    if imgType == 'gray':
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out = eval(op)(img, **paradict)
    cv2.imwrite(dict['filepath'], out)


def imageResize(Sx, Sy, filePath):
    """
    图片缩放

    参数:
        Sx: 横向缩放比例 float
        Sy: 纵向缩放比例 float
        filePath: 图片路径 string
    返回:
        无返回值，直接修改图片
    """
    filePath = parse.unquote(filePath)
    img = cv2.imread(filePath)
    x = float(Sx)
    y = float(Sy)
    out = cv2.resize(img, None, fx=x, fy=y, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(filePath, out)


def get_hist_dict(filePath):
    """
    获取图片直方图

    参数:
        filepath: 图片路径
    返回:
        hist_dict: 图片直方图:dict
    """
    filepath = parse.unquote(filePath)
    img = cv2.imread(filepath)
    imgType = judge_img_type(img)
    # cv2是显示bgr的
    hist_dict = {'r': [], 'g': [], 'b': [], 'gray': []}
    if imgType == 'gray':
        hist_dict['gray'] = cv2.calcHist([img], [0], None, [256], [0, 256]).reshape(-1)
    else:
        hist_dict['b'] = cv2.calcHist([img], [0], None, [256], [0, 256]).reshape(-1)
        hist_dict['g'] = cv2.calcHist([img], [1], None, [256], [0, 256]).reshape(-1)
        hist_dict['r'] = cv2.calcHist([img], [2], None, [256], [0, 256]).reshape(-1)
    return hist_dict


def reverse(img):
    """
    图片反色

    参数:
        img: 图片
    返回:
        255-img: 反色图片
    """
    return 255 - img


def log(img, c=1.0):
    """
    对数变换

    参数:
        img: 图片
        c: 参数 float
    返回:
        out: 对数变换后的图片
    """
    out = c * np.log(img + 1.0)
    out = np.uint8(cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX))
    return out


def gamma(img, gamma=2., eps=0.):
    """
    伽马变换
    
    参数:
        img: 图片
        gamma: 参数 float
        eps: 参数 float
    返回:
        out: 伽马变换后的图片
    """
    return 255. * ((img + eps) / 255.) ** gamma


def hist_equal(img):
    """
    直方图均衡化

    参数:
        img: 图片
    返回:
        out: 直方图均衡化后的图片
    """
    if img.ndim == 2:
        return cv2.equalizeHist(img)
    elif img.ndim == 3:
        b = cv2.equalizeHist(img[:, :, 0])
        g = cv2.equalizeHist(img[:, :, 1])
        r = cv2.equalizeHist(img[:, :, 2])
        return cv2.merge([b, g, r])


def gray_three_linear_trans(input, a, b, c=0, d=255):
    """
    灰度三线性变换

    参数:
        input: 图片
        a: 参数 int
        b: 参数 int
        c: 参数 int
        d: 参数 int
    返回:
        out: 灰度三线性变换后的图片
    """
    if a == b or b == 255:
        return None
    # 得到掩码
    m1 = (input < a)
    m2 = (a <= input) & (input <= b)
    m3 = (input > b)

    out = (c / a * input) * m1 \
          + ((d - c) / (b - a) * (input - a) + c) * m2 \
          + ((255 - d) / (255 - b) * (input - b) + d) * m3
    return out


def contrast_stretching(img, m=255., eps=0., E=2.):
    """
    对比度拉伸

    参数:
        img: 图片
        m: 参数 float
        eps: 参数 float
        E: 参数 float
    返回:
        out: 对比度拉伸后的图片
    """
    out = 1. / (1 + (m / (img + eps)) ** E)
    out = np.uint8(cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX))
    return out


def salt_pepper_noise(img, pa, pb):
    """
    椒盐噪声

    参数:
        img: 图片
        pa: 参数 float
        pb: 参数 float
    返回:
        out: 椒盐噪声后的图片
    """
    out = img.copy()
    rows, cols, = img.shape[:2]
    for i in range(rows):
        for j in range(cols):
            if np.random.random() < pa:
                out[i, j] = 0
            elif np.random.random() < pb:
                out[i, j] = 255
    return out


def gaussian_noise(img, mean=0, var=4):
    """
    高斯噪声

    参数:
        img: 图片
        mean: 参数 float
        var: 参数 float
    返回:
        out: 高斯噪声后的图片
    """
    H, W = img.shape[:2]
    out = img.copy()
    # 高斯噪声
    for y in range(H):
        for x in range(W):
            rdn = np.random.randn(1)
            out[y, x] = out[y, x] + rdn * var + mean
    return out



def mean_noise(img, mean=10, var=100):
    """
    均值噪声

    参数:
        img: 图片
        mean: 参数 float
        var: 参数 float
    返回:
        out: 均值噪声后的图片
    """
    a = 2 * mean - np.sqrt(12 * var)
    b = 2 * mean + np.sqrt(12 * var)
    img_noise = np.random.uniform(a, b, img.shape)
    out = img + img_noise
    out_normal = np.uint8(cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX))
    return out_normal


def mean_blur(img, ksize):
    """
    均值滤波

    参数:
        img: 图片
        ksize: 参数 int
    返回:
        out: 均值滤波后的图片
    """
    return cv2.blur(img, (ksize, ksize))


def median_blur(img, ksize):
    """
    中值滤波

    参数:
        img: 图片
        ksize: 参数 int
    返回:
        out: 中值滤波后的图片
    """
    return cv2.medianBlur(img, ksize)


def filter(img, op_name, ksize):
    """
    滤波

    参数:
        img: 图片
        op_name: 参数 str
        ksize: 参数 int
    返回:
        out: 滤波后的图片
    """
    if op_name == 'mean':
        return mean_blur(img, ksize)
    elif op_name == 'median':
        return median_blur(img, ksize)
    else:
        return img


def adaptive_mean(image, m=5, n=None):
    """
    自适应局部降噪

    参数:
        image: 图片
        m: 参数 int
        n: 参数 int
    返回:
        imgAda: 自适应局部降噪后的图片
    """
    eps = 1e-8
    if n == None:
        n = m
    hPad = int((m - 1) / 2)
    wPad = int((n - 1) / 2)
    q = image.ndim
    e = 3
    if q == 2:
        image = image.reshape(image.shape[0], image.shape[1], 1)
        e = 1
    print(q, e, image.shape)
    imgAda = np.zeros(image.shape)
    for k in range(e):
        img = image[:, :, k]
        imgPad = np.pad(img.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), 'edge')
        _, std = cv2.meanStdDev(img)
        var = std ** 2
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                pad = imgPad[i:i + m, j:j + n]
                gxy = img[i, j]
                zSxy = np.mean(pad)
                varSxy = np.var(pad)
                rateVar = min(var / (varSxy + eps), 1.0)
                imgAda[i, j, k] = gxy - rateVar * (gxy - zSxy)
    if q == 2:
        return imgAda[:, :, 0]
    return imgAda


def adaptive_median(image, smax=7):
    """
    自适应中值滤波

    参数:
        image: 图片
        smax: 参数 int
    返回:
        imgAda: 自适应中值滤波后的图片
    """
    m, n = smax, smax
    hPad = int((m - 1) / 2)
    wPad = int((n - 1) / 2)
    q = image.ndim
    e = 3
    if q == 2:
        image = image.reshape(image.shape[0], image.shape[1], 1)
        e = 1
    imgAda = np.zeros(image.shape)
    for k in range(e):
        img = image[:, :, k]
        imgPad = np.pad(img.copy(), ((hPad, m - hPad - 1), (wPad, n - wPad - 1)), 'edge')
        for i in range(hPad, img.shape[0] + hPad):
            for j in range(wPad, img.shape[1] + wPad):
                ksize = 3
                k = int(ksize / 2)
                pad = imgPad[i - k:i + k + 1, j - k:j + k + 1]
                zxy = img[i - hPad, j - wPad]
                zmin = np.min(pad)
                zmax = np.max(pad)
                zmed = np.median(pad)

                if zmin < zmed < zmax:
                    if zmin < zxy < zmax:
                        imgAda[i - hPad, j - wPad] = zxy
                    else:
                        imgAda[i - hPad, j - wPad] = zmed
                else:
                    while True:
                        ksize += 2
                        k = int(ksize / 2)
                        if zmin < zmed < zmax or ksize > smax:
                            break
                        pad = imgPad[i - k:i + k + 1, j - k:j + k + 1]
                        zmed = np.median(pad)
                        zmin = np.min(pad)
                        zmax = np.max(pad)
                    if zmin < zmed < zmax or ksize > smax:
                        if zmin < zxy < zmax:
                            imgAda[i - hPad, j - wPad] = zxy
                        else:
                            imgAda[i - hPad, j - wPad] = zmed

    if q == 2:
        return imgAda[:, :, 0]
    return imgAda


def sobel(img, ksize=3):
    """
    Sobel滤波

    参数:
        img: 图片
        ksize: 参数 int
    返回:
        sobel: Sobel滤波后的图片
    """
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=ksize)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=ksize)
    sobel = np.uint8(cv2.normalize(abs(sobelx) + abs(sobely), None, 0, 255, cv2.NORM_MINMAX))
    return sobel


def laplacian(img, ksize=1):
    """
    拉普拉斯滤波

    参数:
        img: 图片
        ksize: 参数 int
    返回:
        laplacian: 拉普拉斯滤波后的图片
    """
    return cv2.Laplacian(img, cv2.CV_64F, ksize=ksize)


def prewitt(img):
    """
    Prewitt滤波

    参数:
        img: 图片
    返回:
        prewitt: Prewitt滤波后的图片
    """
    prewitt_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
    prewitt_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
    img_x = cv2.filter2D(img, -1, prewitt_x)
    img_y = cv2.filter2D(img, -1, prewitt_y)
    return abs(img_x) + abs(img_y)


def roberts(img):
    """
    Roberts滤波

    参数:
        img: 图片
    返回:
        roberts: Roberts滤波后的图片
    """
    kernel_Roberts_x = np.array([[1, 0], [0, -1]])
    kernel_Roberts_y = np.array([[0, -1], [1, 0]])
    imgRoberts_x = cv2.filter2D(img, -1, kernel_Roberts_x)
    imgRoberts_y = cv2.filter2D(img, -1, kernel_Roberts_y)
    return abs(imgRoberts_x) + abs(imgRoberts_y)


def LoG(img, ksize=3):
    """
    LoG滤波

    参数:
        img: 图片
        ksize: 参数 int
    返回:
        out: LoG滤波后的图片
    """
    out = cv2.GaussianBlur(img, (ksize, ksize), 0)
    out = (cv2.Laplacian(out, cv2.CV_64F, ksize))
    return out


def gaussian(img, ksize=3, sigma=0):
    """
    高斯滤波

    参数:
        img: 图片
        ksize: 参数 int
        sigma: 参数 int
    返回:
        out: 高斯滤波后的图片
    """
    if sigma == 0:
        sigma = ksize / 2
    return cv2.GaussianBlur(img, (ksize, ksize), sigma)


def shift_img(img, x, y):
    """
    图像平移

    参数:
        img: 图像
        x: x轴平移量
        y: 轴平移量
    返回值:
        shifted: 平移后的图像
    """
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return shifted


def rotate(img, angle, x_center=0.5, y_center=0.5, scale=1):
    """
    图像旋转

    参数:
        img: 图像
        angle: 旋转角度
        x_center: x轴中心比例
        y_center: y轴中心比例
        scale: 缩放比例
    返回值:
        rotated: 旋转后的图像
    """
    h, w = img.shape[:2]
    center = (x_center * w, y_center * h)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(img, M, (w, h))
    return rotated


def flip(image, x_flip=False, y_flip=False):
    """
    图像翻转

    参数:
        image: 图像
        x_flip: x轴翻转
        y_flip: y轴翻转
    返回值:
        image: 翻转后的图像
    """
    if x_flip:
        image = cv2.flip(image, 0)
    if y_flip:
        image = cv2.flip(image, 1)
    return image


def motion_disk_Blur(img, angle, radius, dist):
    """
    图像运动模糊

    参数:
        img: 图像
        angel: 旋转角度
        radius: 半径
        dist: 距离
    返回值:
        out: 运动模糊后的图像
    """
    out = motionBlur(img, angle, dist)
    out = disk(out, radius)
    return out


def disk(img, radius):
    """
    图像圆盘模糊

    参数:
        img: 图像
        radius: 半径
    返回值:
        img: 圆盘模糊后的图像
    """
    if radius == 0:
        return img;
    k = 0;
    r = radius
    mask = np.zeros((int(2 * r) + 1, int(2 * r) + 1))
    for i in range(int(2 * r + 1)):
        for j in range(int(2 * r + 1)):
            if (i - r) ** 2 + (j - r) ** 2 <= r ** 2:
                mask[i, j] = 1
                k += 1
    kernel = mask / k
    n = img.ndim
    m = 3
    if n == 2:
        img = img.reshape(img.shape[0], img.shape[1], 1)
        m = 1
    for i in range(m):
        blurred = img[:, :, i]
        blurred = cv2.filter2D(blurred, -1, kernel)
        blurredNorm = np.uint8(cv2.normalize(blurred, None, 0, 255, cv2.NORM_MINMAX))
        img[:, :, i] = blurredNorm
    if n == 2:
        img = img.reshape(img.shape[0], img.shape[1])
    return img



def motionBlur(image, angle, dist, eps=1e-6):
    """
    图像运动模糊

    参数:
        image: 图像
        angel: 旋转角度
        dist: 距离
    返回值:
        image: 运动模糊后的图像
    """
    if angle == 0 and dist == 0:
        return image
    shape = image.shape[:2]
    xCenter = (shape[0] - 1) / 2
    yCenter = (shape[1] - 1) / 2
    sinVal = np.sin(angle * np.pi / 180)
    cosVal = np.cos(angle * np.pi / 180)
    PSF = np.zeros(shape[:2])
    for i in range(int(dist)):
        xOffset = round(sinVal * i)
        yOffset = round(cosVal * i)
        PSF[int(xCenter - xOffset), int(yCenter + yOffset)] = 1
    PSF = PSF / PSF.sum()
    n = image.ndim
    m = 3
    if n == 2:
        image = image.reshape(image.shape[0], image.shape[1], 1)
        m = 1
    out = image.copy()
    for i in range(m):
        img = image[:, :, i]
        fftImg = np.fft.fft2(img)  # 进行二维数组的傅里叶变换
        fftPSF = np.fft.fft2(PSF) + eps
        fftBlur = np.fft.ifft2(fftImg * fftPSF)
        fftBlur = np.abs(np.fft.fftshift(fftBlur))
        out[:, :, i] = fftBlur
    if n == 2:
        out = out.reshape(out.shape[0], out.shape[1])
    return out


def getPuv(image):
    """
    getPuv

    参数:
        image: 图像
    返回值:
        fftPuv
    """
    h, w = image.shape[:2]
    hPad, wPad = h - 3, w - 3
    pxy = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    pxyPad = np.pad(pxy, ((hPad // 2, hPad - hPad // 2), (wPad // 2, wPad - wPad // 2)), mode='constant')
    fftPuv = np.fft.fft2(pxyPad)
    return fftPuv


def wienerFilter(img, dist, angle, ValueOfwienerOrsmooth, nsr=0):
    """
    图像维纳滤波

    参数:
        img: 图像
        dist: 距离
        angle: 旋转角度
        ValueOfwienerOrsmooth: wiener滤波或者平滑
        nsr: 噪声比
    返回值:
        img: 维纳滤波后的图像
    """
    shape = img.shape[:2]
    xCenter = (shape[0] - 1) / 2
    yCenter = (shape[1] - 1) / 2
    sinVal = np.sin(angle * np.pi / 180)
    cosVal = np.cos(angle * np.pi / 180)
    PSF = np.zeros(shape[:2])
    K = nsr
    for i in range(int(dist)):
        xOffset = round(sinVal * i)
        yOffset = round(cosVal * i)
        PSF[int(xCenter - xOffset), int(yCenter + yOffset)] = 1
    PSF = PSF / PSF.sum()
    if ValueOfwienerOrsmooth == 'wiener':
        fftImg = np.fft.fft2(img)
        if PSF.all == None:
            return np.abs(np.fft.ifft2(fftImg - K))
        else:
            fftPSF = np.fft.fft2(PSF)
        fftWiener = np.conj(fftPSF) / (np.abs(fftPSF) ** 2 + K)
        imgWienerFilter = np.fft.ifft2(fftImg * fftWiener)
        imgWienerFilter = np.abs(np.fft.fftshift(imgWienerFilter))
        imgWienerFilter = np.uint8(cv2.normalize(imgWienerFilter, None, 0, 255, cv2.NORM_MINMAX))
        return imgWienerFilter
    elif ValueOfwienerOrsmooth == 'smooth':
        fftImg = np.fft.fft2(img)
        fftPSF = np.fft.fft2(PSF)
        conj = fftPSF.conj()
        fftPuv = getPuv(img)
        Huv = conj / (np.abs(fftPSF) ** 2 + K * (np.abs(fftPuv) ** 2))
        ifftImg = np.fft.ifft2(fftImg * Huv)
        ifftShift = np.abs(np.fft.fftshift(ifftImg))
        imgLSFilter = np.uint8(cv2.normalize(np.abs(ifftShift), None, 0, 255, cv2.NORM_MINMAX))
        return imgLSFilter
    else:
        return img


def sharpen1(img, ValueOfSharpen):
    """
    sharpen1

    参数:
        img: 图像
        ValueOfSharpen: 锐化算子
    返回值:
        img: 锐化后的图像
    """
    if ValueOfSharpen == 'Roberts':
        return np.uint8(cv2.normalize(roberts(img) + img, None, 0, 255, cv2.NORM_MINMAX))
    elif ValueOfSharpen == 'Prewitt':
        return np.uint8(cv2.normalize(prewitt(img) + img, None, 0, 255, cv2.NORM_MINMAX))
    else:
        return img


def sharpen2(img, ValueOfSharpen, inputSharpenSize):
    """
    sharpen2

    参数:
        img: 图像
        ValueOfSharpen: 锐化算子
        inputSharpenSize: 锐化算子大小
    返回值:
        img: 锐化后的图像
    """
    ksize = inputSharpenSize
    if ValueOfSharpen == 'Sobel':
        return np.uint8(cv2.normalize(sobel(img, ksize) + img, None, 0, 255, cv2.NORM_MINMAX))
    elif ValueOfSharpen == 'LoG':
        return np.uint8(cv2.normalize(LoG(img, ksize) + img, None, 0, 255, cv2.NORM_MINMAX))
    elif ValueOfSharpen == 'Laplace':
        return np.uint8(cv2.normalize(laplacian(img, ksize) + img, None, 0, 255, cv2.NORM_MINMAX))
    else:
        return img


def fft2change(img, ValueOfmagnitudeOrphase):
    """
    fft2变换

    参数:
        img: 图像
        ValueOfmagnitudeOrphase: magnitude或者phase
    返回值:
        img: fft2变换后的图像
    """
    out = np.fft.fft2(img)
    out = np.fft.fftshift(out)
    if ValueOfmagnitudeOrphase == 'magnitude':
        out = np.log(1 + np.abs(out))
        return np.uint8(cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX))
    elif ValueOfmagnitudeOrphase == 'phase':
        out = np.angle(out)
        return np.uint8(cv2.normalize(out, None, 0, 255, cv2.NORM_MINMAX))
    else:
        return img



def ideal_low_pass(img, d0):
    """
    理想低通器

    参数
        img: 原图像的频域图像
        d0: 阈值
    返回:
        mask: 低通滤波器
    """
    img_shape = img.shape
    mask = np.ones(img_shape, dtype=np.float64)
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            if np.sqrt((i - img_shape[0] / 2) ** 2 + (j - img_shape[1] / 2) ** 2) > d0:
                mask[i, j] = 0
    return mask


def ideal_high_pass(img, d0):
    """
    理想高通器

    参数:
        img: 原图像的频域图像
        d0: 阈值
    返回:
        mask: 高通滤波器
    """
    img_shape = img.shape
    mask = np.zeros(img_shape, dtype=np.float64)
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            if np.sqrt((i - img_shape[0] / 2) ** 2 + (j - img_shape[1] / 2) ** 2) > d0:
                mask[i, j] = 1
    return mask


def butterworth_low_pass(img, d0, n):
    """
    巴特沃斯低通器

    参数
        img: 原图像的频域图像
        d0: 阈值
        n: 次数
    返回:
        mask: 巴特沃斯低通滤波器
    """
    img_shape = img.shape
    mask = np.ones(img_shape, dtype=np.float64)
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            mask[i, j] = 1 / (1 + (np.sqrt((i - img_shape[0] / 2) ** 2 + (j - img_shape[1] / 2) ** 2) / d0) ** (2 * n))
    return mask



def butterworth_high_pass(img, d0, n):
    """
    巴特沃斯高通器

    参数
        img: 原图像的频域图像
        d0: 阈值
        n: 次数
    返回:
        mask: 巴特沃斯高通滤波器
    """
    return 1 - butterworth_low_pass(img, d0, n)


 
def gaussian_low_pass(img, d0):
    """
    高斯低通器

    参数
        img: 原图像的频域图像
        d0: 阈值
    返回:
        mask: 高斯低通滤波器
    """
    img_shape = img.shape
    mask = np.ones(img_shape, dtype=np.float64)
    for i in range(img_shape[0]):
        for j in range(img_shape[1]):
            mask[i, j] = np.exp(-((i - img_shape[0] / 2) ** 2 + (j - img_shape[1] / 2) ** 2) / (2 * d0 ** 2))
    return mask



def gaussian_high_pass(img, d0):
    """
    高斯高通器

    参数
        img: 原图像的频域图像
        d0: 阈值
    返回:
        mask: 高斯高通滤波器
    """
    return 1 - gaussian_low_pass(img, d0)


def toTrans(img, operater, d0):
    """
    变换

    参数
        img: 原图像
        operater: 滤波器
        d0: 阈值
    返回:
        out: 变换后的图像
    """
    out = np.fft.fft2(img)
    out = np.fft.fftshift(out)
    out = out * operater(out, d0)
    out = np.fft.ifftshift(out)
    out = np.fft.ifft2(out)
    return np.abs(out)


def toTransBtws(img, operater, d0, n):
    """
    巴特沃斯变换

    参数
        img: 原图像
        operater: 滤波器
        d0: 阈值
        n: 次数
    返回:
        out: 变换后的图像
    """
    out = np.fft.fft2(img)
    out = np.fft.fftshift(out)
    out = out * operater(out, d0, n)
    out = np.fft.ifftshift(out)
    out = np.fft.ifft2(out)
    return np.abs(out)


def lowFilter(img, ValueOfFilter, inputThreshold, n=0):
    """
    低通滤波

    参数
        img: 原图像
        ValueOfFilter: 滤波器类型
        inputThreshold: 阈值
        n: 次数
    返回:
        out: 变换后的图像
    """
    if ValueOfFilter == 'ideal':
        return toTrans(img, ideal_low_pass, inputThreshold)
    elif ValueOfFilter == 'butterworth':
        return toTransBtws(img, butterworth_low_pass, inputThreshold, n)
    elif ValueOfFilter == 'gaussian':
        return toTrans(img, gaussian_low_pass, inputThreshold)
    else:
        return img


def highFilter(img, ValueOfFilter, inputThreshold, n=0):
    """
    高通滤波

    参数
        img: 原图像
        ValueOfFilter: 滤波器类型
        inputThreshold: 阈值
        n: 次数
    返回:
        out: 变换后的图像
    """
    if ValueOfFilter == 'idealHigh':
        return toTrans(img, ideal_high_pass, inputThreshold)
    elif ValueOfFilter == 'butterworthHigh':
        return toTransBtws(img, butterworth_high_pass, inputThreshold, n)
    elif ValueOfFilter == 'gaussianHigh':
        return toTrans(img, gaussian_high_pass, inputThreshold)
    else:
        return img


def OTSU(img):
    """
    OSTU二值化

    参数
        img: 原图像
    返回:
        img: 二值化后的图像
    """
    q = img.ndim
    e = 3
    if q == 2:
        e = 1
        img = img.reshape(img.shape[0], img.shape[1], 1)
    for k in range(e):
        _, img[:, :, k] = cv2.threshold(img[:, :, k], 0, 255, cv2.THRESH_OTSU)
    if q == 2:
        img = img.reshape(img.shape[0], img.shape[1])
    return img


def GLOBAL(image):
    """
    全局阈值二值化

    参数
        image: 原图像
    返回:
        img: 二值化后的图像
    """
    q = image.ndim
    e = 3
    if q == 2:
        e = 1
        image = image.reshape(image.shape[0], image.shape[1], 1)
    for k in range(e):
        img = image[:, :, k]
        deltaT = 1
        hist = cv2.calcHist([img], [0], None, [256], [0, 256]).ravel()
        grayScale = range(256)
        total_pixels = img.shape[0] * img.shape[1]
        total_gray = hist @ grayScale
        T = round(total_gray / total_pixels)

        while True:
            num1, sum1 = 0, 0
            for i in range(T):
                num1 += hist[i]
                sum1 += i * hist[i]
            num2, sum2 = (total_pixels - num1), (total_gray - sum1)
            T1 = round(sum1 / num1)
            T2 = round(sum2 / num2)
            newT = round((T1 + T2) / 2)
            if abs(newT - T) < deltaT:
                break
            T = newT
        _, image[:, :, k] = cv2.threshold(img, T, 255, cv2.THRESH_BINARY)
    if q == 2:
        image = image.reshape(img.shape[0], img.shape[1])
    return image


def OtsuOrGlobal(img, ValueOfOtsuOrGlobal):
    """
    选择二值化方法

    参数
        img: 原图像
        ValueOfOtsuOrGlobal: 二值化方法
    返回:
        img: 二值化后的图像
    """
    if ValueOfOtsuOrGlobal == 'Otsu':
        return OTSU(img)
    elif ValueOfOtsuOrGlobal == 'Global':
        return GLOBAL(img)
    else:
        return img


def rgb2hsi(img, ValueOfRGBToHSI):
    """
    RGB转HSI

    参数
        img: 原图像
        ValueOfRGBToHSI: 转换方法
    返回:
        img: 转换后的图像
    """
    ndim = img.ndim
    if ndim == 2:
        return img
    else:
        print(1)
        b = np.float64(img[:, :, 0])
        g = np.float64(img[:, :, 1])
        r = np.float64(img[:, :, 2])
        I = (r + g + b) / 3
        print(2)
        S = 1 - (3 / (r + g + b)) * np.min([r, g, b], axis=0)
        print(3)
        num = 0.5 * ((r - g) + (r - b))
        den = np.sqrt(1. * (r - g) ** 2 + (0. + r - b) * (0. + g - b))
        out = num / (den + 1e-6)
        print(out)
        theta = np.arccos(out)
        print(theta)
        H = theta
        for i in range(H.shape[0]):
            for j in range(H.shape[1]):
                if b[i, j] > g[i, j]:
                    H[i, j] = 2 * np.pi - H[i, j]
                if S[i, j] == 0:
                    H[i, j] = 0
        H = np.uint8(cv2.normalize(H, None, 0, 255, cv2.NORM_MINMAX))
        S = np.uint8(cv2.normalize(S, None, 0, 255, cv2.NORM_MINMAX))
        I = np.uint8(cv2.normalize(I, None, 0, 255, cv2.NORM_MINMAX))
        if ValueOfRGBToHSI == 'I':
            return I
        elif ValueOfRGBToHSI == 'S':
            return S
        elif ValueOfRGBToHSI == 'H':
            return H
        elif ValueOfRGBToHSI == 'HSI':
            return cv2.merge([I, S, H])


def edge(img, ValueOfEdge, inputEdgeKernel, inputEdgeThreshold):
    """
    边缘检测

    参数
        img: 原图像
        ValueOfEdge: 边缘检测方法
        inputEdgeKernel: 边缘检测核
        inputEdgeThreshold: 边缘检测阈值
    返回:
        img: 边缘检测后的图像
    """
    type = judge_img_type(img)
    out = img.copy()
    if ValueOfEdge == 'Sobel':
        out = sobel(img, inputEdgeKernel)
    elif ValueOfEdge == 'Laplace':
        out = laplacian(img, inputEdgeKernel)
    elif ValueOfEdge == 'LoG':
        out = LoG(img, inputEdgeKernel)
    else:
        return img
    if type == 'gray':
        return np.where(out > inputEdgeThreshold, 255, 0)
    else:
        return out


def regional_growth(img, thresh=5):
    """
    区域生长算法

    参数:
        img: 图像
        thresh: 阈值
    返回:  
        区域生长结果
    """
    ndim = img.ndim
    e = 3
    if ndim == 2:
        img = img.reshape(img.shape[0], img.shape[1], 1)
        e = 1
    for k in range(e):
        img[:, :, k] = regional_growth1(img[:, :, k], thresh)
    if ndim == 2:
        img = img.reshape(img.shape[0], img.shape[1])
    return img


def regional_growth1(img, thresh=5):
    """
    区域生长算法

    参数:
        img: 图像
        thresh: 阈值
    返回:
        区域生长结果
    """
    _, _, _, centroids = cv2.connectedComponentsWithStats(cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1])
    seeds = centroids.astype(int)
    height, weight = img.shape
    seedMark = np.zeros(img.shape)
    seedList = []
    for seed in seeds:
        if (0 < seed[0] < height and 0 < seed[1] < weight): seedList.append(seed)
    label = 1  
    connects = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    while (len(seedList) > 0): 
        currentPoint = seedList.pop(0)  
        seedMark[currentPoint[0], currentPoint[1]] = label 
        for i in range(8): 
            tmpX = currentPoint[0] + connects[i][0]
            tmpY = currentPoint[1] + connects[i][1]
            if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight: 
                continue
            grayDiff = abs(int(img[tmpX, tmpY]) - int(img[currentPoint[0], currentPoint[1]]))  
            if grayDiff < thresh and seedMark[tmpX, tmpY] == 0:
                seedMark[tmpX, tmpY] = label
                seedList.append((tmpX, tmpY))
    seedMark = np.uint8(cv2.normalize(seedMark, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1))
    return seedMark
