// TKP_Shablon.cpp : Defines the entry point for the application.
//

#include "stdafx.h"
#include "resource.h"

#define MAX_LOADSTRING 100

// Global Variables:
HINSTANCE hInst;								// current instance
TCHAR szTitle[MAX_LOADSTRING];								// The title bar text
TCHAR szWindowClass[MAX_LOADSTRING];								// The title bar text
LRESULT CALLBACK	WndProc(HWND, UINT, WPARAM, LPARAM);


int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
	DialogBox(hInstance,(LPCTSTR)IDD_MAIN,NULL,(DLGPROC)WndProc);
	
	return 0;
}

LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{

	switch (message)
	{
	 case WM_INITDIALOG:
		return FALSE;
	  break;
     case WM_RBUTTONDOWN:
      break;
	  case WM_COMMAND:
		switch (wParam)
	           {
		case IDOK:
	          break;
		case IDCANCEL:
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
