echo "Cloning Repo...."
git clone https://github.com/theriturajps/Shortener-Converter-Bot.git /Shortener-Converter-Bot
cd /Shortener-Converter-Bot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
