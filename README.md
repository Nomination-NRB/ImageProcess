# ImageProcess
## 简介

数字图像处理，复现基本的图像处理函数

## 技术栈

前端：vue

后端：Django restframework

数据库：Django自带的sqlite

## 基本功能

- class_name：在Django的api/models.py中实现，对应每个接口所调用的处理操作
- function_parameters：前端所传的参数
- parameters_help：参数，类型的解释

| class_name             | Chinese_name          | function_parameters                                          | parameters_help                                              |
| ---------------------- | --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| resize                 | 放大/缩小             | zoomXValue、zoomYValue                                       | x,y轴变化倍率                                                |
| rotate                 | 旋转                  | rotateValue                                                  | 角度（-180到180）                                             |
| reversal               | 翻转                  | spinXYVaue                                                   | 翻转，字符串（X/Y）                                          |
| translate              | 平移                  | transXValue、transYValue                                     | x,y轴偏移（%）                                               |
| logChange              | 对数变换              | None                                                         | None                                                         |
| reverseChange          | 反色变换              | None                                                         | None                                                         |
| gammaChange            | 幂次变换              | inputGamma                                                   | 数值（0到10）                                                 |
| histogramToBalance     | 直方图均衡化          | None                                                         | None                                                         |
| linearChange           | 分段线性变换          | inputA、inputB、inputC、inputD                               | 数值（0到255）                                                |
| contrast               | 对比度拉伸            | None                                                         | None                                                         |
| addSaltPepper          | 椒盐噪声              | zoomPepperValue、zoomSaltValue                               | 数值比例（0.001到1）                                          |
| addGaussian            | 高斯噪声              | inputMean、inputVariance                                     | 数值（0到1）                                                  |
| motion                 | Motion/Disk模糊操作   | inputMotionDistance、inputMotionAngle、inputMotionRadius     | 距离（0到255）角度（0到360）                                   |
| wiener                 | 复原函数              | inputPSFDistance、inputPSFAngle、inputNSRRadius、ValueOfwienerOrsmooth | 数值，数值，数值，字符串（wiener/smooth）                    |
| selfMedian             | 自适应中值滤波        | None                                                         | None                                                         |
| selfMean               | 自适应均值滤波        | None                                                         | None                                                         |
| filter                 | 平滑滤波（中值/均值） | ValueOfMeanOrMedian、inputMeanOrMedianSize                   | 字符串（mean/median）数值（0到10）                            |
| sharpenOne、sharpenTwo | 锐化滤波              | ValueOfSharpenOne、ValueOfSharpenTwo、inputSharpenSize       | 字符串（Roberts/Prewitt）字符串（Sobel/LoG/Laplace）数值（0到10） |
| fft                    | 傅里叶变换            | ValueOfmagnitudeOrphase                                      | 字符串（magnitude/phase）                                    |
| lowFilter              | 低通滤波              | ValueOfLowFilter、inputLowThreshold，inputLowButter          | 字符串（ideal/butterworth/gaussian）数值（0到200）数值（0到200） |
| highFilter             | 高通滤波              | ValueOfHighFilter、inputHighThreshold，inputHighButter       | 字符串（idealHigh/butterworthHigh/gaussianHigh）数值（0到200）数值（0到200） |
| partition              | 图像分割              | ValueOfOtsuOrGlobal                                          | 字符串（Otsu/Global）                                        |
| rgbToHSI               | RGB转HIS              | ValueOfRGBToHSI                                              | 字符串（H/S/I/HSI）                                          |
| edge                   | 边缘检测              | ValueOfEdge、inputEdgeKernel、inputEdgeThreshold             | 字符串（Sobel/LoG/Laplace）数值、数值                        |
| edgeColor              | 彩图分割              | ValueOfEdgeColor、inputEdgeColorKernel、inputEdgeColorThreshold | 字符串（Sobel/LoG/Laplace）数值、数值                        |
| AreaGrow               | 区域生长              | ValueOfAreaGrow、inputAreaGrow                               | 字符串（AreaGrow）数值                                       |

## 总览

[![z7xZDg.png](https://s1.ax1x.com/2022/12/16/z7xZDg.png)](https://imgse.com/i/z7xZDg)

[![z7vr7j.png](https://s1.ax1x.com/2022/12/16/z7vr7j.png)](https://imgse.com/i/z7vr7j)

## 关键目录

- 前端

```
src
├─ App.vue
├─ api
│    └─ resolve.js						//所有的api接口
├─ components
│    └─ chart							//echarts直方图组件
│           ├─ index.js
│           ├─ index.vue
│           └─ options
├─ main.js
├─ router								//注册路由
│    └─ index.js
├─ utils
│    └─ request.js						//前端请求封装
└─ views
       └─ home
              ├─ components
              │    ├─ panel.vue			//操作盘vue
              │    └─ processView.vue	//处理视图vue
              └─ index.vue
```



- 后端

```
DjangoRestframewor
├─ api
│    ├─ models.py						//数据库表的定义
│    ├─ serializers.py					//处理数据的序列化器
│    ├─ urls.py							//将接口注册到路由中
│    └─ views.py						//各个视图集操作前端传入的数据进行处理
├─ db.sqlite3							//Django自带的数据库
├─ lib
│    ├─ manage
│    │    └─ imageProcess.py			//图像处理函数
│    └─ utils
│         └─ json_response.py			//返回定制的json数据格式
├─ log									//运行日志
│    ├─ all.log
│    ├─ error.log
│    └─ script.log
├─ manage.py
├─ media								//本地存放的图片路径
│    └─ images							//处理的图片路径
│           ├─ grass1.jpg
│           ├─ grass1_1475Amh.jpg
│           ├─ grass1_tAABlwO.jpg
│           ├─ ori						//备份的图片路径
│                ├─ grass1.jpg
│                └─ warma4_mt9yOn0.jpg
├─ python_dip_courseproject_django
│    ├─ settings.py 					//项目的各种配置
│    └─ urls.py							//项目的总路由
└─ requirements.txt						//项目所需的依赖包
```



## 使用方法

```bash
git clone https://github.com/Nomination-NRB/ImageProcess.git
```

在vscode或者其他编译器打开项目文件夹

激活本项目具体使用的环境，切换到ImageProcess/DjangoRestframework/requirements.txt目录下在终端执行该命令即可

```bash
pip install -r requirements.txt
```

- 启动后端
  - 确保当前路径在后端项目DjangoRestframework文件夹下，且有manage.py文件

```bash
python manage.py runserver
```

- 启动前端
  - 确保当前路径在前端项目Frontend文件夹下

```bash
npm install
npm run dev
```

- 打开本地连接即可
