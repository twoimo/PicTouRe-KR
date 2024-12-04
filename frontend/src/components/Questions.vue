<template>
  <v-card class="mx-auto" max-width="900" flat>
    <v-card-title class="headline font-weight-medium">질문</v-card-title>
    <v-card-subtitle class="subtitle-1 font-weight-medium">*로 표시된 항목은 필수입니다</v-card-subtitle>
    <v-alert color="#C51162" dark icon="mdi-format-list-checks" prominent>다음 문장에 대한 동의 수준을 표시해 주세요.</v-alert>
    <v-card-text>
      <v-form class="body-1 text-justify" ref="form" v-model="valid" lazy-validation>
        <span class="question">* 3~7장의 사진을 찾는 것이 쉬웠습니다.</span>
        <v-radio-group v-model="questions.Q1" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="매우 동의하지 않음" value="0"></v-radio>
          <v-radio color="primary" label="동의하지 않음" value="1"></v-radio>
          <v-radio color="primary" label="중립" value="2"></v-radio>
          <v-radio color="primary" label="동의함" value="3"></v-radio>
          <v-radio color="primary" label="매우 동의함" value="4"></v-radio>
        </v-radio-group>
        <span class="question">* 주로 인터넷에서 다운로드한 사진을 사용했습니다 (예: 구글, 플리커 등).</span>
        <v-radio-group v-model="questions.Q2" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="매우 동의하지 않음" value="0"></v-radio>
          <v-radio color="primary" label="동의하지 않음" value="1"></v-radio>
          <v-radio color="primary" label="중립" value="2"></v-radio>
          <v-radio color="primary" label="동의함" value="3"></v-radio>
          <v-radio color="primary" label="매우 동의함" value="4"></v-radio>
        </v-radio-group>
        <span class="question">* 주로 내 사진을 사용했습니다.</span>
        <v-radio-group v-model="questions.Q3" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="매우 동의하지 않음" value="0"></v-radio>
          <v-radio color="primary" label="동의하지 않음" value="1"></v-radio>
          <v-radio color="primary" label="중립" value="2"></v-radio>
          <v-radio color="primary" label="동의함" value="3"></v-radio>
          <v-radio color="primary" label="매우 동의함" value="4"></v-radio>
        </v-radio-group>
        <span class="question">* 7가지 요소에 대한 설명을 이해했습니다.</span>
        <v-radio-group v-model="questions.Q4" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="매우 동의하지 않음" value="0"></v-radio>
          <v-radio color="primary" label="동의하지 않음" value="1"></v-radio>
          <v-radio color="primary" label="중립" value="2"></v-radio>
          <v-radio color="primary" label="동의함" value="3"></v-radio>
          <v-radio color="primary" label="매우 동의함" value="4"></v-radio>
        </v-radio-group>
        <span class="question">* 결과 프로필이 내 선호도와 일치합니다.</span>
        <v-radio-group v-model="questions.Q5" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="매우 동의하지 않음" value="0"></v-radio>
          <v-radio color="primary" label="동의하지 않음" value="1"></v-radio>
          <v-radio color="primary" label="중립" value="2"></v-radio>
          <v-radio color="primary" label="동의함" value="3"></v-radio>
          <v-radio color="primary" label="매우 동의함" value="4"></v-radio>
        </v-radio-group>
        <span class="question">결과 프로필에서 잘 맞지 않는 요소는 무엇입니까? (복수 응답 가능)</span>
        <v-checkbox v-model="questions.Q6_1" color="primary" label="태양 &amp; 휴식"></v-checkbox>
        <v-checkbox v-model="questions.Q6_2" color="primary" label="지식 &amp; 여행"></v-checkbox>
        <v-checkbox v-model="questions.Q6_3" color="primary" label="독립 &amp; 역사"></v-checkbox>
        <v-checkbox v-model="questions.Q6_4" color="primary" label="문화 &amp; 탐닉"></v-checkbox>
        <v-checkbox v-model="questions.Q6_5" color="primary" label="사회 &amp; 스포츠"></v-checkbox>
        <v-checkbox v-model="questions.Q6_6" color="primary" label="액션 &amp; 재미"></v-checkbox>
        <v-checkbox v-model="questions.Q6_7" color="primary" label="자연 &amp; 휴양"></v-checkbox>
        <span class="question">결과 프로필을 어떻게 조정하시겠습니까? (복수 조정 가능)</span>
        <v-row>
          <v-col cols="12">
            <span style="padding-left: 10px;">
              태양 &amp; 휴식 점수
              <b>{{ selfassessment.F1 }}</b>
            </span>
            <v-slider v-model="selfassessment.F1" thumb-label @change="adjusted = true"></v-slider>
          </v-col>
          <v-col cols="12">
            <span style="padding-left: 10px;">
              지식 &amp; 여행 점수
              <b>{{ selfassessment.F2 }}</b>
            </span>
            <v-slider v-model="selfassessment.F2" thumb-label @change="adjusted = true"></v-slider>
          </v-col>
          <v-col cols="12">
            <span style="padding-left: 10px;">
              독립 &amp; 역사 점수
              <b>{{ selfassessment.F3 }}</b>
            </span>
            <v-slider v-model="selfassessment.F3" thumb-label @change="adjusted = true"></v-slider>
          </v-col>
          <v-col cols="12">
            <span style="padding-left: 10px;">
              문화 &amp; 탐닉 점수
              <b>{{ selfassessment.F4 }}</b>
            </span>
            <v-slider v-model="selfassessment.F4" thumb-label @change="adjusted = true"></v-slider>
          </v-col>
          <v-col cols="12">
            <span style="padding-left: 10px;">
              사회 &amp; 스포츠 점수
              <b>{{ selfassessment.F5 }}</b>
            </span>
            <v-slider v-model="selfassessment.F5" thumb-label @change="adjusted = true"></v-slider>
          </v-col>
          <v-col cols="12">
            <span style="padding-left: 10px;">
              액션 &amp; 재미 점수
              <b>{{ selfassessment.F6 }}</b>
            </span>
            <v-slider v-model="selfassessment.F6" thumb-label @change="adjusted = true"></v-slider>
          </v-col>
          <v-col cols="12">
            <span style="padding-left: 10px;">
              자연 &amp; 휴양 점수
              <b>{{ selfassessment.F7 }}</b>
            </span>
            <v-slider v-model="selfassessment.F7" thumb-label @change="adjusted = true"></v-slider>
          </v-col>
        </v-row>
        <span class="question">* 나이는 어떻게 되십니까?</span>
        <v-radio-group v-model="questions.age" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="18세 미만" value="1"></v-radio>
          <v-radio color="primary" label="18 - 24세" value="2"></v-radio>
          <v-radio color="primary" label="25 - 34세" value="3"></v-radio>
          <v-radio color="primary" label="35 - 44세" value="4"></v-radio>
          <v-radio color="primary" label="45 - 55세" value="5"></v-radio>
          <v-radio color="primary" label="55세 이상" value="6"></v-radio>
          <v-radio color="primary" label="말하고 싶지 않음" value="0"></v-radio>
        </v-radio-group>
        <span class="question">* 성별은 무엇입니까?</span>
        <v-radio-group v-model="questions.gender" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="남성" value="1"></v-radio>
          <v-radio color="primary" label="여성" value="2"></v-radio>
          <v-radio color="primary" label="기타" value="3"></v-radio>
          <v-radio color="primary" label="말하고 싶지 않음" value="0"></v-radio>
        </v-radio-group>
        <span class="question">* 최종 학력은 무엇입니까?</span>
        <v-radio-group v-model="questions.education" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="고등학교 졸업 이하" value="1"></v-radio>
          <v-radio color="primary" label="고등학교 졸업" value="2"></v-radio>
          <v-radio color="primary" label="학사 학위" value="3"></v-radio>
          <v-radio color="primary" label="석사 학위" value="4"></v-radio>
          <v-radio color="primary" label="박사 학위" value="5"></v-radio>
          <v-radio color="primary" label="기타" value="6"></v-radio>
          <v-radio color="primary" label="말하고 싶지 않음" value="0"></v-radio>
        </v-radio-group>
        <span class="question">* 여가를 위해 얼마나 자주 여행하십니까?</span>
        <v-radio-group v-model="questions.travel_frequency" :rules="[v => !!v || '필수 항목입니다!']" required column>
          <v-radio color="primary" label="1년에 한 번 미만" value="1"></v-radio>
          <v-radio color="primary" label="1년에 1~2번" value="2"></v-radio>
          <v-radio color="primary" label="1년에 2~3번" value="3"></v-radio>
          <v-radio color="primary" label="1년에 3~4번" value="4"></v-radio>
          <v-radio color="primary" label="1년에 4~5번" value="5"></v-radio>
          <v-radio color="primary" label="1년에 5번 이상" value="6"></v-radio>
          <v-radio color="primary" label="말하고 싶지 않음" value="0"></v-radio>
        </v-radio-group>
        <h3>의견/제안:</h3>
        <v-textarea class="mx-2" label="메시지" v-model="questions.message" rows="3"></v-textarea>
        <v-alert dense outlined type="error" :value="!valid" transition="scale-transition">필수 정보가 누락되었습니다! 모든 필수 항목을 작성해
          주세요 (*로 표시된 항목).</v-alert>
        <v-card-actions>
          <v-spacer></v-spacer>
          <div class="my-2">
            <v-btn @click="formSubmit()" large color="primary">제출</v-btn>
          </div>
        </v-card-actions>
      </v-form>
    </v-card-text>
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
          <v-btn color="primary" text @click="dialog = false">확인</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import axios from "axios";
