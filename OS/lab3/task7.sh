#!/bin/bash
menu="1. Вывод полной информации о файлах каталога.\n2. Изменить атрибуты файла.\n3. Выход."
echo -e $menu
while read name && [ $name != 3 ]
do
	if [ $name == 1 ]
        then echo -e "Введите имя каталога: "
        read path
        ls -l $path
    else 
    	if [ $name == 2 ]
		    then echo "Введите путь к файлу: "
		    read path 
		    echo "Введите имя файла: "
		    read file
		    echo "Введите желаемые атрибуты файла: "
		    read attr
			chmod $attr $path/$file
			ls -l $path
		fi
    fi
    echo -e $menu
done
