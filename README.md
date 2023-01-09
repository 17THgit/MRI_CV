# MRI_CV
DICOM 파일을 파이썬을 통해 읽어, otsu.py를 이용해 OTSU 알고리즘을 이용해 contour를 그린 후, 그 contour를 감싸는 minimum enclosing circle을 그려 각 원의 중심에 대한 좌표 확보.
pydicomFINAL.py를 이용해 각 원의 중심에 대한 좌표를 기반으로 크기가 같은 원을 그린 후 mask를 통해 각 원들의 image intensity 값들의 평균, 최고값, 최소값 등의 정보를 얻어냄.
다른 파일들에서도 원의 좌표가 같기 때문에 원의 좌표는 고정할 수 있음.
