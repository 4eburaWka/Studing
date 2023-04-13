// lab1_2_1.cpp : Defines the entry point for the application.
//

#include "stdafx.h"

#include <windows.h>         // описани€ Windows 
LRESULT CALLBACK	    WndProc (HWND, UINT, WPARAM, LPARAM);
char   szWindowStyle [ ] = "myWindowStyle";

//===============================
//    √Ћј¬Ќјя ‘”Ќ ÷»я 
int  WINAPI  WinMain   (HINSTANCE hInst,  //дескриптор приложени€
                                       HINSTANCE hPreInst,  //всегда NULL
                                       LPSTR          lpszCmdLine,  //командна€ строка
                                       int                 nCmdShow) //окно при первом выводе
{    	
	HWND                               hWnd;                  //дескриптор окна
	MSG                                  lpMsg;                  //структура хранени€ сообщений 
	WNDCLASS                      wcApp;                 //структура описани€ стил€ окна
	wcApp.lpszClassName   = szWindowStyle;   //им€ стил€ окна
	wcApp.hInstance	       = hInst;                   //дескриптор приложени€ 
	wcApp.lpfnWndProc	       = WndProc;            //указатель на обработчик сооб-щений 
	wcApp.hCursor	       = LoadCursor(NULL, IDC_ARROW);   //курсор - "стрелка"
	wcApp.hIcon		       = 0;                          //без использовани€ пиктограммы
       wcApp.lpszMenuName   = 0;                          //дескриптор меню (без меню)
	wcApp.hbrBackground    = (HBRUSH) GetStockObject (WHITE_BRUSH); //цвет фона 
	wcApp.style		       = CS_HREDRAW | CS_VREDRAW; //перерисовывать окно 
	wcApp.cbClsExtra	       = 0;                          //число доп. байт дл€ WNDCLASS       
	wcApp.cbWndExtra	       = 0;                          //общее число доп. байт 

	if    ( ! RegisterClass (&wcApp) )  //регистраци€ окна   
		return  0;

     hWnd = CreateWindow (szWindowStyle, 
                           "“»ѕќ¬ќ…  ј– ј— Windows-приложени€ Е ",  
		           WS_OVERLAPPEDWINDOW, //окно перекрывающеес€, меню, кнопки
                               CW_USEDEFAULT,        //координата х - левый верхний угол окна 
                               CW_USEDEFAULT,        //координата у - левый верхний угол окна
                               CW_USEDEFAULT,        //ширина окна в единицах устройства
                               CW_USEDEFAULT,        //высота окна в единицах устройства
                               (HWND) NULL,                //указатель на родительское окно
                               (HMENU) NULL,              //зависит от стил€ окна (указатель меню) 
                                hInst,                               //дескриптор приложени€ 
                                NULL );       //адрес дополнительной информации об окне
        ShowWindow (hWnd, nCmdShow);       //вывод окна
        UpdateWindow (hWnd);                         //перерисовка окна
	  while (GetMessage ( &lpMsg, NULL, 0, 0) ) 
	  {
		TranslateMessage (&lpMsg);         //преобразование виртуальных клавиш
		 DispatchMessage (&lpMsg);         //передача сообщени€ обработчику
         }
     	  return ( lpMsg.wParam );
}
short i=0;
char MyString[256];
bool  ReDraw = false;
WORD x,y;

//================================
//    ‘”Ќ ÷»я-ќЅ–јЅќ“„»  √Ћј¬Ќќ√ќ ќ Ќј. (им€ выбирает пользователь)
LRESULT CALLBACK  WndProc (HWND  hWnd,               //дескриптор окна
                                                       UINT    messg,              //код сообщени€
                                                       WPARAM  wParam,  LPARAM    lParam) 
{	
	HDC                   hdc;             //дескриптор контекста устройства 
	PAINTSTRUCT ps;                //структура дл€ клие нтской области окна
	switch (messg)
	{   
		case WM_LBUTTONDOWN:
		case WM_KEYDOWN:

			
				ShowWindow(hWnd,SW_HIDE); 
				Sleep(1000);
				ShowWindow(hWnd,SW_SHOWNORMAL);  
			break;

		case WM_PAINT:
			hdc = BeginPaint( hWnd, &ps );
			TextOut(hdc,100,100,"samara",6);
			TextOut(hdc,100,100,"mansvd",6);
			ValidateRect(hWnd,NULL);
			EndPaint(hWnd, &ps);
			ReDraw=false;
			
		      break;

		case WM_DESTROY:      //послать сообщение о завершении приложени€
		        PostQuitMessage (0);
		        break;
		default: 
		        return ( DefWindowProc (hWnd, messg, wParam, lParam)); 
             }
             return 0;
}
