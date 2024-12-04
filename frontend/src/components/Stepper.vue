<template>
  <v-stepper :value="stepNumber" alt-labels tile>
    <v-stepper-header>
      <v-stepper-step step="1">소개</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="2">사진 업로드</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="3">프로필</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="4">추천</v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="5">마지막</v-stepper-step>
    </v-stepper-header>
  </v-stepper>
</template>

<script>
export default {
  name: "Stepper",
  props: ['stepNumber']
}
</script>

<style scoped></style>