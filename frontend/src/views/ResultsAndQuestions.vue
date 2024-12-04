<template>
  <v-container fluid pa-0 ma-0 style="height: 100%;">
    <Stepper stepNumber="3"></Stepper>
    <v-card tile height="100%">
      <v-card class="mx-auto" max-width="900" flat>
        <v-card-title class="headline font-weight-medium">당신의 프로필</v-card-title>
        <v-card-subtitle class="subtitle-1 font-weight-medium">제공한 사진을 기반으로</v-card-subtitle>
        <Profile />
        <SevenFactors />
        <v-alert icon="mdi-information-outline" prominent text type="info" class="text-justify">
          <p>
            참고로, 사람들은 일곱 가지 요인의 혼합으로 묘사됩니다.
            각 요인은 0에서 100까지의 범위를 가지며, 0은 해당 요인이 전혀 여행 선호도를 반영하지 않음을 의미하고 100은 완벽하게 반영함을 의미합니다.
          </p>
          <p>
            일곱 가지 요인에 대한 간략한 설명은 해당 요인에 마우스를 올리거나(모바일에서는 터치) 확인할 수 있습니다.
            일곱 가지 요인에 대한 자세한 내용은
            <a href="/#/sevenfactormodel" target="blank_">여기</a>에서 확인할 수 있습니다.
          </p>
        </v-alert>
      </v-card>
      <v-divider></v-divider>
      <Questions />
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";
import Profile from "../components/Profile";
import SevenFactors from "../components/SevenFactors";
import Questions from "../components/Questions";
import Stepper from "../components/Stepper";

export default {
  components: {
    Profile,
    SevenFactors,
    Questions,
    Stepper
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
    formData.append("step", 3);
    axios
      .post(url, formData, config)
      .then(response => {
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
        this.$data.dialog = true;
      });
  }
};
</script>

<style scoped></style>