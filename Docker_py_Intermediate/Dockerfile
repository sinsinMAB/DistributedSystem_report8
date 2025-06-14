# --- ビルドステージ ---
FROM python:3.9-slim-buster AS builder

WORKDIR /app

# 依存関係ファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# --- 最終ステージ ---
FROM python:3.9-slim-buster

WORKDIR /app

# 必要であれば、ここで pip install --no-cache-dir gunicorn をもう一度実行する手もありますが、
# これだとイメージサイズが少し大きくなる可能性があります。
# または、site-packages を確実にコピーし、gunicorn の実行パスを明示的に指定する。
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# アプリケーションコードをコピー
COPY app/ app/

# ポートを公開
EXPOSE 5000

# gunicornの実行パスを明示的に指定
# 'python -m gunicorn' でモジュールとして実行する
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "app:app"]