// lab2_8.cpp : Defines the entry point for the application.
//

#include "stdafx.h"
#include "resource.h";
#include <stdio.h>
//=========== ???????? ?????????? ???????? =============
LRESULT CALLBACK calback (HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK   callback2 (HWND, UINT, WPARAM, LPARAM);
char   szWindowStyle [ ] = "win";
HINSTANCE hInstance;
//================??????? ???????===================
int  WINAPI  WinMain (HINSTANCE hInst,  HINSTANCE hPreInst,  
                                      LPSTR  lpszCmdLine,    int   nCmdShow) 
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
int x=0, y=0;bool Redraw=false;
//=== ???????-?????????? ????????? ???????? ????  ===
LRESULT CALLBACK calback(HWND hWnd, UINT  Mess,  WPARAM  wParam, LPARAM lParam)
{	
	HDC  hdc;  
	PAINTSTRUCT ps;   
	switch (Mess) 
	{                                         
	          case WM_PAINT:  
						hdc = BeginPaint (hWnd, &ps);
						DialogBox (hInstance, (LPCTSTR) IDD_DIALOG1, hWnd, (DLGPROC) callback2);
		        ValidateRect (hWnd,NULL);
		       EndPaint (hWnd, &ps);
		       break;
                 //case  < ???????????? > :
		        //hdc = BeginPaint (hWnd, &ps);            
                          //< ???????? ???????????? >
		        //ValidateRect (hWnd,NULL);
		        //EndPaint (hWnd, &ps);
		        //break;
		case WM_DESTROY:  
		         PostQuitMessage (0);
		         break;

		default: 
		         return DefWindowProc (hWnd, Mess, wParam, lParam); 
       }
       return  0;
}

LRESULT CALLBACK callback2 ( HWND    hDlg, UINT   Message, 
                                                                       WPARAM wParam,  LPARAM lParam)
{
	switch (Message)
	{
	 case WM_INITDIALOG:
		return FALSE;
	  case WM_COMMAND:
		switch (wParam)
	           {
		case IDOK:
				if (MessageBox(NULL, "ok?", "ok?", 1) == IDOK)
					 EndDialog(hDlg,TRUE);
	                     break;
		case IDCANCEL:
			PostQuitMessage (0);
		if (MessageBox(NULL, "cancel?", "cancel?", 1) == IDOK)
		         EndDialog(hDlg,FALSE);
		          break;
		case IDC_BUTTON1:
					if (MessageBox(NULL, "cancel?", "cancel?", 1) == IDOK)
		         EndDialog(hDlg,FALSE);
					break;
		 default:
		          return FALSE;
	            }
		break;
	   default:
		return FALSE;
	  }
         return TRUE;
};



