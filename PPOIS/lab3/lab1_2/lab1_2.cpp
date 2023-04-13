// lab1_2.cpp : Defines the entry point for the application.
//

#include "stdafx.h"


#include <windows.h>         // �������� Windows 
LRESULT CALLBACK	    WndProc (HWND, UINT, WPARAM, LPARAM);
char   szWindowStyle [ ] = "myWindowStyle";

//===============================
//    ������� ������� 
int  WINAPI  WinMain   (HINSTANCE hInst,  //���������� ����������
                                       HINSTANCE hPreInst,  //������ NULL
                                       LPSTR          lpszCmdLine,  //��������� ������
                                       int                 nCmdShow) //���� ��� ������ ������
{    	
	HWND                               hWnd;                  //���������� ����
	MSG                                  lpMsg;                  //��������� �������� ��������� 
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

	if    ( ! RegisterClass (&wcApp) )  //����������� ����   
		return  0;

     hWnd = CreateWindow (szWindowStyle, 
                           "������� ������ Windows-���������� � ",  
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
	 ShowWindow (hWnd,SW_SHOWMAXIMIZED);       //����� ����
        UpdateWindow (hWnd);                         //����������� ����
	 MessageBox(hWnd,"UpdateWindow","UpdateWindow",MB_OK);
	  while (GetMessage ( &lpMsg, NULL, 0, 0) ) 
	  {
		TranslateMessage (&lpMsg);         //�������������� ����������� ������
		 DispatchMessage (&lpMsg);         //�������� ��������� �����������
         }
     	  return ( lpMsg.wParam );
}

//================================
//    �������-���������� �������� ����. (��� �������� ������������)
LRESULT CALLBACK  WndProc (HWND  hWnd,               //���������� ����
                                                       UINT    messg,              //��� ���������
                                                       WPARAM  wParam,  LPARAM    lParam) 
{	
	HDC                   hdc;             //���������� ��������� ���������� 
	PAINTSTRUCT ps;                //��������� ��� ���������� ������� ����
	switch (messg) 
	{                                         
	          case WM_PAINT:                     //������������ ����
				hdc = BeginPaint (hWnd, &ps);            
                        //-----������ ��������� ������������
		      //-----����� ��������� ������������	
		      ValidateRect (hWnd,NULL); 
		      EndPaint (hWnd, &ps); 
		      break;
		case WM_DESTROY:      //������� ��������� � ���������� ����������
				MessageBox(hWnd,"WM_DESTROY","WM_DESTROY",MB_OK);
		        PostQuitMessage (0);
		        break;
		default: 
		        return ( DefWindowProc (hWnd, messg, wParam, lParam)); 
             }
             return 0;
}

