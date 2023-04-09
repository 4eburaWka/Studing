mkdir Litvinyuk
mkdir Litvinyuk/1 Litvinyuk/4
mkdir Litvinyuk/1/2 Litvinyuk/1/3
cp /etc/group /media/timofei/Files/Studing/OS/lab1/Litvinyuk/1
cp /etc/group Litvinyuk/1/2
cp /etc/group Litvinyuk/1/3
cp /etc/group /media/timofei/Files/Studing/OS/lab1/Litvinyuk/4 #~ не работает из-за того, что не на том диске
cd Litvinyuk/1/3
rm ../../4/group
cd ../../..
rm -r Litvinyuk/1 Litvinyuk/4
head -13 /etc/group
tail -13 /etc/group 
