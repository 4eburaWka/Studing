// lab3_5.cpp : Defines the entry point for the application.
//

#include "stdafx.h"
#include "resource.h"

Message messg;
LRESULT CALLBACK WndProc (HWND hWnd, UINT Message, WPARAM wParam,  LPARAM lParam);
int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
 	HWND                               hWnd;   
	MSG                                  lpMsg;   
	WNDCLASS                       wcApp;  
	wcApp.lpszClassName   = szWindowStyle;  
	wcApp.hInstance	       = hInst;  
	wcApp.lpfnWndProc	       = calback; 
	wcApp.hCursor	       = LoadCursor (NULL, IDC_ARROW);  
	wcApp.hIcon		       = 0;  
	wcApp.lpszMenuName   = 0;  
	wcApp.hbrBackground    = (HBRUSH) GetStockObject (WHITE_BRUSH);
	wcApp.style		       = CS_HREDRAW | CS_VREDRAW;	
       wcApp.cbClsExtra	       = 0;
	wcApp.cbWndExtra	       = 0;       
	if    ( ! RegisterClass (&wcApp))  return  0;
       hWnd = CreateWindow  (szWindowStyle, "Kabak_litvinyuk",
                                               WS_OVERLAPPEDWINDOW, CW_USEDEFAULT,
                                               CW_USEDEFAULT, CW_USEDEFAULT, 
                                               CW_USEDEFAULT, (HWND) NULL,               
                                               ( HMENU )NULL,  hInst,  NULL);                                                                                                                                                                                     
       ShowWindow (hWnd, nCmdShow);
       UpdateWindow (hWnd); 
       while ( GetMessage (&lpMsg, NULL, 0, 0) ) 
	{
		TranslateMessage (&lpMsg);
		DispatchMessage  (&lpMsg);    
       }
     	return (lpMsg.wParam);
}


LRESULT CALLBACK WndProc (HWND hWnd, UINT Message, 
					  WPARAM wParam,  LPARAM lParam)
{	
	switch (Message) 
	{
	case WM_COMMAND:  // сообщение от меню
		switch (wParam)  // параметр сообщения - ID выбранного пункта меню
		{
		case ID_OUTPUT_LINE1:
			break;
		case ID_OUTPUT_LINE2:
			break;  
                        default:
			return DefWindowProc(hWnd, messg, wParam, lParam);
		}
		break;
		default:
			return (DefWindowProc(hWnd, messg, wParam, lParam));
	}
	return 0;
}
