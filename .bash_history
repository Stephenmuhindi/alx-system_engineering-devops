git config --global user.name "Stephenmuhindi"
git config --global user.email bteneson42@gmail.com
cd ~
mkdir zero_day
cd zero_day
git init
git remote add zero_day https://github.com/Stephenmuhindi/zero_day.git
echo "Strong" > README.md
git add .
git commit -m "My first commit"
git push
git push --set-upstream zero_day master
clear
mkdir 0x00-vagrant
cd 0x00-vagrant
echo "maasai" > README.md
ls
echo "Linux" > 0-hello_ubuntu
git add .
git commit -m "vagrant"
git push
