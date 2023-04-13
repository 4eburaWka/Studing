// lab1_2.cpp : Defines the entry point for the application.
//

#include "stdafx.h"


#include <windows.h>         // описания Windows 
LRESULT CALLBACK	    WndProc (HWND, UINT, WPARAM, LPARAM);
char   szWindowStyle [ ] = "myWindowStyle";

//===============================
//    ГЛАВНАЯ ФУНКЦИЯ 
int  WINAPI  WinMain   (HINSTANCE hInst,  //дескриптор приложения
                                       HINSTANCE hPreInst,  //всегда NULL
                                       LPSTR          lpszCmdLine,  //командная строка
                                       int                 nCmdShow) //окно при первом выводе
{    	
	HWND                               hWnd;                  //дескриптор окна
	MSG                                  lpMsg;                  //структура хранения сообщений 
	WNDCLASS                      wcApp;
	wcApp.lpszClassName   = szWindowStyle;
	wcApp.hInstance	       = hInst; 
	wcApp.lpfnWndProc	       = WndProc;
	wcApp.hCursor	       = LoadCursor(NULL, IDC_CROSS);
	wcApp.hIcon		       = 0; 
       wcApp.lpszMenuName   = 0;  
	wcApp.hbrBackground    = (HBRUSH) GetStockObject (DKGRAY_BRUSH);
	wcApp.style		       = CS_BYTEALIGNCLIENT|CS_CLASSDC;
	wcApp.cbClsExtra	       = 0;                               
	wcApp.cbWndExtra	       = 0;                          

	if    ( ! RegisterClass (&wcApp) )  //регистрация окна   
		return  0;

     hWnd = CreateWindow (szWindowStyle, 
                           "ТИПОВОЙ КАРКАС Windows-приложения … ",  
		           WS_BORDER | WS_CAPTION | WS_SYSMENU | WS_VSCROLL|WS_MAXIMIZEBOX|WS_MINIMIZEBOX,
                               100,
                               200,
							   300,
                               300,
                               (HWND) NULL,
                               (HMENU) NULL,
                                hInst,
								NULL);
     MessageBox(hWnd,"CreateWindow","CreateWindow",MB_OK);
	 ShowWindow (hWnd,SW_SHOWMAXIMIZED);       //вывод окна
        UpdateWindow (hWnd);                         //перерисовка окна
	 MessageBox(hWnd,"UpdateWindow","UpdateWindow",MB_OK);
	  while (GetMessage ( &lpMsg, NULL, 0, 0) ) 
	  {
		TranslateMessage (&lpMsg);         //преобразование виртуальных клавиш
		 DispatchMessage (&lpMsg);         //передача сообщения обработчику
         }
     	  return ( lpMsg.wParam );
}

//================================
//    ФУНКЦИЯ-ОБРАБОТЧИК ГЛАВНОГО ОКНА. (имя выбирает пользователь)
LRESULT CALLBACK  WndProc (HWND  hWnd,               //дескриптор окна
                                                       UINT    messg,              //код сообщения
                                                       WPARAM  wParam,  LPARAM    lParam) 
{	
	HDC                   hdc;             //дескриптор контекста устройства 
	PAINTSTRUCT ps;                //структура для клиентской области окна
	switch (messg) 
	{                                         
	          case WM_PAINT:                     //перерисовать окно
				hdc = BeginPaint (hWnd, &ps);            
                        //-----Начало фрагмента пользователя
		      //-----Конец фрагмента пользователя	
		      ValidateRect (hWnd,NULL); 
		      EndPaint (hWnd, &ps); 
		      break;
		case WM_DESTROY:      //послать сообщение о завершении приложения
				MessageBox(hWnd,"WM_DESTROY","WM_DESTROY",MB_OK);
		        PostQuitMessage (0);
		        break;
		default: 
		        return ( DefWindowProc (hWnd, messg, wParam, lParam)); 
             }
             return 0;
}