export default {
  name: "Questions",
  components: {
  },
  data() {
    return {
      valid: true,
      dialog: false,
      adjusted: false
    };
  },
  methods: {
    formSubmit() {
      if (!this.$refs.form.validate()) {
        this.valid = false;
        return;
      }
      const url = "http://127.0.0.1:5000/backend/questions";
      //const url = "/backend/questions";
      const config = {
        headers: {
          "Content-Type": "multipart/form-data" //multipart/form-data"
        }
      };
      const formData = new FormData();
      formData.append("uuid", this.$store.state.id);
      formData.append("Q1", this.questions.Q1);
      formData.append("Q2", this.questions.Q2);
      formData.append("Q3", this.questions.Q3);
      formData.append("Q4", this.questions.Q4);
      formData.append("Q5", this.questions.Q5);
      formData.append("Q6_1", this.questions.Q6_1);
      formData.append("Q6_2", this.questions.Q6_2);
      formData.append("Q6_3", this.questions.Q6_3);
      formData.append("Q6_4", this.questions.Q6_4);
      formData.append("Q6_5", this.questions.Q6_5);
      formData.append("Q6_6", this.questions.Q6_6);
      formData.append("Q6_7", this.questions.Q6_7);
      formData.append("age", this.questions.age);
      formData.append("gender", this.questions.gender);
      formData.append("education", this.questions.education);
      formData.append("travel_frequency", this.questions.travel_frequency);
      formData.append("message", this.questions.message);
      formData.append("adjusted", this.adjusted);
      formData.append("F1", this.selfassessment.F1);
      formData.append("F2", this.selfassessment.F2);
      formData.append("F3", this.selfassessment.F3);
      formData.append("F4", this.selfassessment.F4);
      formData.append("F5", this.selfassessment.F5);
      formData.append("F6", this.selfassessment.F6);
      formData.append("F7", this.selfassessment.F7);

      axios
        .post(url, formData, config)
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "recommendation" });
        })
        .catch(e => {
          console.log(e);
          this.$data.dialog = true;
        });
    }
  },
  computed: {
    questions: {
      get() {
        return this.$store.state.questions;
      },
      set(value) {
        this.$store.commit("updateQuestions", value);
      }
    },
    selfassessment: {
      get() {
        return this.$store.state.profile;
      },
      set(value) {
        this.$store.commit("updateSelfassessment", value);
      }
    }
  }
};
</script>

<style scoped>
#message {
  width: 100%;
  height: 100px;
  font-size: 16px;
}

.question {
  font-style: italic;
  font-weight: bold;
}

h3 {
  padding: 15px 0;
}

.v-input--selection-controls {
  margin-top: 0px !important;
}
</style>