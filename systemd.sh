sudo apt-get -y update
sudo apt-get -y install python3-pip
sudo apt-get -y install virtualenv


cd ./character_sheets

# install the service script
sudo cp flask-app.service /etc/systemd/system/
# reload the service scripts
sudo systemctl daemon-reload
# stop the old service
sudo systemctl stop flask-app
# install the application files
install_dir=/opt/flask-app
sudo rm -rf ${install_dir}
sudo mkdir ${install_dir}
sudo cp -r ./* ${install_dir}
sudo chown -R pythonadm:pythonadm ${install_dir}
# configure python virtual environment and install dependencies
sudo su - pythonadm << EOF
cd ${install_dir}
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
EOF
# start the flask app
sudo systemctl start flask-app
