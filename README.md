# PicTouRe

PicTouRe는 사진 기반의 관광 추천 시스템입니다. 이 시스템은 사람들이 여행 결정을 내리는 초기 단계에서 자신의 관광 선호도를 명확히 표현하는 데 어려움을 겪는 문제를 해결하고자 합니다. "한 장의 사진이 천 마디 말을 대신한다"는 속담을 따르며, PicTouRe는 사진을 사용하여 사람들의 관광 선호도를 암묵적으로 파악합니다. 사용자가 업로드한 사진을 분석해 그들의 여행 선호도를 쉽게 이해할 수 있는 프로파일로 만듭니다. PicTouRe를 사용해 보시려면 [여기](https://pictoprof.ec.tuwien.ac.at)로 방문하세요. 또한 데모 영상을 [YouTube](https://youtu.be/xZnXLPcenEs)에서 볼 수 있습니다. 자세한 내용은 [여기](https://doi.org/10.1145/3383313.3411526)에서 확인할 수 있습니다.



저희 연구를 인용할 때는 다음과 같이 해주세요:
```bibtex
@inproceedings{sertkan2020_pictoure,
	title        = {PicTouRe - A Picture-Based Tourism Recommender},
	author       = {Sertkan, Mete and Neidhardt, Julia and Werthner, Hannes},
	year         = 2020,
	booktitle    = {Proceedings of the 14th ACM Conference on Recommender Systems},
	location     = {Virtual Event, Brazil},
	publisher    = {Association for Computing Machinery},
	address      = {New York, NY, USA},
	series       = {RecSys '20},
	pages        = {597–599},
	doi          = {10.1145/3383313.3411526},
	isbn         = 9781450375832,
	url          = {https://doi.org/10.1145/3383313.3411526},
	numpages     = 3,
	keywords     = {travel-behaviour, picture-based, preference elicitation, tourism, tourist}
}
```

저희는 PicTouRe의 성능을 평가하기 위해 81명을 대상으로 한 연구를 진행했으며, 사진 모음을 통해 사용자의 여행 선호도를 정확히 파악할 수 있음을 확인했습니다. 자세한 사항은 연구논문을 [여기](https://arxiv.org/pdf/2006.05172.pdf)에서 확인하세요. 

연구를 인용할 때는 다음과 같이 해주세요:
```bibtex
@inproceedings{sertkan2020_elicit,
	title        = {Eliciting Touristic Profiles: A User Study on Picture Collections},
	author       = {Sertkan, Mete and Neidhardt, Julia and Werthner, Hannes},
	year         = 2020,
	booktitle    = {Proceedings of the 28th ACM Conference on User Modeling, Adaptation and Personalization},
	location     = {Genoa, Italy},
	publisher    = {Association for Computing Machinery},
	address      = {New York, NY, USA},
	series       = {UMAP '20},
	pages        = {230–238},
	doi          = {10.1145/3340631.3394868},
	isbn         = 9781450368612,
	url          = {https://doi.org/10.1145/3340631.3394868},
	numpages     = 9,
	keywords     = {picture-based, travel-behaviour, preference elicitation, tourist, tourism}
}
```

# 백엔드
먼저 백엔드 폴더로 이동하세요. `cd backend`. 제공된 `environment.yml`을 사용하여 필요한 패키지가 있는 새로운 conda 환경을 생성하고, 그 다음에 새로 생성된 환경을 활성화하는 것을 권장합니다.
```bash
conda env create -n pic2prof --file environment.yml
conda activate pic2prof
```
예측 모델의 가중치를 [여기](https://owncloud.tuwien.ac.at/index.php/s/kotvEsald31Pw51)에서 다운로드하세요. 백엔드에 `models` 폴더를 생성하고 (`mkdir models`), 다운로드한 `*.pth` 파일을 이 디렉토리에 복사하세요.

플라스크 앱을 다음과 같이 시작하세요.
```bash
$env:FLASK_APP="main.py"
flask run --host=0.0.0.0
```

# 프론트엔드
백엔드 폴더에 있는 경우 `cd ../frontend`를 실행하여 프론트엔드 폴더로 이동하세요.
프론트엔드를 설정하고 실행하기 위해서는 node.js가 필요하므로 [여기](https://nodejs.org/en/)의 지침을 따르세요.
이제 필요한 패키지를 다음과 같이 설치하세요 (시간이 좀 걸릴 수 있습니다):
```bash
npm install
```
추천 항목(여기서는 여행지의 사진)의 이미지를 [여기](https://owncloud.tuwien.ac.at/index.php/s/h70PGy8EkqtQKxs)에서 다운로드하세요. `public` 폴더 아래에 `pics` 폴더를 생성하세요 (`mkdir public/pics`). 다운로드한 `*.zip`의 내용을 새로 생성된 `pics` 디렉토리에 복사하세요. 이제 `public/pics/destination_id/pic_id.jpg` 구조가 되어야 합니다.

프론트엔드를 다음과 같이 컴파일하고 실행하세요.
```bash
npm run serve
```

이제 PicTouRe는 [http://localhost:8080/](http://localhost:8080/)에서 실행됩니다. 🎉