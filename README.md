# pycon-apac-2023-django-orm-dojo
https://2023-apac.pycon.jp/timetable?id=GJJGPS

## 概要

PyCon APAC 2023 でのトーク「Django ORM道場 -- クエリの基本を押さえ、より良い形を身に付けよう」のサンプルコードです。

トーク資料: <URL TBD>

## 動作確認したバージョン

* Python 3.10.8
* Django 4.2.6

## ファイルの説明

* `requirements.txt`: venv用にライブラリをまとめたファイル(環境構築で使用)
* `src/`: Djangoプロジェクトのルートディレクトリ
* `src/config/settings.py`: Djangoプロジェクト設定のLOGGING定義
* `src/app/models.py`: Staff等のモデル定義
* `src/app/views.py`: Staff一覧画面用view関数定義
* `src/app/templatetags/status.py`: staff_status フィルタ関数定義
* `src/app/templates/index.html`: Staff一覧画面用HTML

## Djangoプログラム実行方法

```bash
(venv) $ python src/manage.py migrate
(venv) $ python src/manage.py runserver
-- 中略 --
Django version 4.2.6, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

ブラウザで http://127.0.0.1:8000/staff/ にアクセスしてください。
