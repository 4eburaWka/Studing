// lab2_9.cpp : Defines the entry point for the application.
//

#include "stdafx.h"
#include "resource.h"

LRESULT CALLBACK   callback (HWND hDlg, UINT Message, WPARAM wParam,  LPARAM lParam);

HINSTANCE hInst;
int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
 	
	DialogBox(hInst, (LPCTSTR) IDD_DIALOG1, NULL, (DLGPROC) callback ) ;

	return 0;
}

LRESULT CALLBACK   callback (HWND hDlg, UINT Message, 
                                                           WPARAM wParam,  LPARAM lParam)
{	
        switch (Message)
	{
	 case WM_INITDIALOG:
		return FALSE; 
	  case WM_COMMAND:
		switch (wParam)
	           {
		case IDC_BUTTON1:
			char str[256];
			GetDlgItemText(hDlg,IDC_EDIT1, str, 15);
			SetDlgItemText(hDlg,IDC_EDIT2, str);
			break;
		case IDCANCEL:
			EndDialog(hDlg,TRUE);
			PostQuitMessage(0);
			break;
		 default:
		          return FALSE;
	            }
				break;
	   default:
		return FALSE;
	  }
         return TRUE;

}




