hFig= figure("Position",[550 400 600 500]);

hAxes = axes('Units', 'points', 'Position', [20 40 250 300], 'FontSize',6);
hT1 = uicontrol('Style','text','Position', [400 430 100 20],'String','Левая граница');
hE1 = uicontrol('Style','edit','Position', [400 410 100 20]);
hT2 = uicontrol('Style','text','Position', [400 390 100 20],'String','Приращение');
hE2 = uicontrol('Style','edit','Position', [400 370 100 20]);
hT3 = uicontrol('Style','text','Position', [400 350 100 20],'String','Правая граница');
hE3 = uicontrol('Style','edit','Position', [400 330 100 20]);
hB = uicontrol('Style','pushbutton','Position', [400 270 100 30],'String','Построить','Callback',@build);


function build(src,event)
    m = menu('Какая функция ?','sin x','cos x','tg x','ctg x','exp x');
    global hAxes hE1 hE2 hE3 hT1 hT2 hT3 hB hB2;

    hB2 = uicontrol("Style","pushbutton","String",'Новая функция','Position',[200 0 100 30],'Callback',@rebuild);
    set(hAxes,'Position', [40 40 350 300]);
    set(hB2,'Visible','on');
    set(hB,'Visible','off');
    set(hE1,'Visible','off');
    set(hT1,'Visible','off');
    set(hE2,'Visible','off');
    set(hT2,'Visible','off');
    set(hE3,'Visible','off');
    set(hT3,'Visible','off');
    cla(hAxes);

    x = str2double(get(hE1,'String')):str2double(get(hE2,'String')):str2double(get(hE3,'String'));
    switch m
        case 1
            plot(hAxes, x, sin(x));
        case 2
            plot(hAxes, x, cos(x));
        case 3
            plot(hAxes, x, tan(x));
        case 4
            plot(hAxes, x, cotd(x));
        case 5
            plot(hAxes, x, exp(x));
        otherwise
            b = 0 : 0.25 : 10;
            plot(b, cosh(b))
    end
end

function rebuild(src, event)
    global hAxes hE1 hE2 hE3 hT1 hT2 hT3 hB hB2;
    cla(hAxes);

    set(hAxes,'Position', [20 40 250 300]);
    set(hB2,'Visible','off');
    set(hE1,'Visible','on');
    set(hT1,'Visible','on');
    set(hE2,'Visible','on');
    set(hT2,'Visible','on');
    set(hE3,'Visible','on');
    set(hT3,'Visible','on');
    set(hB,'Visible','on');
end
