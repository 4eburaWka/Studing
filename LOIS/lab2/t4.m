hFig= figure("Position",[550 400 600 500]);

hAxes = axes('Units', 'points', 'Position', [20 40 250 300], 'FontSize',6);
hT1 = uicontrol('Style','text','Position', [400 430 100 20],'String','Левая граница');
hE1 = uicontrol('Style','edit','Position', [400 410 100 20]);
hT2 = uicontrol('Style','text','Position', [400 390 100 20],'String','Приращение');
hE2 = uicontrol('Style','edit','Position', [400 370 100 20]);
hT3 = uicontrol('Style','text','Position', [400 350 100 20],'String','Правая граница');
hE3 = uicontrol('Style','edit','Position', [400 330 100 20]);
hB = uicontrol('Style','pushbutton','Position', [400 270 100 30],'String','Построить','Callback',@build);


function build(d,c)
    m = menu('Какая функция ?','sin x','cos x','tg x','ctg x','exp x');
    global hAxes hE1 hE2 hE3;

    cla(hAxes)
    x = str2double(get(hE1,'String')) : str2double(get(hE2,'String')) : str2double(get(hE3,'String'));
    switch m
        case 1
            plot(hAxes, x, sin(x))
        case 2
            plot(hAxes, x, cos(x))
        case 3
            plot(hAxes, x, tan(x))
        case 4
            plot(hAxes, x, cotd(x))
        case 5
            plot(hAxes, x , exp(x))
        otherwise
            b = 0 : 0.25 : 10;
            plot(b, cosh(b))
    end

end