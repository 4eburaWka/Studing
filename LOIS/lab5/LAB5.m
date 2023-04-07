%https://studylib.ru/doc/3806821/13-primenenie-paketa-nnt-matlab-dlya-postroeniya-nejronnyh
%Пример
[alphabet, targets] = prprob;
i = 2;
ti = alphabet(:, i);
letter{i} = reshape(ti, 5, 7);
disp(letter{i})
%вызов prprob(формирование массива)
[alphabet,targets]=prprob;
[R,Q] = size(alphabet);
[S2,Q]= size(targets);
%создание двухслойной сети
S1=10;
net=newff(minmax(alphabet),[S1 S2],{'logsig' 'logsig'},'traingdx');
net.LW{2,1}=net.LW{2,1}*0.01;
net.b{2}=net.b{2}*0.01;
view(net);
%обучение в отс. шума
P=alphabet;
T=targets;
net.performFcn='sse';
net.trainParam.goal=0.1;
net.trainParam.show=20;
net.trainParam.epochs=5000;
net.trainParam.mc=0.95;
[net,~] = train(net,P,T);
%Обучение с шумом
netn=net;
netn.trainParam.goal=0.6;
netn.trainParam.epochs=300;
T= [targets targets targets targets];
for pass = 1:10
    P=[alphabet,alphabet,(alphabet+randn(R,Q)*0.1),(alphabet+randn(R,Q)*0.2)];
    [netn,~]=train(netn,P,T);
end
%Повторное обучение в отс. шума
netn.trainParam.goal=0.1;% Предельная среднеквадр погрешность
netn.trainParam.epochs=500;% Максимальное количество циклов обучения
netn.trainParam.show=5;%Частота вывода результатов на экран
[netn,tr] = train(netn,P,T);
%Тестирование(можно как отдельеную функцию)
noise_range = 0:.05:.5;
max_test=100;
network1=[];
network2=[];
T=targets;
%%выполнить тест 
for noiselevel = noise_range
    errors1=0;
    errors2=0;
    for i=1:max_test
        P=alphabet+randn(35,26)*noiselevel;

        %тест сеть 1
        A=sim(net,P);
        AA=compet(A);
        errors1=errors1+sum(sum(abs(AA-T)))/2;
       
        %тест сеть 2
        An=sim(netn,P);
        AAn=compet(An);
        errors2=errors2+sum(sum(abs(AAn-T)))/2;
    end
    network1=[network1 errors1/26/100];
    network2=[network2 errors2/26/100];
end
plot(noise_range,network1*100,'--',noise_range,network2*100);
%тест на распознование символов(шумный J)
noisyJ = alphabet(:,10) + randn(35,1)*0.2;
A2=sim(netn,noisyJ);
answ=find(compet(A2)==1);
disp(answ)
plotchar(alphabet(:,answ));
       