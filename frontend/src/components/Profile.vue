<template>
  <div id="profile">
    <div class="hidden-md-and-up">
      <apexchart type="radar" height="335" :options="chartOptionsMobile" :series="getProfileSeries" />
    </div>
    <div class="hidden-sm-and-down">
      <apexchart type="radar" :options="chartOptionsDesktop" :series="getProfileSeries" />
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Profile",
  data() {
    return {
      chartOptionsMobile: {
        chart: {
          toolbar: {
            show: false
          }
        },
        labels: [
          "태양-휴식",
          "지식-여행",
          "독립-역사",
          "문화-향유",
          "사회-스포츠",
          "액션-재미",
          "자연-레크리에이션"
        ],
        yaxis: {
          max: 100,
          min: 0,
          labels: {
            style: {
              fontSize: "12px",
              color: "#A9A9A9"
            }
          }
        },
        xaxis: {
          labels: {
            style: {
              colors: ["000", "000", "000", "000", "000", "000", "000"],
            }
          }
        },
        markers: {
          size: 6,
          hover: {
            size: 8
          }
        },
        tooltip: {
          custom: ({ series, seriesIndex, dataPointIndex, w }) => {
            var longLabels = [
              "태양 & 휴식",
              "지식 & 여행",
              "독립 & 역사",
              "문화 & 향유",
              "사회 & 스포츠",
              "액션 & 재미",
              "자연 & 레크리에이션"
            ];
            return (
              '<div class="profileTooltip">' +
              "<span>" +
              longLabels[dataPointIndex] +
              ": " +
              series[seriesIndex][dataPointIndex] +
              "</span>" +
              "</div>"
            );
          }
        },
        plotOptions: {
          radar: {
            polygons: {
              strokeColor: "#e8e8e8",
              fill: {
                colors: ["#f8f8f8", "#fff"]
              }
            }
          }
        }
      },
      chartOptionsDesktop: {
        chart: {
          toolbar: {
            show: false
          }
        },
        labels: [
          "태양 & 휴식",
          "지식 & 여행",
          "독립 & 역사",
          "문화 & 향유",
          "사회 & 스포츠",
          "액션 & 재미",
          "자연 & 레크리에이션"
        ],
        yaxis: {
          max: 100,
          min: 0,
          labels: {
            style: {
              color: "#A9A9A9",
              fontSize: '12px'
            }
          }
        },
        xaxis: {
          labels: {
            style: {
              colors: ["000", "000", "000", "000", "000", "000", "000"],
              fontSize: '14px'
            }
          }
        },
        markers: {
          size: 6,
          hover: {
            size: 8
          }
        },
        tooltip: {
          custom: ({ series, seriesIndex, dataPointIndex, w }) => {
            var longLabels = [
              "태양 & 휴식",
              "지식 & 여행",
              "독립 & 역사",
              "문화 & 향유",
              "사회 & 스포츠",
              "액션 & 재미",
              "자연 & 레크리에이션"
            ];
            return (
              '<div class="profileTooltip">' +
              "<span>" +
              longLabels[dataPointIndex] +
              ": " +
              series[seriesIndex][dataPointIndex] +
              "</span>" +
              "</div>"
            );
          }
        },
        plotOptions: {
          radar: {
            polygons: {
              strokeColor: "#e8e8e8",
              fill: {
                colors: ["#f8f8f8", "#fff"]
              }
            }
          }
        }
      }
    };
  },
  computed: mapGetters(["getProfileSeries"])
};
</script>

<style>
.profileTooltip {
  background-color: #C51162;
  color: #fff;
  border-radius: 6px;
  padding: 5px;
  font-size: 16px;
}

.hidden-sm-and-down {
  margin-bottom: -100px;
  margin-top: -30px;
}

.hidden-md-and-up {
  margin-bottom: -30px;
}

.hidden-sm-and-down .apexcharts-canvas {
  position: absolute;
  left: -35px;
}
</style>