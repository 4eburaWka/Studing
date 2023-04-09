cd Folder

echo -e "№1"
echo "Пример" > bigfile
echo "Пример" >> bigfile1
echo "Пример" > bigfile
echo "Пример" >> bigfile1

read
echo -e "№2"
cat - > 1

read
echo -e "№3"
sh myscript 
sh myscript > file1
sh myscript 2> file3 && sh myscript 2> file2
sh myscript > file1 && sh myscript 2> file2
sh myscript &> file3
sh myscript > file4 2>> file4

read
echo -e "№4"
cat /etc/group | sort -r > file1
tail -15 file1 | sed -n '3p'
tail -15 file1 | sed -n '6p'

read 
echo -e "№5"
ls -l /dev | grep '^b' | wc -l
ls -l /dev | grep '^c' | wc -l


