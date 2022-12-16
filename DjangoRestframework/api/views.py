import re
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from lib.utils.json_response import success
from lib.manage.imageProcess import *
from api.models import Image
from api.serializers import ImageSerializer


def getISP(request):
    images = Image.objects.get(id=request.data.get('id'))
    serializer = ImageSerializer(images, context={'request': request})
    path = re.search(r'media/(.*)', serializer.data['file']).group()
    return serializer, path


class index(APIView):
    def get(self, request):
        return success('已连接至服务器,可以进行图像处理')


class ImageSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def retrieve(self, request, *args, **kwargs):
        print('retrieve',request)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return success(serializer.data)

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset()
        serializer = self.get_serializer(instance, many=True)
        return success(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return success(serializer.data)


class new_(APIView):
    def post(self, request):
        serializer, path = getISP(request)

        ori_path = re.search(r'media/(.*)', serializer.data['ori_file']).group()
        get_new(path, ori_path)
        
        return success(serializer.data)


class resize(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        zoomXValue = request.data.get("zoomXValue")
        zoomYValue = request.data.get("zoomYValue")
        imageResize(zoomXValue, zoomYValue, path)
        
        return success(serializer.data)


class getHistArray(APIView):
    def post(self, request):
        serializer, path = getISP(request)

        histArray = get_hist_dict(path)
        
        return success(histArray)


class reverseChange(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        opera('reverse', dict)

        return success(serializer.data)


class linearChange(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        dict['a'] = int(request.data.get('inputA'))
        dict['b'] = int(request.data.get('inputB'))
        dict['c'] = int(request.data.get('inputC'))
        dict['d'] = int(request.data.get('inputD'))
        opera('gray_three_linear_trans', dict)

        return success(serializer.data)


class contrast(APIView):
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        opera('contrast_stretching', dict)
        
        return success(serializer.data)


class rotate(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        dict['angle'] = request.data.get('rotateValue')
        opera('rotate', dict)
        
        return success(serializer.data)


class translate(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        dict['x'] = request.data.get('transXValue')
        dict['y'] = request.data.get('transYValue')
        opera('shift_img', dict)
        
        return success(serializer.data)


class logChange(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        opera('log', dict)
        
        return success(serializer.data)


class reversal(APIView): 
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        temp = request.data.get('spinXYVaue')
        if temp == 'X':
            dict['x_flip'] = True
            dict['y_flip'] = False
        else:
            dict['x_flip'] = False
            dict['y_flip'] = True
        opera('flip', dict)
        
        return success(serializer.data)


class gammaChange(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        dict['gamma'] = eval(request.data.get('inputGamma'))
        opera('gamma', dict)
        
        return success(serializer.data)


class histogramToBalance(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        opera('hist_equal', dict)
        
        return success(serializer.data)


class addSaltPepper(APIView): 
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['pa'] = request.data.get('zoomPepperValue')
        dict['pb'] = request.data.get('zoomSaltValue')
        opera('salt_pepper_noise', dict)
        
        return success(serializer.data)


class addGaussian(APIView): 
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['mean'] = float(request.data.get('inputMean'))
        dict['var'] = float(request.data.get('inputVariance'))
        opera('gaussian_noise', dict)
        
        return success(serializer.data)


class motion(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        if request.data.get('inputMotionDistance') == '':
            dict['dist'] = 0
        else:
            dict['dist'] = float(request.data.get('inputMotionDistance'))
        if request.data.get('inputMotionAngle') == '':
            dict['angle'] = 0
        else:
            dict['angle'] = float(request.data.get('inputMotionAngle'))
        if request.data.get('inputMotionRadius') == '':
            dict['radius'] = 0
        else:
            dict['radius'] = float(request.data.get('inputMotionRadius'))
        opera('motion_disk_Blur', dict)
        
        return success(serializer.data)


class wiener(APIView):
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['dist'] = int(request.data.get('inputPSFDistance'))
        dict['angle'] = int(request.data.get('inputPSFAngle'))
        dict['nsr'] = float(request.data.get('inputNSRRadius'))
        dict['ValueOfwienerOrsmooth'] = request.data.get('ValueOfwienerOrsmooth')
        opera('wienerFilter', dict)
        
        return success(serializer.data)



class selfMedian(APIView):
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        opera('adaptive_median', dict)
        
        return success(serializer.data)


class selfMean(APIView): 
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        opera('adaptive_mean', dict)
        
        return success(serializer.data)


class filter(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        dict['op_name'] = request.data.get('ValueOfMeanOrMedian')
        temp = int(request.data.get('inputMeanOrMedianSize'))
        if (temp % 2 == 0):
            temp += 1
        dict['ksize'] = temp
        opera('filter', dict)
        
        return success(serializer.data)


class sharpenOne(APIView):
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['ValueOfSharpen'] = request.data.get('pathValueOfSharpenOne')
        opera('sharpen1', dict)

        return success(serializer.data)


class sharpenTwo(APIView): 
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['ValueOfSharpen'] = request.data.get('ValueOfSharpenTwo')
        dict['inputSharpenSize'] = int(request.data.get('inputSharpenSize'))
        opera('sharpen2', dict)
        
        return success(serializer.data)


class fft(APIView): 
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['ValueOfmagnitudeOrphase'] = request.data.get('ValueOfmagnitudeOrphase')
        opera('fft2change', dict)
        
        return success(serializer.data)


class lowFilter(APIView):
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['ValueOfFilter'] = request.data.get('ValueOfLowFilter')
        dict['inputThreshold'] = int(request.data.get('inputLowThreshold'))
        if request.data.get('inputLowButter') != '':
            dict['n'] = int(request.data.get('inputLowButter'))
        opera('lowFilter', dict)
        
        return success(serializer.data)


class highFilter(APIView): 
    def post(self, request):
        serializer, path = getISP(request)

        dict = {}
        dict['filepath'] = path
        dict['ValueOfFilter'] = request.data.get('ValueOfHighFilter')
        dict['inputThreshold'] = int(request.data.get('inputHighThreshold'))
        if request.data.get('inputHighButter') != '':
            dict['n'] = int(request.data.get('inputHighButter'))
        opera('highFilter', dict)
        
        return success(serializer.data)


class partition(APIView):
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['ValueOfOtsuOrGlobal'] = request.data.get('ValueOfOtsuOrGlobal')
        opera('OtsuOrGlobal', dict)
        
        return success(serializer.data)


class rgbToHSI(APIView): 
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['ValueOfRGBToHSI'] = request.data.get('ValueOfRGBToHSI')
        opera('rgb2hsi', dict)
        
        return success(serializer.data)


class edge(APIView):  
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['ValueOfEdge'] = request.data.get('ValueOfEdge')
        dict['inputEdgeKernel'] = int(request.data.get('inputEdgeKernel'))
        dict['inputEdgeThreshold'] = int(request.data.get('inputEdgeThreshold'))
        opera('edge', dict)
        
        return success(serializer.data)


class edgeColor(APIView):
    def post(self, request):
        serializer, path = getISP(request)
        
        dict = {}
        dict['filepath'] = path
        dict['ValueOfEdge'] = request.data.get('ValueOfEdgeColor')
        dict['inputEdgeKernel'] = int(request.data.get('inputEdgeColorKernel'))
        dict['inputEdgeThreshold'] = int(request.data.get('inputEdgeColorThreshold'))
        opera('edge', dict)
        
        return success(serializer.data)


class AreaGrow(APIView):
    def post(self, request):
        serializer, path = getISP(request)
    
        dict = {}
        dict['filepath'] = path
        if request.data.get('ValueOfAreaGrow') == 'AreaGrow':
            dict['thresh'] = int(request.data.get('inputAreaGrow'))
            opera('regional_growth', dict)
        
        return success(serializer.data)
