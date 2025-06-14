from flask import render_template, request, redirect, url_for
from app import app, engine
from sqlalchemy import text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form['name']
        if user_name:
            with engine.connect() as connection:
                # ユーザー名をデータベースに挿入
                connection.execute(
                    text("INSERT INTO users (name) VALUES (:name)"),
                    {"name": user_name}
                )
                connection.commit()
            return redirect(url_for('index')) # フォーム送信後にリダイレクトして二重送信を防ぐ

    # データベースから全ユーザー名を取得
    users = []
    with engine.connect() as connection:
        result = connection.execute(text("SELECT id, name, created_at FROM users ORDER BY created_at DESC"))
        for row in result:
            users.append({'id': row.id, 'name': row.name, 'created_at': row.created_at})
    
    return render_template('index.html', users=users)

if __name__ == '__main__':
    # これは直接実行されることはない（gunicornが呼び出すため）
    # ただし、ローカルでFlaskを直接起動する場合のために残しておく
    app.run(host='0.0.0.0', port=5000, debug=True)