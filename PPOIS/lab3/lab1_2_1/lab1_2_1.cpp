// lab1_2_1.cpp : Defines the entry point for the application.
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
	WNDCLASS                      wcApp;                 //��������� �������� ����� ����
	wcApp.lpszClassName   = szWindowStyle;   //��� ����� ����
	wcApp.hInstance	       = hInst;                   //���������� ���������� 
	wcApp.lpfnWndProc	       = WndProc;            //��������� �� ���������� ����-����� 
	wcApp.hCursor	       = LoadCursor(NULL, IDC_ARROW);   //������ - "�������"
	wcApp.hIcon		       = 0;                          //��� ������������� �����������
       wcApp.lpszMenuName   = 0;                          //���������� ���� (��� ����)
	wcApp.hbrBackground    = (HBRUSH) GetStockObject (WHITE_BRUSH); //���� ���� 
	wcApp.style		       = CS_HREDRAW | CS_VREDRAW; //�������������� ���� 
	wcApp.cbClsExtra	       = 0;                          //����� ���. ���� ��� WNDCLASS       
	wcApp.cbWndExtra	       = 0;                          //����� ����� ���. ���� 

	if    ( ! RegisterClass (&wcApp) )  //����������� ����   
		return  0;

     hWnd = CreateWindow (szWindowStyle, 
                           "������� ������ Windows-���������� � ",  
		           WS_OVERLAPPEDWINDOW, //���� ���������������, ����, ������
                               CW_USEDEFAULT,        //���������� � - ����� ������� ���� ���� 
                               CW_USEDEFAULT,        //���������� � - ����� ������� ���� ����
                               CW_USEDEFAULT,        //������ ���� � �������� ����������
                               CW_USEDEFAULT,        //������ ���� � �������� ����������
                               (HWND) NULL,                //��������� �� ������������ ����
                               (HMENU) NULL,              //������� �� ����� ���� (��������� ����) 
                                hInst,                               //���������� ���������� 
                                NULL );       //����� �������������� ���������� �� ����
        ShowWindow (hWnd, nCmdShow);       //����� ����
        UpdateWindow (hWnd);                         //����������� ����
	  while (GetMessage ( &lpMsg, NULL, 0, 0) ) 
	  {
		TranslateMessage (&lpMsg);         //�������������� ����������� ������
		 DispatchMessage (&lpMsg);         //�������� ��������� �����������
         }
     	  return ( lpMsg.wParam );
}
short i=0;
char MyString[256];
bool  ReDraw = false;
WORD x,y;

//================================
//    �������-���������� �������� ����. (��� �������� ������������)
LRESULT CALLBACK  WndProc (HWND  hWnd,               //���������� ����
                                                       UINT    messg,              //��� ���������
                                                       WPARAM  wParam,  LPARAM    lParam) 
{	
	HDC                   hdc;             //���������� ��������� ���������� 
	PAINTSTRUCT ps;                //��������� ��� ���� ������ ������� ����
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

		case WM_DESTROY:      //������� ��������� � ���������� ����������
		        PostQuitMessage (0);
		        break;
		default: 
		        return ( DefWindowProc (hWnd, messg, wParam, lParam)); 
             }
             return 0;
}
