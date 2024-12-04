<template>
  <v-card-text class="body-1 font-weight-medium text-center">
    <div class="factor">
      <div class="tooltip">
        태양 &amp; 휴식
        <span class="tooltiptext">따뜻한 날씨와 일광욕을 좋아하고 추운 날씨, 비 오는 날, 붐비는 장소를 싫어하는 신경질적인 태양 애호가</span>
      </div>
      - 점수 = {{ profile.F1 }}
    </div>
    <div class="factor">
      <div class="tooltip">
        지식 &amp; 여행
        <span class="tooltiptext">게으름 피우기보다는 단체 여행과 지식 습득을 좋아하는 개방적이고 교육적이며 잘 조직된 관광객</span>
      </div>
      - 점수 = {{ profile.F2 }}
    </div>
    <div class="factor">
      <div class="tooltip">
        독립 &amp; 역사
        <span class="tooltiptext">삶의 의미를 찾고 역사와 전통에 관심이 있으며 조직된 여행보다는 독립적인 여행을 좋아하는 독립적인 관광객</span>
      </div>
      - 점수 = {{ profile.F3 }}
    </div>
    <div class="factor">
      <div class="tooltip">
        문화 &amp; 향유
        <span class="tooltiptext">외향적이고 문화와 역사를 사랑하며 좋은 음식과 와인을 즐기는 고급 관광객</span>
      </div>
      - 점수 = {{ profile.F4 }}
    </div>
    <div class="factor">
      <div class="tooltip">
        사회 &amp; 스포츠
        <span class="tooltiptext">현지인들과 어울리기를 좋아하고 관광객이 많은 지역을 싫어하는 개방적인 스포츠 여행객</span>
      </div>
      - 점수 = {{ profile.F5 }}
    </div>
    <div class="factor">
      <div class="tooltip">
        액션 &amp; 재미
        <span class="tooltiptext">액션, 파티, 독점성을 좋아하고 조용하고 평화로운 장소를 피하는 제트 세터</span>
      </div>
      - 점수 = {{ profile.F6 }}
    </div>
    <div class="factor">
      <div class="tooltip">
        자연 &amp; 휴양
        <span class="tooltiptext">일상 생활에서 벗어나고 싶어하며 붐비는 장소와 대도시를 피하는 자연과 고요함을 사랑하는 사람</span>
      </div>
      - 점수 = {{ profile.F7 }}
    </div>
  </v-card-text>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "SevenFactors",
  data() {
    return {};
  },
  computed: mapState(["profile"])
};
</script>

<style scoped>
/* 툴팁 컨테이너 */
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted #C51162;
  /* 호버 가능한 텍스트 아래 점선 */
  font-weight: bold;
}

/* 툴팁 텍스트 */
.tooltip .tooltiptext {
  visibility: hidden;
  width: 300px;
  background-color: #C51162;
  color: #fff;
  text-align: justify !important;
  border-radius: 6px;
  padding: 5px;

  /* 툴팁 위치 */
  position: absolute;
  z-index: 1;
  bottom: 100%;
  left: 50%;
  margin-left: -120px;
}

/* 툴팁 컨테이너에 마우스를 올리면 툴팁 텍스트 표시 */
.tooltip:hover .tooltiptext {
  visibility: visible;
}
</style>
