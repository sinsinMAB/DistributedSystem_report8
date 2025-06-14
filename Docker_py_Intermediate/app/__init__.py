from flask import Flask
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import os
import time

app = Flask(__name__)

# 環境変数からデータベース接続情報を取得
DB_USER = os.environ.get('POSTGRES_USER', 'user')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'password')
DB_NAME = os.environ.get('POSTGRES_DB', 'mydatabase')
DB_HOST = os.environ.get('DB_HOST', 'db') # Docker Compose のサービス名 'db' をホスト名とする
DB_PORT = os.environ.get('DB_PORT', '5432')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = None # 後で初期化

def init_db():
    global engine
    retries = 5
    while retries > 0:
        try:
            print(f"Attempting to connect to database at {DATABASE_URL}...")
            engine = create_engine(DATABASE_URL)
            # データベース接続をテストするために簡単なクエリを実行
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
            print("Database connected successfully!")
            break
        except OperationalError as e:
            print(f"Database connection failed: {e}")
            retries -= 1
            if retries > 0:
                print(f"Retrying in 5 seconds... ({retries} retries left)")
                time.sleep(5)
            else:
                print("Failed to connect to database after multiple retries.")
                raise # 接続できない場合は例外を発生させる

    if engine:
        # テーブルが存在しない場合に作成する (usersテーブル)
        with engine.connect() as connection:
            connection.execute(text("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """))
            connection.commit() # トランザクションをコミット
        print("Users table ensured.")

# アプリケーションの起動時にデータベース接続を初期化
# これはFlaskのBlueprintや拡張機能を使うともっと洗練できますが、シンプルな例として直接呼び出します
with app.app_context():
    init_db()

# main.py のルートをインポート（循環参照を避けるため、通常は初期化後にインポート）
from app import main