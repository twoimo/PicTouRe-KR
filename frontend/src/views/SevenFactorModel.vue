<template>
  <v-container fluid pa-0 ma-0 style="height: 100%;">
    <v-card tile height="100%">
      <v-card class="mx-auto" max-width="900" flat>
        <v-card-title class="headline font-weight-medium">7요인 모델</v-card-title>
        <v-card-subtitle class="subtitle-1 font-weight-medium">사용자는 7가지 여행 행동 요인의 혼합으로 표현됩니다</v-card-subtitle>
        <v-card-text class="body-1 text-justify">
          7요인 모델은 여행자의 선호도와 성격을 포착하기 위한 잘 확립된 프레임워크입니다.
          7요인 모델은 장기적인 사용자 행동과 관련된 "빅 파이브" 성격 특성을 결합한 요인 분석의 결과입니다
          <a href="https://psycnet.apa.org/doiLanding?doi=10.1037%2F0022-3514.59.6.1216" target="_blank">(Goldberg
            1990)</a>
          , 그리고 단기적인 선호도를 나타내는 17가지 관광 역할을 제안한
          <a href="https://www.sciencedirect.com/science/article/pii/S0160738301000378" target="_blank">Gibson and
            Yiannakis (2002)</a>
          . 이러한 요인은 7차원 벡터 공간의 기초를 형성하며, 태양 &amp; 휴식, 지식 &amp; 여행, 독립 &amp; 역사, 문화 &amp; 탐닉, 사회 &amp; 스포츠, 액션 &amp; 재미,
          자연 &amp; 휴양으로 요약된 여행 행동 패턴을 나타냅니다.
          또한, 각 사용자는 7요인의 혼합으로 표현됩니다
          <a href="https://link.springer.com/article/10.1007/s40558-014-0017-5" target="_blank">(Neidhadt et al.
            2015)</a>
          .
        </v-card-text>
        <v-img src="@/assets/seven_factors.png" />
        <v-card-text class="body-1">
          <h3>F1 - 태양 &amp; 휴식</h3>
          <p>
            <b style="color: green">좋아하는 것:</b>
            따뜻한 날씨, 태양, 일광욕, 접근성
          </p>
          <p>
            <b style="color: red">싫어하는 것:</b>
            추운 날씨나 비 오는 날씨, 붐비는 장소
          </p>
          <p>
            <b style="color: blue">당신은:</b>
            새로운 아이디어가 많고, 독창적이며, 효율적이고, 때때로 스트레스를 받고, 기분이 변덕스러운 사람
          </p>

          <h3>F2 - 지식 &amp; 여행</h3>
          <p>
            <b style="color: green">좋아하는 것:</b>
            지식 습득, 워크숍, 강좌 수강
          </p>
          <p>
            <b style="color: red">싫어하는 것:</b>
            아무것도 하지 않는 것, 해변에 누워 있는 것, 발견하거나 경험할 것이 없는 것
          </p>
          <p>
            <b style="color: blue">당신은:</b>
            교육 지향적이고, 도움을 주며 이타적이고, 의사소통이 원활하고 개방적이며, 용서하는 성격
          </p>

          <h3>F3 - 독립 &amp; 역사</h3>
          <p>
            <b style="color: green">좋아하는 것:</b>
            독립적인 여행, 전통 &amp; 역사, 유명한 장소, 삶의 의미 발견
          </p>
          <p>
            <b style="color: red">싫어하는 것:</b>
            조직된 투어 &amp; 여행, 시끄럽고 붐비는 행사
          </p>
          <p>
            <b style="color: blue">당신은:</b>
            개방적이고, 탐구자이며, 철학적이고, 감상적이며, 사색가이고, 유연하며, 호기심이 많은 사람
          </p>

          <h3>F4 - 문화 &amp; 탐닉</h3>
          <p>
            <b style="color: green">좋아하는 것:</b>
            역사, 예술, 문화, 일류 호텔 &amp; 여행, 고급 레스토랑
          </p>
          <p>
            <b style="color: red">싫어하는 것:</b>
            패스트푸드, 저예산 호텔, 유스호스텔
          </p>
          <p>
            <b style="color: blue">당신은:</b>
            교육받은 사람, 미식가, 에너지가 넘치는 사람, 열정적이고 호기심이 많은 사람
          </p>

          <h3>F5 - 사회 &amp; 스포츠</h3>
          <p>
            <b style="color: green">좋아하는 것:</b>
            현지 사람들과 교류, 현지 음식 맛보기, 언어 배우기 및 현지인과의 접촉
          </p>
          <p>
            <b style="color: red">싫어하는 것:</b>
            일반적인 관광 경로, 큰 소음이 나는 클럽 및 장소
          </p>
          <p>
            <b style="color: blue">당신은:</b>
            운동을 좋아하고, 사회적이며, 자연스럽고, 에너지와 긍정적인 기운이 넘치는 사람
          </p>

          <h3>F6 - 액션 &amp; 재미</h3>
          <p>
            <b style="color: green">좋아하는 것:</b>
            액션, 화려한 밤 생활, 독점 이벤트, VIP 파티
          </p>
          <p>
            <b style="color: red">싫어하는 것:</b>
            조용한 장소
          </p>
          <p>
            <b style="color: blue">당신은:</b>
            스릴을 추구하고, 삶을 즐기며, 도전을 찾고, 약간 시끄럽고, 활발한 사람
          </p>

          <h3>F7 - 자연 &amp; 휴양</h3>
          <p>
            <b style="color: green">좋아하는 것:</b>
            자연의 고요함과 평화, 마음을 정리하는 것, 휴식과 휴식 취하기
          </p>
          <p>
            <b style="color: red">싫어하는 것:</b>
            붐비는 장소, 대도시와 대도시
          </p>
          <p>
            <b style="color: blue">당신은:</b>
            완전히 편안하고, 몸과 마음이 균형 잡힌 사람, 점잖고, 서두르지 않는 사람
          </p>
        </v-card-text>
      </v-card>
    </v-card>
  </v-container>
</template>

<script>
export default {};
</script>

<style scoped></style>