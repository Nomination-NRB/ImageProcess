<template>
  <div class="main">
    <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
      <el-tab-pane label="基本操作" name="basic" class="el-tabs__content">
        <el-scrollbar noresize height="560px">
          <div style="width: 98%">
            <el-divider content-position="center" style="font-size: 20px">(像素)放大/缩小</el-divider>
            <div class="slider-demo-block">
              <span class="demonstration">X轴变化率(倍)</span>
              <el-slider v-model="zoomXValue" :step="0.1" :min="0.1" :max="10" show-input />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration">Y轴变化率(倍)</span>
              <el-slider v-model="zoomYValue" :step="0.1" :min="0.1" :max="10" show-input />
            </div>
            <el-button @click="resizeHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">旋转</el-divider>
            <div class="slider-demo-block">
              <span class="demonstration">角度(%)</span>
              <el-slider v-model="rotateValue" :step="1" :min="-180" :max="180" show-input />
            </div>
            <el-button @click="rotateHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            <el-divider content-position="center" style="font-size: 20px">翻转/镜像</el-divider>
            <div>
              <el-radio v-model="spinXYVaue" label="X" size="large" border>X轴翻转</el-radio>
              <el-radio v-model="spinXYVaue" label="Y" size="large" border>Y轴翻转</el-radio>
            </div>

            <el-button @click="reversalHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">平移</el-divider>
            <div class="slider-demo-block">
              <span class="demonstration">X轴偏移(%)</span>
              <el-slider v-model="transXValue" :step="1" :min="-180" :max="180" show-input />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration">Y轴偏移(%)</span>
              <el-slider v-model="transYValue" :step="1" :min="-180" :max="180" show-input />
            </div>
            <el-button @click="translateHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
          </div>
        </el-scrollbar>
      </el-tab-pane>
      <el-tab-pane label="灰度变换" name="change" class="el-tabs__content">
        <el-scrollbar noresize height="560px">
          <div style="width: 98%">
            <el-divider content-position="center" style="font-size: 20px">对数变换</el-divider>
            <el-button @click="logChangeHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">反色变换/反转</el-divider>
            <el-button @click="reverseChangeHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">伽马变换/幂次变换</el-divider>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">幂次值</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputGamma" placeholder="输入值，例如：3"
                style="margin-left: 10px; width: 200px" />
            </div>

            <el-button @click="gammaChangeHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">直方图均衡化</el-divider>
            <el-button @click="histogramToBalanceHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            <el-divider content-position="center" style="font-size: 20px">分段线性变换</el-divider>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">a</span>
              <el-input oninput="if(value>255)value=255;if(value<0)value=0" @change="inputALinear"
                v-model.number="inputA" placeholder="输入值，例如：150" style="margin-left: 10px; width: 200px" />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">b</span>
              <el-input oninput="if(value>255)value=255;if(value<0)value=0" v-model="inputB" placeholder="输入值，例如：230"
                style="margin-left: 10px; width: 200px" />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">c</span>
              <el-input oninput="if(value>255)value=255;if(value<0)value=0" v-model="inputC" placeholder="输入值，例如：0"
                style="margin-left: 10px; width: 200px" />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">d</span>
              <el-input oninput="if(value>255)value=255;if(value<0)value=0" v-model="inputD" placeholder="输入值，例如：255"
                style="margin-left: 10px; width: 200px" />
            </div>
            <el-button @click="linearChangeHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">对比度拉伸</el-divider>
            <el-button @click="contrastHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
          </div>
        </el-scrollbar>
      </el-tab-pane>
      <el-tab-pane label="噪声添加" name="noise" class="el-tabs__content">
        <el-scrollbar noresize height="560px">
          <div style="width: 98%">
            <el-divider content-position="center" style="font-size: 20px">椒盐噪声</el-divider>
            <div class="slider-demo-block">
              <span class="demonstration">椒噪声比例</span>
              <el-slider v-model="zoomPepperValue" :step="0.01" :min="0.001" :max="1" show-input />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration">盐噪声比例</span>
              <el-slider v-model="zoomSaltValue" :step="0.01" :min="0.001" :max="1" show-input />
            </div>
            <el-button @click="addSaltPepperHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">高斯噪声</el-divider>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">均值</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputMean" placeholder="输入值，例如：0"
                style="margin-left: 10px; width: 200px" />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">方差</span>
              <el-input oninput="if(value>100)value=100;if(value<0)value=0" v-model="inputVariance" placeholder="输入值，例如：0.03"
                style="margin-left: 10px; width: 200px" />
            </div>
            <el-button @click="addGaussianHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
          </div>
        </el-scrollbar>
      </el-tab-pane>
      <el-tab-pane label="复原操作" name="re" class="el-tabs__content">
        <el-scrollbar noresize height="560px">
          <div style="width: 98%">
            <el-divider content-position="center" style="font-size: 20px">模糊操作
            </el-divider>
            <div>
              <el-tag style="margin-top: 6px; align-items: center; font-size: 15px">Motion</el-tag>
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">距离</span>
              <el-input oninput="if(value>255)value=255;if(value<0)value=0" v-model="inputMotionDistance"
                placeholder="输入值，例如：50" style="margin-left: 10px; width: 200px" />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">角度</span>
              <el-input oninput="if(value>360)value=360;if(value<0)value=0" v-model="inputMotionAngle" placeholder="输入值，例如：60"
                style="margin-left: 10px; width: 200px" />
            </div>

            <div>
              <el-tag style="margin-top: 6px; align-items: center; font-size: 15px">Disk</el-tag>
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">半径</span>
              <el-input onkeyup="value=value.replace(/[^\d]/g,'')" oninput="if(value>200)value=200;if(value<0)value=0"
                v-model="inputMotionRadius" placeholder="输入值，例如：2" style="margin-left: 10px; width: 200px" />
            </div>

            <el-button @click="motionHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">复原函数
            </el-divider>
            <el-row>
              <div style="margin-bottom: 15px">
                <div>
                  <el-tag style="margin-top: 6px; align-items: center; font-size: 15px">PSF</el-tag>
                </div>
                <div class="slider-demo-block">
                  <span class="demonstration" style="margin-right: 4px; overflow: visible">距离</span>
                  <el-input oninput="if(value>255)value=255;if(value<0)value=0" v-model="inputPSFDistance"
                    placeholder="(必须是灰度图)例如：20" style="margin-left: 10px; width: 200px" />
                </div>
                <div class="slider-demo-block">
                  <span class="demonstration" style="margin-right: 4px; overflow: visible">角度</span>
                  <el-input oninput="if(value>360)value=360;if(value<0)value=0" v-model="inputPSFAngle"
                    placeholder="(必须是灰度图)例如：30" style="margin-left: 10px; width: 200px" />
                </div>

                <div>
                  <el-tag style="margin-top: 6px; align-items: center; font-size: 15px">NSR</el-tag>
                </div>
                <div class="slider-demo-block">
                  <span class="demonstration" style="margin-right: 4px; overflow: visible">噪信比</span>
                  <el-input onkeyup="value=value.replace(/[^\d]/g,'')"
                    oninput="if(value>200)value=200;if(value<0)value=0" v-model="inputNSRRadius" placeholder="(必须是灰图)例如：1"
                    style="margin-left: 10px; width: 200px" />
                </div>
              </div>
            </el-row>
            <div>
                  <el-radio v-model="ValueOfwienerOrsmooth" label="wiener" size="large" border>维纳滤波</el-radio>
                  <el-radio v-model="ValueOfwienerOrsmooth" label="smooth" size="large" border>约束复原</el-radio>
            </div>
            <el-button @click="wienerHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            
            <el-divider content-position="center" style="font-size: 20px">自适应中值滤波
            </el-divider>
            <el-button @click="selfMedianHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
            <el-divider content-position="center" style="font-size: 20px">自适应均值滤波
            </el-divider>
            <el-button @click="selfMeanHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
          </div>
        </el-scrollbar>
      </el-tab-pane>
      <el-tab-pane label="图像分割" name="partitionPart" class="el-tabs__content">
        <el-scrollbar noresize height="560px">
          <div style="width: 98%">
            <el-divider content-position="center" style="font-size: 20px">分割算法</el-divider>
            <div style="margin-bottom: 15px">
              <div>
                <el-radio v-model="ValueOfOtsuOrGlobal" label="Otsu" size="large" border>Otsu</el-radio>
                <el-radio v-model="ValueOfOtsuOrGlobal" label="Global" size="large" border>基本全局阈值法</el-radio>
              </div>
            </div>
            <el-button @click="partitionHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            <div style="margin-bottom: 15px">
              <div>
                <el-radio style="margin-top: 15px;" v-model="ValueOfAreaGrow" label="AreaGrow" size="large" border>区域生长</el-radio>
              </div>
            </div>
            
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">阈值</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputAreaGrow" placeholder="输入值，例如：2"
                style="margin-left: 10px; width: 200px" />
            </div>

            <el-button @click="AreaGrowHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            <el-divider content-position="center" style="font-size: 20px">边缘检测</el-divider>
            <div style="margin-bottom: 15px"> 
              <div>
                <el-radio v-model="ValueOfEdge" label="Sobel" size="large" border>Sobel</el-radio>
                <el-radio v-model="ValueOfEdge" label="LoG" size="large" border>LoG</el-radio>
                <el-radio v-model="ValueOfEdge" label="Laplace" size="large" border>Laplace</el-radio>
              </div>
            </div>

            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">滤波核大小</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputEdgeKernel" placeholder="输入值，例如：3"
                style="margin-left: 10px; width: 200px" />
                
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">阈值的大小</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputEdgeThreshold" placeholder="输入值，例如：5"
                style="margin-left: 10px; width: 200px" />
            </div>
            

            <el-button @click="edgeHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            

          </div>
        </el-scrollbar>
      </el-tab-pane>
      <el-tab-pane label="空间域操作" name="space" class="el-tabs__content">
        <el-scrollbar noresize height="560px">
          <div style="width: 98%">
            <el-divider content-position="center" style="font-size: 20px">平滑
            </el-divider>
            <div style="margin-bottom: 15px">
              <div>
                <el-radio v-model="ValueOfMeanOrMedian" label="mean" size="large" border>均值滤波</el-radio>
                <el-radio v-model="ValueOfMeanOrMedian" label="median" size="large" border>中值滤波</el-radio>
              </div>
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">滤波核大小</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputMeanOrMedianSize"
                placeholder="输入值，例如：2" style="margin-left: 10px; width: 200px" />
            </div>

            <el-button @click="filterHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            <el-divider content-position="center" style="font-size: 20px">锐化
            </el-divider>
            <div>
                  <el-tag style="margin-bottom: 8px; align-items: center; font-size: 15px">一阶锐化</el-tag>
            </div>
            <div style="margin-bottom: 15px">
              <div>
                <el-radio v-model="ValueOfSharpenOne" label="Roberts" size="large" border>Roberts</el-radio>
                <el-radio v-model="ValueOfSharpenOne" label="Prewitt" size="large" border>Prewitt</el-radio>
              </div>
            </div>

            <el-button @click="sharpenHandlerOne" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>


            <div>
                  <el-tag style="margin-bottom: 8px; margin-top: 15px; align-items: center; font-size: 15px">二阶锐化</el-tag>
            </div>
            <div style="margin-bottom: 15px">
              <div>
                <el-radio v-model="ValueOfSharpenTwo" label="Sobel" size="large" border>Sobel</el-radio>
                <el-radio v-model="ValueOfSharpenTwo" label="LoG" size="large" border>LoG</el-radio>
                <el-radio v-model="ValueOfSharpenTwo" label="Laplace" size="large" border>Laplace</el-radio>
              </div>
            </div>

            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">滤波核大小</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputSharpenSize" placeholder="输入值，例如：3"
                style="margin-left: 10px; width: 200px" />
            </div>

            <el-button @click="sharpenHandlerTwo" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
          </div>
        </el-scrollbar>
      </el-tab-pane>
      <el-tab-pane label="频域操作" name="op" class="el-tabs__content">
        <el-scrollbar noresize height="560px">
          <div style="width: 98%">
            <el-divider content-position="center" style="font-size: 20px">傅里叶变换（空间域到频域变换）
            </el-divider>
            <div style="margin-bottom: 15px">
              <div style="width: 565px; height: auto; align-items: stretch">
                <div>
                  <el-radio v-model="ValueOfmagnitudeOrphase" label="magnitude" size="large" border>幅度谱</el-radio>
                  <el-radio v-model="ValueOfmagnitudeOrphase" label="phase" size="large" border>相位谱</el-radio>
                </div>
              </div>
            </div>
            <el-button @click="fftHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            <el-divider content-position="center" style="font-size: 20px">平滑
            </el-divider>
            <div style="margin-bottom: 15px">
              <div style="width: 565px; height: auto; align-items: stretch">
                <div>
                  <el-radio v-model="ValueOfLowFilter" label="ideal" size="large" border>理想低通滤波</el-radio>
                  <el-radio v-model="ValueOfLowFilter" label="butterworth" size="large" border>巴特沃斯低通滤波</el-radio>
                  <el-radio v-model="ValueOfLowFilter" label="gaussian" size="large" border>高斯低通滤波</el-radio>
                </div>
              </div>
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">阈值大小</span>
              <el-input oninput="if(value>200)value=200;if(value<0)value=0" v-model="inputLowThreshold"
                placeholder="输入值，例如：5" style="margin-left: 10px; width: 200px" />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">巴特幂次</span>
              <el-input oninput="if(value>255)value=255;if(value<0)value=0" v-model="inputLowButter" placeholder="输入值，例如：2"
                style="margin-left: 10px; width: 200px" />
            </div>
            <el-button @click="lowFilterHandler" type="primary"
              style="margin-top: 26px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            <el-divider content-position="center" style="font-size: 20px">锐化
            </el-divider>
            <div style="margin-bottom: 15px">
              <div style="width: 565px; height: auto; align-items: stretch">
                <div>
                  <el-radio v-model="ValueOfHighFilter" label="idealHigh" size="large" border>理想高通滤波</el-radio>
                  <el-radio v-model="ValueOfHighFilter" label="butterworthHigh" size="large" border>巴特沃斯高通滤波</el-radio>
                  <el-radio v-model="ValueOfHighFilter" label="gaussianHigh" size="large" border>高斯高通滤波</el-radio>
                </div>
              </div>
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">阈值大小</span>
              <el-input oninput="if(value>200)value=200;if(value<0)value=0" v-model="inputHighThreshold"
                placeholder="输入值，例如：4" style="margin-left: 10px; width: 200px" />
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">巴特幂次</span>
              <el-input oninput="if(value>255)value=255;if(value<0)value=0" v-model="inputHighButter" placeholder="输入值，例如：3"
                style="margin-left: 10px; width: 200px" />
            </div>
            <el-button @click="highFilterHandler" type="primary"
              style="margin-top: 26px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>
          </div>
        </el-scrollbar>
      </el-tab-pane>
      <el-tab-pane label="彩图处理" name="colorful" class="el-tabs__content">
        <el-scrollbar noresize height="560px">
          <div style="width: 98%">
            <el-divider content-position="center" style="font-size: 20px">RGB转HSI
            </el-divider>
            <div style="margin-bottom: 15px">
              <div style="width: 565px; height: auto; align-items: stretch">
                <div>
                  <el-radio v-model="ValueOfRGBToHSI" label="H" size="large" border>H色调</el-radio>
                  <el-radio v-model="ValueOfRGBToHSI" label="S" size="large" border>S饱和度</el-radio>
                  <el-radio v-model="ValueOfRGBToHSI" label="I" size="large" border>I强度</el-radio>
                  <el-radio v-model="ValueOfRGBToHSI" label="HSI" size="large" border>HSI</el-radio>
                </div>
              </div>
            </div>
            <el-button @click="rgbToHSIHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

            <el-divider content-position="center" style="font-size: 20px">彩图分割</el-divider>
            <div style="margin-bottom: 15px"> 
              <div>
                <el-radio v-model="ValueOfEdgeColor" label="Sobel" size="large" border>Sobel</el-radio>
                <el-radio v-model="ValueOfEdgeColor" label="LoG" size="large" border>LoG</el-radio>
                <el-radio v-model="ValueOfEdgeColor" label="Laplace" size="large" border>Laplace</el-radio>
              </div>
            </div>

            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">滤波核大小</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputEdgeColorKernel" placeholder="输入值，例如：3"
                style="margin-left: 10px; width: 200px" />
                
            </div>
            <div class="slider-demo-block">
              <span class="demonstration" style="margin-right: 4px; overflow: visible">阈值的大小</span>
              <el-input oninput="if(value>10)value=10;if(value<0)value=0" v-model="inputEdgeColorThreshold" placeholder="输入值，例如：5"
                style="margin-left: 10px; width: 200px" />
            </div>
            

            <el-button @click="edgeColorHandler" type="primary"
              style="margin-top: 6px; margin-left: 4px; align-items: center">
              <el-icon size="medium">
                <Setting />
              </el-icon>
              应用
            </el-button>

          </div>
        </el-scrollbar>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import * as API from "@/api/resolve";
