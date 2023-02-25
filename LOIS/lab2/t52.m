hFig= figure("Position",[550 400 600 500]);
global hAxes hE1 hE2 hE3 hE4 hE5
hT1=uicontrol('Style','text','Position', [20 430 150 20],'String','Левая граница отрезка х');
hE1=uicontrol('Style','edit','Position', [50 410 100 20]);
hT2=uicontrol('Style','text','Position', [20 390 150 20],'String','Правая граница отрезка х');
hE2=uicontrol('Style','edit','Position', [50 370 100 20]);
hT3=uicontrol('Style','text','Position', [50 350 100 20],'String','Значение y1(0)');
hE3=uicontrol('Style','edit','Position', [50 330 100 20]);
hT4=uicontrol('Style','text','Position', [50 310 100 20],'String','Значение y2(0)');
hE4=uicontrol('Style','edit','Position', [50 290 100 20]);
hT5=uicontrol('Style','text','Position', [50 270 100 20],'String','Значение K');
hE5=uicontrol('Style','edit','Position', [50 250 100 20]);
hB=uicontrol('Style','pushbutton','String','Вычислить','Position',[50 230 100 20],'Callback',@DiffBegin);
hAxes = axes('Units', 'points', 'Position', [170 40 250 300], 'FontSize',6);


function DiffBegin(src,entry)
    global hAxes hE1 hE2 hE3 hE4 hE5;
    x1 = str2double(get(hE1,'String'));
    x2 = str2double(get(hE2,'String'));
    y1 = str2double(get(hE3,'String'));
    y2 = str2double(get(hE4,'String'));
    k = str2double(get(hE5,'String'));
    cla(hAxes);

    [x,y]=ode15s(@(x,y)[y2;-y1+k*(1-y1^2)*y2],[x1 x2],[y1,y2]);
    disp(y(:,1))
    disp(x)
    plot(hAxes,x,y(:,1))
    hold on
    plot(hAxes,x,y(:,2))
    hold off
end

function dydt=diffunc(x,y)
    global k;
    dydt=[k*x^2+y(2);-y(1)];
end

function dydt = diffunc2(x,y)
    dydt=[0.01*x^2+y(2);-y(1)];
end

function dydt = diffunc23(x,y)
    dydt=[y(2);-y(1)+1000*(1-y(1)^2)*y(2)];
end


