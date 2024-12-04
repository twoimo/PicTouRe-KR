<template>
  <v-container fluid pa-0 ma-0 style="height: 100%;">
    <Stepper stepNumber="1"></Stepper>
    <v-card tile height="100%">
      <v-card class="mx-auto" max-width="900" flat>
        <v-card-title class="headline font-weight-medium">한 장의 사진은 천 마디 말보다 낫다</v-card-title>
        <v-card-subtitle class="subtitle-1 font-weight-medium">더 많은 사진은 더 좋습니다</v-card-subtitle>
        <v-alert color="#C51162" dark icon="mdi-axis-arrow" prominent>이 애플리케이션을 통해 자신의 사진이나 좋아하는 사진을 사용하여 여행 프로필을 결정할 수
          있습니다.</v-alert>
        <v-alert color="#C51162" dark icon="mdi-map-marker" prominent>여행 프로필을 기반으로 관광지 추천을 제공합니다.</v-alert>
        <v-card-text class="body-1 font-weight-medium text-justify">
          <p>
            우리는
            <i>“한 장의 사진은 천 마디 말보다 낫다”</i>라는 격언을 따르며, 사진을 사용하여 사용자의 여행 프로필, 즉 7요인 표현을 결정합니다.
            <a href="/#/sevenfactormodel" target="blank_">7요인 모델</a>은 여행자의 선호도와 성격을 포착하는 잘 확립된 프레임워크입니다.
            또한, 결정된 여행 프로필에 따라 관광지 추천을 제공합니다.
          </p>
          <p>사용자 연구에 참여해 주셔서 대단히 감사합니다. 귀하의 응답은 우리의 연구에 크게 기여할 것입니다.</p>
        </v-card-text>
        <v-alert icon="mdi-shield-lock-outline" prominent text type="info" class="text-justify">
          수집된 모든 데이터는 즉시 익명화되며 개인에게 추적될 수 없습니다.
          데이터는 연구 및 출판에 사용됩니다.
          업로드된 사진은 언제든지 저장되지 않습니다.
          TU Wien의 개인정보 보호 및 데이터 보호에 대한 정보는
          <a href="https://www.tuwien.at/en/tu-wien/organisation/service-providers/data-protection-and-document-management/data-protection-at-tu-wien/documents/"
            target="blank_">여기</a>에서 확인할 수 있습니다.
        </v-alert>
        <v-row align="center" justify="center" dense>
          <v-col cols="12" sm="6">
            <v-checkbox v-model="terms" color="primary" style="justify-content: center">
              <template v-slot:label>
                <div>
                  <b>* 사용자 연구에 참여하는 것에 동의합니다</b>
                </div>
              </template>
            </v-checkbox>
          </v-col>
          <v-col class="text-center" cols="12" sm="4">
            <div>
              <v-btn large :disabled="isDisabled" color="primary" @click="startSurvey()">시작</v-btn>
            </div>
          </v-col>
        </v-row>
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
import Stepper from "../components/Stepper";
export default {
  components: {
    Stepper
  },
  data() {
    return {
      terms: false,
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
    formData.append("step", 1);
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
  computed: {
    isDisabled() {
      return !this.terms;
    }
  },
  methods: {
    startSurvey() {
      this.$router.push({ name: "imageselection" });
    }
  }
};
</script>
