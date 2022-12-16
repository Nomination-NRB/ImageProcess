<template>
  <div class="container">
    <div class="mainView">
      <el-button @click="newHandler" type="primary" style="align-items: center; margin-left: 92%">
        <el-icon size="mini">
          <Setting />
        </el-icon>
        复原
      </el-button>
      <div class="stepView">

        <div class="stepContent" :style="{
          transform: 'translateX(' + -stepStatusActive * 1200 + 'px)',
        }">
          <div class="viewContent">
            <div class="leftContent">
              <div class="imageShowView">
                <el-popover placement="bottom" title="图像" :width="200" trigger="hover" content="原始图像,点击上传">
                  <template #reference>
                    <!-- 上传图像 -->
                    <el-upload action="/ImageSet/" class="avatar-uploader" :http-request="uploadImg"
                      :on-success="handleImgSuccess" :show-file-list="false">
                      <el-image v-if="oriImageUrl" :src="oriImageUrl" fit="contain" class="avatar-uploader" />
                      <el-icon v-else class="avatar-uploader-icon">
                        <Plus />
                      </el-icon>
                    </el-upload>
                  </template>
                </el-popover>
                <el-popover placement="bottom" title="图像" :width="200" trigger="hover" content="处理后的图像，点击查看大图">
                  <template #reference>
                    <!-- 处理的预览图像 -->
                    <el-image @click="openImageHandler" :src="modImageUrl" fit="contain" class="avatar-uploader image">
                    </el-image>
                  </template>
                </el-popover>
              </div>
              <div class="zhifang">
                <chartView style="margin-top: 8px; width: 580px; height: 340px" :chart-option="chartOpt"
                  :auto-resize="true" height="100%" />
              </div>
            </div>
            <div class="rightContent">
              <panel v-if="imageID" @refresh="refreshHandle" />
              <el-skeleton v-else :rows="16" animated />
            </div>
          </div>
        </div>
      </div>
    </div>

    <el-dialog v-model="centerDialogVisible" title="提示" width="30%" center>
      <span>{{ centerDialogContent }}</span>
      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="centerDialogVisibleHandler">确定</el-button>
        </span>
      </template>
    </el-dialog>
    <el-dialog v-model="imageDialogVisible" title="图像" fullscreen>
      <el-image :src="modImageUrl" fit="contain" style="width: 100%; height: 100%" />
      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="imageDialogVisible = false">关闭</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import {
  Plus,
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from "@element-plus/icons-vue";
import { ElNotification, UploadProps, ElLoading } from "element-plus";
import * as API from "@/api/resolve";
import panel from "@/views/home/components/panel";

import { chartView } from "@/components/chart";

export default {
  components: {
    Plus,
    Document,
    IconMenu,
    Location,
    Setting,
    panel,
  },
  created() {
    this.chartOpt = this.$eChartFn.testBar({ r: [], g: [], b: [], gray: [] });
  },
  data() {
    return {
      chartOpt: {},
      stepStatusActive: 0,
      oriImageUrl: "",
      modImageUrl: "",
      imageID: null,
      centerDialogVisible: false,
      activeIndex: "0",
      imageDialogVisible: false,
    };
  },
  computed: {},
  watch: {},
  mounted() {
    this.init();
  },
  methods: {
    async init() {
      let { data: helloData } = await API.hello();
      if (helloData) {
        ElNotification({
          title: "你好！",
          message: helloData + "请先上传图片，随后操作面板将打开",
          type: "success",
        });
      }
    },

    async newHandler() {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      let _id = this.$store.getters.id;
      //以上为必备操作

      //针对不同操作调用不同API即可
      let res = await API.new_({
        id: _id,
      });
      this.refreshHandle()
      loading.close()
      ElNotification({
        title: "操作成功",
        message: "图片已复原",
        type: "success",
      });
    },

    async refreshHandle() {
      let { data: histData } = await API.getHistArray({
        id: this.imageID,
      });
      // console.log("完成后获取的直方图：", histData);
      this.modImageUrl = this.$store.getters.url + "?date=" + String(Date.now());
      this.chartOpt = this.$eChartFn.testBar(histData);
      this.$forceUpdate();
    },

    async handleImgSuccess(response, uploadFile) {
      let loading = ElLoading.service({
        lock: true,
        text: "处理中...",
        background: "rgba(255, 255, 255, 0.2)",
      });
      // console.log(response, uploadFile);
      this.oriImageUrl = URL.createObjectURL(uploadFile);
      this.modImageUrl = response.data.file;
      this.imageID = response.data.id;
      this.$store.commit("image/SET_ID", response.data.id);
      this.$store.commit("image/SET_URL", response.data.file);

      let { data: histData } = await API.getHistArray({
        id: this.imageID,
      });
      // console.log("上传图片后首次获取的直方图：", histData);
      this.chartOpt = this.$eChartFn.testBar(histData);
      loading.close();
      ElNotification({
        title: "上传成功",
        message: "图像上传成功,可以开始图像处理",
        type: "success",
      });
    },
    uploadImg(param) {
      // console.log("待上传的图像：", param);
      const formData = new FormData();
      formData.append("file", param.file);
      formData.append("ori_file", param.file);
      API.uploadImage(formData).then((res) => {
        this.handleImgSuccess(res, param.file);
      });
    },
    beforeImgUpload(rawFile) {
      // console.log("beforeImgUpload", rawFile);
      if (rawFile.type !== "image/jpeg") {
        ElMessage.error("Avatar picture must be JPG format!");
        return false;
      }
      return true;
    },
    openImageHandler() {
      this.imageDialogVisible = true;
    },
  },
};
</script>

<style scoped>
.el-menu-demo {
  width: 100%;
}

.image {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
}

.imageShowView {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.rightContent {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.leftContent {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.avatar-uploader {
  width: 270px;
  height: 270px;
}

.avatar-uploader .avatar {
  width: 270px;
  height: 270px;
  display: block;
}

.avatar-uploader .el-upload {
  border: 1px dashed var(--el-border-color);
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
  border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 270px;
  height: 270px;
  text-align: center;
}

.container {
  min-width: 1280px;
  position: relative;
  width: 100%;
  background-color: #f4f6fc;
  height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* 伪元素 */
.container::after {
  content: "";
  position: absolute;
  height: 2000px;
  width: 2000px;
  top: -10%;
  right: 48%;
  transform: translateY(-50%);
  /* background-image: linear-gradient(-45deg, #4481eb 0%, #04befe 100%); */
  transition: 1.8s ease-in-out;
  border-radius: 50%;
  filter: blur(1px);
  animation: color-change-5x 12s linear infinite alternate both,
    wave 12s linear infinite alternate both;
}

.viewTitle {
  position: absolute;
  top: 1%;
  left: 50%;
  transform: translateX(-50%);
  font-weight: bolder;
  font-size: 36px;
  color: #2d66f6;
  background-color: rgba(255, 255, 255, 0);
  backdrop-filter: blur(2px);
  padding: 5px;
  border-bottom: 2px solid #2d66f6;
}

.viewPic {
  z-index: 20;
  position: absolute;
  width: 200px;
  height: 200px;
  bottom: 0;
  left: 20px;
}

.mainView {
  opacity: 0.99;
  z-index: 10;
  height: 720px;
  width: 1240px;
  background-color: #fff;
  border-radius: 20px;
  box-sizing: border-box;
  padding: 10px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.stepView {
  position: relative;
  margin-top: 15px;
  width: 1200px;
  height: 90%;
  background: #fff;
  overflow: hidden;
}

.viewContent {
  position: absolute;
  width: 1200px;
  height: 100%;
  transition: 0.5s ease-in-out;
  display: flex;
  flex-direction: row;
}

.cell-item {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: auto;
}

.doneView {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
}

.doneViewLeft {
  width: 40%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.doneViewRight {
  width: 60%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title {
  font-size: 28px;
  color: #2d66f6;
  font-weight: bold;
  padding: 5px;
}

.tipsContent {
  font-size: 18px;
  padding: 5px;
  font-weight: bold;
}

.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
}

@keyframes color-change-5x {
  0% {
    background: #2d67f6;
  }

  50% {
    background: #4481eb;
  }

  100% {
    background: #04befe;
  }
}

@keyframes wave {
  0% {
    transform: translateY(-50%);
    transform: translateX(0);
  }

  100% {
    transform: translateY(-20%);
    transform: translateX(20%);
  }
}
</style>
