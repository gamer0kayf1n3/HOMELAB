
REM go to your project directory
cd /d C:\Users\rfont\HOMELAB

REM pull latest changes
git config --global --add safe.directory C:/Users/rfont/HOMELAB
git pull origin production

REM optional: update dependencies
REM python -m pip install -r requirements.txt

python homeserver.py