status_matrix = readmatrix("status_matrix");

WE_time = 30;
NS_time = 30;

WE_num = 0;
NS_num = 0;

cars_for_1_sec = 2; % кол-во машин, проезжающих за одну секунду зеленого светофора

disp("WE_num  NS_num  WE_time  NS_time");
for i = 1:10
    WE_num = WE_num + randi(90); % кол-во машин на СЮ
    NS_num = NS_num + randi(90); % кол-во машин на ЗВ
    
    WE_num = max(WE_num - cars_for_1_sec * WE_time, 0);
    NS_num = max(NS_num - cars_for_1_sec * NS_time, 0);

    WE_trf_stasus = round(membershipFunc_for_trfLgtTime(WE_time));
    WE_car_num = round(membershipFunc_for_carNums(WE_num));
    NS_car_num = round(membershipFunc_for_carNums(NS_num));
        
    change_time = conclusion(WE_trf_stasus, WE_car_num, NS_car_num);

    WE_time = min(max(WE_time + change_time, 10), 50); % чтобы 10 < time < 50
    NS_time = 60 - WE_time;
    
    disp([WE_num, NS_num, WE_time, NS_time]);
    
    % время светофора не моет быть меньше 10 сек
end


function N = membershipFunc_for_carNums(x)
    very_few = max(min( 1, (18 - x) / (18 - 12) ), 0);
    few = max(min([ (x - 16) / (21 - 16), 1, (36 - x) / (36 - 31) ]), 0);
    average = max(min([ (x - 34) / (40 - 34), 1, (56 - x) / (56 - 50) ]), 0);
    big = max(min([ (x - 54) / (59 - 54), 1, (76- x) / (76- 69) ]), 0);
    very_big = max(min( (x - 72) / (77- 72), 1 ), 0);

    N = 1 * very_few + 2 * few + 3 * average + 4 * big + 5 * very_big;
end

function N = membershipFunc_for_trfLgtTime(x)
    few = max(min( 1, (25 - x) / (25 - 20) ), 0);
    average = max(min([ (x - 20) / (25 - 20), 1, (40 - x) / (40 - 35) ]), 0);
    big = max(min( (x - 35) / (40 - 35), 1 ), 0);

    N = 1 * few + 2 * average + 3 * big;
end

function time = conclusion(a, b, c)
    status_matrix = readmatrix("status_matrix");
    status = 0;

    arr = [a, b, c];
    for i=1:length(status_matrix)
        if status_matrix(i,1:3) == arr
            status = status_matrix(i,4);
            break
        end
    end
    switch status
        case 1
            time = randi(20);
        case 2
            time = randi(30) - 15;
        case 3
            time = randi(20) - 20;
        case 0
            time = 0;
    end
end

    