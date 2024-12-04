<template>
  <v-container fluid pa-0 ma-0 style="height: 100%;">
    <Stepper stepNumber="2"></Stepper>
    <v-card tile height="100%">
      <v-card class="mx-auto" max-width="900" flat>
        <v-card-title class="headline font-weight-medium">사진을 업로드하세요</v-card-title>
        <v-card-subtitle class="subtitle-1 font-weight-medium">여행 프로필을 결정하기 위해</v-card-subtitle>
        <v-alert color="#C51162" dark icon="mdi-island" prominent>다음 휴가를 상상해보세요.</v-alert>
        <v-alert color="#C51162" dark icon="mdi-image-multiple" prominent>마음속의 휴가를 잘 설명할 수 있는 사진 3~7장을 선택하세요. 자신의 사진이나
          인터넷에서 다운로드한 사진을 사용할 수 있습니다.</v-alert>
        <v-alert color="#C51162" dark icon="mdi-sort" prominent>선택한 사진을 중요도에 따라 순위를 매기세요. 상위에 있을수록 더 중요합니다.</v-alert>
        <v-alert icon="mdi-information-outline" prominent text type="info" class="text-justify">
          <ul>
            <li>
              사진의 순위를 매기려면, 이동하고 싶은 사진을 클릭하고(모바일에서는 터치) 예상 위치로 이동하세요.
            </li>
            <li>
              사진 업로드 및 처리는 시간이 걸릴 수 있습니다. 인내심을 가져주셔서 감사합니다.
            </li>
            <li>
              업로드된 사진은 절대 저장되지 않는다는 점을 유의하세요!
            </li>
          </ul>
        </v-alert>
        <v-card-title class="headline font-weight-medium">여기에서 선택하고 순위를 매기세요</v-card-title>
        <v-card-subtitle class="subtitle-1 font-weight-medium">그리고 업로드 버튼을 누르세요</v-card-subtitle>
        <ImageUpload />
      </v-card>
    </v-card>
    <v-dialog v-model="dialog" max-width="290">
      <v-card>
        <v-card-title class="headline">오류 발생...</v-card-title>
        <v-card-text class="text-justify">
          문제가 발생했습니다!
          문제가 일시적일 수 있습니다.
          잠시 후 다시 시도해 주세요.
          문제가 지속되면 저희에게 연락해 주세요.
          감사합니다!
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">
            확인
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from "axios";
import ImageUpload from "../components/ImageUpload";
import Stepper from "../components/Stepper";

export default {
  components: {
    ImageUpload,
    Stepper
  },
  data() {
    return {
      dialog: false
    };
  },
  mounted() {
    const url = "http://127.0.0.1:5000/backend/time";
    //const url = "/backend/time";
    const config = {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    };
    const formData = new FormData();
    formData.append("uuid", this.$store.state.id);
    formData.append("step", 2);
    axios
      .post(url, formData, config)
      .then(response => {
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
        this.$data.dialog = true;
      });
  },
};
</script>