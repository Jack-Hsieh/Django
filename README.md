# Django Deployment on GCP VM

(參考資料Credit: https://github.com/yalonw/Summarization )

<br>

# 開發版
1. 安裝 python 套件
1. 下載及解壓縮 bert_models 資料
1. 因為 Tensorflow 和 Keras 的關係，執行 Django 時，要加 `--nothreading --noreload`
```
pip install -r requirements.txt

wget -q https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip
unzip -o chinese_L-12_H-768_A-12.zip

python manage.py runserver --nothreading --noreload
```

<br>

# 部署版

1. 更新部署環境 ── Linux (VM)
   - 更新套件資料庫
   - 更改時區
   - 安裝解壓縮工具
   - 安裝 pip3
```
s