import { Setting, Calendar } from "@element-plus/icons-vue";
import { ElNotification, ElLoading } from "element-plus";
export default {
  components: {
    Setting,
    Calendar,
  },
  data() {
    return {
      activeName: "basic",

      //放大，缩小
      zoomXValue: 1,
      zoomYValue: 1,

      //旋转
      rotateValue: 0,

      //翻转
      spinXYVaue: "X",

      //平移
      transXValue: 0,
      transYValue: 0,

      //对数变换，无参数
      logChangeValue: "log",

      //反色变换，无参数
      reverseChangeValue: "reverse",

      //幂次变换
      inputGamma: '',

      //直方图均衡化，无参数
      histogramToBalanceValue: 0,

      //分段线性变换
      inputA: '',
      inputB: '',
      inputC: '',
      inputD: '',

      //对比度拉伸，无参数
      contrastValue: 0,

      //椒盐噪声
      zoomPepperValue: 0.02,
      zoomSaltValue: 0.02,

      //高斯噪声，均值，方差
      inputMean: '',
      inputVariance: '',

      //Motion距离，角度/Disk半径
      inputMotionDistance: '',
      inputMotionAngle: '',
      inputMotionRadius: '',

      //维纳滤波，平滑约束复原
      inputPSFDistance: '',
      inputPSFAngle: '',
      inputNSRRadius: '',
      ValueOfwienerOrsmooth: 'wiener',

      //自适应中值滤波，无参数（待修改）
      selfMedianValue: 0,

      //自适应均值滤波，无参数（待修改）
      selfMeanValue: 0,

      //Otsu，基于全局阈值
      ValueOfOtsuOrGlobal: "Otsu",

      //区域生长
      ValueOfAreaGrow: "AreaGrow",
      inputAreaGrow: '',

      //边缘检测,阈值
      ValueOfEdge: "Sobel",
      inputEdgeKernel: '',
      inputEdgeThreshold: '',

      //平滑滤波（中值/均值），滤波核大小
      ValueOfMeanOrMedian: "mean",
      inputMeanOrMedianSize: '',

      //锐化滤波，滤波核大小
      ValueOfSharpenOne: "Roberts",
      ValueOfSharpenTwo: "Sobel",
      inputSharpenSize: '',

      //傅里叶变换
      ValueOfmagnitudeOrphase: "magnitude",

      //低通滤波，低通阈值
      ValueOfLowFilter: "ideal",
      inputLowThreshold: '',
      inputLowButter: '',

      //高通滤波，高通阈值
      ValueOfHighFilter: "idealHigh",
      inputHighThreshold: '',
      inputHighButter: '',

      //rgbToHsi
      ValueOfRGBToHSI: "H",

      //彩图分割，阈值
      ValueOfEdgeColor: "Sobel",
      inputEdgeColorKernel: '',
      inputEdgeColorThreshold: '',


    };
  },
  methods: {
    // 测试输入值，将此函数放在下方异步函数中，如addGaussianHandler，通过this.gaussionMean()调用
    gaussianMean() {
      const newVal = this.inputMean
      console.log(newVal);
    },


    async resizeHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.resize({
        zoomXValue: this.zoomXValue,
        zoomYValue: this.zoomYValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "已缩小/放大图片",
        type: "success",
      });
    },

    async rotateHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.rotate({
        rotateValue: this.rotateValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "已旋转图片",
        type: "success",
      });
    },



    async reversalHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.reversal({
        spinXYVaue: this.spinXYVaue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "已翻转图片",
        type: "success",
      });
    },

    async translateHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.translate({
        transXValue: this.transXValue,
        transYValue: this.transYValue,
        id: _id,
      });


      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "已平移图片",
        type: "success",
      });
    },

    async logChangeHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.logChange({
        logChangeValue: this.logChangeValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已对数变换",
        type: "success",
      });
    },

    async reverseChangeHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.reverseChange({
        reverseChangeValue: this.reverseChangeValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已反转变换",
        type: "success",
      });
    },

    async gammaChangeHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.gammaChange({
        inputGamma: this.inputGamma,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已伽马变换",
        type: "success",
      });
    },

    async histogramToBalanceHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.histogramToBalance({
        histogramToBalanceValue: this.histogramToBalanceValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "直方图已均衡化",
        type: "success",
      });
    },

    async linearChangeHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.linearChange({
        inputA: this.inputA,
        inputB: this.inputB,
        inputC: this.inputC,
        inputD: this.inputD,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已线性变换",
        type: "success",
      });
    },

    async contrastHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.contrast({
        contrastValue: this.contrastValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已对比变换",
        type: "success",
      });
    },

    async addSaltPepperHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.addSaltPepper({
        zoomPepperValue: this.zoomPepperValue,
        zoomSaltValue: this.zoomSaltValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已加入椒盐噪声",
        type: "success",
      });
    },


    async addGaussianHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作
      //针对不同操作调用不同API即可
      let res = await API.addGaussian({
        inputMean: this.inputMean,
        inputVariance: this.inputVariance,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已加入高斯噪声",
        type: "success",
      });
    },

    async motionHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.motion({
        inputMotionDistance: this.inputMotionDistance,
        inputMotionAngle: this.inputMotionAngle,
        inputMotionRadius: this.inputMotionRadius,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已模糊",
        type: "success",
      });
    },

    async wienerHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.wiener({
        inputPSFDistance: this.inputPSFDistance,
        inputPSFAngle: this.inputPSFAngle,
        inputNSRRadius: this.inputNSRRadius,
        ValueOfwienerOrsmooth: this.ValueOfwienerOrsmooth,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过Wiener滤波处理",
        type: "success",
      });
    },

    async selfMedianHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.selfMedian({
        selfMedianValue: this.selfMedianValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过自适应中值滤波处理",
        type: "success",
      });
    },

    async selfMeanHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.selfMean({
        selfMeanValue: this.selfMeanValue,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过自适应均值滤波处理",
        type: "success",
      });
    },

    async partitionHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.partition({
        ValueOfOtsuOrGlobal: this.ValueOfOtsuOrGlobal,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过自适应均值滤波处理",
        type: "success",
      });
    },
    
    async AreaGrowHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.AreaGrow({
        ValueOfAreaGrow: this.ValueOfAreaGrow,
        inputAreaGrow: this.inputAreaGrow,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过分割处理",
        type: "success",
      });
    },


    async edgeHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.edge({
        ValueOfEdge: this.ValueOfEdge,
        inputEdgeKernel: this.inputEdgeKernel,
        inputEdgeThreshold: this.inputEdgeThreshold,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过分割处理",
        type: "success",
      });
    },

    async filterHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.filter({
        ValueOfMeanOrMedian: this.ValueOfMeanOrMedian,
        inputMeanOrMedianSize: this.inputMeanOrMedianSize,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过滤波处理",
        type: "success",
      });
    },

    async sharpenHandlerOne() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.sharpenOne({
        ValueOfSharpenOne: this.ValueOfSharpenOne,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过锐化处理",
        type: "success",
      });
    },

    async sharpenHandlerTwo() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.sharpenTwo({
        ValueOfSharpenTwo: this.ValueOfSharpenTwo,
        inputSharpenSize: this.inputSharpenSize,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过锐化处理",
        type: "success",
      });
    },

    async fftHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.fft({
        ValueOfmagnitudeOrphase: this.ValueOfmagnitudeOrphase,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过傅里叶变换",
        type: "success",
      });
    },

    async lowFilterHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.lowFilter({
        ValueOfLowFilter: this.ValueOfLowFilter,
        inputLowThreshold: this.inputLowThreshold,
        inputLowButter: this.inputLowButter,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过低通滤波处理",
        type: "success",
      });
    },

    async highFilterHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.highFilter({
        ValueOfHighFilter: this.ValueOfHighFilter,
        inputHighThreshold: this.inputHighThreshold,
        inputHighButter: this.inputHighButter,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过高通滤波处理",
        type: "success",
      });
    },
    
    async rgbToHSIHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.rgbToHSI({
        ValueOfRGBToHSI: this.ValueOfRGBToHSI,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过处理",
        type: "success",
      });
    },
    
    async edgeColorHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.edgeColor({
        ValueOfEdgeColor: this.ValueOfEdgeColor,
        inputEdgeColorKernel: this.inputEdgeColorKernel,
        inputEdgeColorThreshold: this.inputEdgeColorThreshold,
        id: _id,
      });

      //以下为必备操作
      this.$store.commit("image/SET_URL", res.data.file);
      this.$forceUpdate();
      this.$emit("refresh");
      loading.close();
      ElNotification({
        title: "操作成功",
        message: "图片已经过处理",
        type: "success",
      });
    },






  },
};
</script>

<style scoped>
.slider-demo-block {
  display: flex;
  align-items: center;
}

.slider-demo-block .el-slider {
  margin-top: 0;
  margin-left: 12px;
}

.slider-demo-block .demonstration {
  font-size: 14px;
  line-height: 44px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-bottom: 0;
}

.slider-demo-block .demonstration+.el-slider {
  flex: 1 0 60%;
}

.el-tabs__content {
  padding: 4px;
  color: #6b778c;
}

.main {
  width: 590px;
  height: 650px;
}
</style>
