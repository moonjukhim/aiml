mkdir aiml
cd aiml
python3 -m venv aiml-venv
find aiml-venv/
ls -ltr aiml-venv/bin/
source aiml-venv/bin/activate

pip install jupyterlab

jupyter lab --ip 0.0.0.0

Security Group에서 8888 포트 추가

token을 copy하고 로그인
