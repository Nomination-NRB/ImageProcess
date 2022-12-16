import request from "@/utils/request";

export function hello() {
  return request({
    url: "/",
    method: "get",
  });
}

export function uploadImage(data) {
  return request({
    url: "/ImageSet/",
    method: "post",
    data,
  });
}

export function getHistArray(data) {
  return request({
    url: "/getHistArray/",
    method: "post",
    data,
  });
}

export function new_(data) {
  return request({
    url: "/new_/",
    method: "post",
    data,
  });
}

// 缩小放大
export function resize(data) {
  return request({
    url: "/resize/",
    method: "post",
    data,
  });
}

// 旋转
export function rotate(data) {
  return request({
    url: "/rotate/",
    method: "post",
    data,
  });
}

// 翻转
export function reversal(data) {
  return request({
    url: "/reversal/",
    method: "post",
    data,
  });
}

// 平移
export function translate(data) {
  return request({
    url: "/translate/",
    method: "post",
    data,
  });
}

// 对数变换
export function logChange(data) {
  return request({
    url: "/logChange/",
    method: "post",
    data,
  });
}


// 反色变换
export function reverseChange(data) {
  return request({
    url: "/reverseChange/",
    method: "post",
    data,
  });
}

// 幂次变换
export function gammaChange(data) {
  return request({
    url: "/gammaChange/",
    method: "post",
    data,
  });
}

// 直方图均衡化
export function histogramToBalance(data) {
  return request({
    url: "/histogramToBalance/",
    method: "post",
    data,
  });
}

// 直方图归一化
export function histogramToOne(data) {
  return request({
    url: "/histogramToOne/",
    method: "post",
    data,
  });
}

// 分段线性变换
export function linearChange(data) {
  return request({
    url: "/linearChange/",
    method: "post",
    data,
  });
}

// 对比度拉伸
export function contrast(data) {
  return request({
    url: "/contrast/",
    method: "post",
    data,
  });
}

// 椒盐噪声
export function addSaltPepper(data) {
  return request({
    url: "/addSaltPepper/",
    method: "post",
    data,
  });
}

// 高斯噪声
export function addGaussian(data) {
  return request({
    url: "/addGaussian/",
    method: "post",
    data,
  });
}

// Motion/Disk模糊操作
export function motion(data) {
  return request({
    url: "/motion/",
    method: "post",
    data,
  });
}

// 维纳滤波
export function wiener(data) {
  return request({
    url: "/wiener/",
    method: "post",
    data,
  });
}


// 自适应中值滤波
export function selfMedian(data) {
  return request({
    url: "/selfMedian/",
    method: "post",
    data,
  });
}

// 自适应均值滤波
export function selfMean(data) {
  return request({
    url: "/selfMean/",
    method: "post",
    data,
  });
}

//Otsu，基本全局阈值分割
export function partition(data) {
  return request({
    url: "/partition/",
    method: "post",
    data,
  });
}

export function AreaGrow(data) {
  return request({
    url: "/AreaGrow/",
    method: "post",
    data,
  });
}
//边缘检测
export function edge(data) {
  return request({
    url: "/edge/",
    method: "post",
    data,
  });
}


// 平滑滤波（中值/均值）
export function filter(data) {
  return request({
    url: "/filter/",
    method: "post",
    data,
  });
}

// 锐化滤波
export function sharpenOne(data) {
  return request({
    url: "/sharpenOne/",
    method: "post",
    data,
  });
}
export function sharpenTwo(data) {
  return request({
    url: "/sharpenTwo/",
    method: "post",
    data,
  });
}

// 傅里叶变换
export function fft(data) {
  return request({
    url: "/fft/",
    method: "post",
    data,
  });
}

// 低通滤波
export function lowFilter(data) {
  return request({
    url: "/lowFilter/",
    method: "post",
    data,
  });
}

// 高通滤波
export function highFilter(data) {
  return request({
    url: "/highFilter/",
    method: "post",
    data,
  });
}

// RGB转HSI
export function rgbToHSI(data) { 
  return request({
    url: "/rgbToHSI/",
    method: "post",
    data,
  });
}

//彩图分割
export function edgeColor(data) {
  return request({
    url: "/edgeColor/",
    method: "post",
    data,
  });
}