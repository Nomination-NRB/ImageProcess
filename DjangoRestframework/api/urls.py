from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  
router.register('ImageSet', views.ImageSet) 

urlpatterns = [
    path('resize/', views.resize.as_view(), name='resize'),
    path('rotate/', views.rotate.as_view(), name='rotate'),
    path('reversal/', views.reversal.as_view(), name='reversal'),
    path('translate/', views.translate.as_view(), name='translate'),
    path('logChange/', views.logChange.as_view(), name='logChange'),
    path('reverseChange/', views.reverseChange.as_view(), name='reverseChange'),
    path('gammaChange/', views.gammaChange.as_view(), name='gammaChange'),
    path('histogramToBalance/', views.histogramToBalance.as_view(), name='histogramToBalance'),
    path('linearChange/', views.linearChange.as_view(), name='linearChange'),
    path('contrast/', views.contrast.as_view(), name='contrast'),
    path('addSaltPepper/', views.addSaltPepper.as_view(), name='addSaltPepper'),
    path('addGaussian/', views.addGaussian.as_view(), name='addGaussian'),
    path('motion/', views.motion.as_view(), name='motion'),
    path('wiener/', views.wiener.as_view(), name='wiener'),
    path('selfMedian/', views.selfMedian.as_view(), name='selfMedian'),
    path('selfMean/', views.selfMean.as_view(), name='selfMean'),
    path('filter/', views.filter.as_view(), name='filter'),
    path('sharpenOne/', views.sharpenOne.as_view(), name='sharpenOne'),
    path('sharpenTwo/', views.sharpenTwo.as_view(), name='sharpenTwo'),
    path('fft/', views.fft.as_view(), name='fft'),
    path('lowFilter/', views.lowFilter.as_view(), name='lowFilter'),
    path('highFilter/', views.highFilter.as_view(), name='highFilter'),
    path('partition/', views.partition.as_view(), name='partition'),
    path('rgbToHSI/', views.rgbToHSI.as_view(), name='rgbToHSI'),
    path('edge/', views.edge.as_view(), name='edge'),
    path('edgeColor/', views.edgeColor.as_view(), name='edgeColor'),
    path('AreaGrow/', views.AreaGrow.as_view(), name='AreaGrow'),
    path('getHistArray/', views.getHistArray.as_view(), name='getHistArray'),
    path('new_/',views.new_.as_view(),name='new_'),
    path('', views.index.as_view(), name='index'),
]


urlpatterns += router.urls  
