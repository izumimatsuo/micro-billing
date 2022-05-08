# micro-billing [![Build Status](https://app.travis-ci.com/izumimatsuo/micro-billing.svg?branch=main)](https://app.travis-ci.com/izumimatsuo/micro-billing)

環境構築

```
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install --upgrade pip
(.venv) $ pip install -r requirements.txt
```

実行

```
(.venv) $ uvicorn main:app --reload
```

テスト
```
(.venv) $ pytest
(.venv) $ coverage run -m pytest
(.venv) $ coverage report
```

技術アーキテクチャ

- 仮想環境 venv
- フレームワーク FastAPI, Uvicorn, SQLAlchemy
- 静的チェック flake8
- PEP8準拠コードフォーマッタ black
- type hintをチェック mypy
- 自動テスト pytest
- テストカバレッジ計測 coverage

