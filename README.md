# DistributedSystem_report8
プロジェクトディレクトリの作成:
まず、PCの任意の場所に「Docker_py_Intermediate」という名前（任意）の新しいフォルダを作成し、その中に上記(提出したpdfファイルを参照)のファイル構成と内容でファイルを保存する。

コマンドプロンプトの起動:
Windowsのコマンドプロンプト（またはPowerShell、Git Bashなど）を開き、作成した「Docker_py_Intermediate」ディレクトリに移動する。
# 例:
C:\Users\YourUser\Documents\分散システム\Docker\Docker_py_Intermediate
Docker Compose の起動:
以下のコマンドを実行して、アプリケーションとデータベースのコンテナをビルドし、起動する。
このコマンドは、必要なPythonパッケージをインストールし、Dockerイメージを構築し、それからWebアプリとデータベースのコンテナをバックグラウンドで起動する。

「docker-compose up --build -d」←上記のディレクトリでのコマンドプロンプト

up: docker-compose.yml に定義されたサービスを起動する。
--build: イメージがまだ存在しない場合や、Dockerfileが変更された場合にイメージを再ビルドする。
-d: コンテナをバックグラウンドで実行する。
注意点:
初回実行時は、PythonやPostgreSQLのベースイメージのダウンロード、Pythonパッケージのインストールに時間がかかることがある。
コマンド実行中に赤いエラーメッセージが表示された場合は、内容をよく読み、メッセージに従って修正を行う。
