#include "stdafx.h"
#include "resource.h"
LRESULT CALLBACK	About(HWND, UINT, WPARAM, LPARAM);
int APIENTRY WinMain(HINSTANCE hInstance,
                     HINSTANCE hPrevInstance,
                     LPSTR     lpCmdLine,
                     int       nCmdShow)
{
DialogBox(hInstance, (LPCTSTR)IDD_LIST, NULL, (DLGPROC)About);
	return 0;
}
char buffer[256];
LRESULT CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
	int  wmId    = LOWORD(wParam); 
    int  wmEvent = HIWORD(wParam); 
    int  RecordsAmount = SendDlgItemMessage(hDlg, IDC_LIST, LB_GETCOUNT, 0, 0);
	int currentNumber = SendDlgItemMessage(hDlg, IDC_LIST, LB_GETCURSEL, 0, 0);
	switch (message)
	{
		case WM_INITDIALOG:
				SendDlgItemMessage(hDlg,IDC_LIST,LB_ADDSTRING,0,(LPARAM)"First");
				SendDlgItemMessage(hDlg,IDC_LIST,LB_ADDSTRING,0,(LPARAM)"Second");
				SendDlgItemMessage(hDlg,IDC_LIST,LB_ADDSTRING,0,(LPARAM)"Third");
				SendDlgItemMessage(hDlg,IDC_LIST,LB_ADDSTRING,0,(LPARAM)"Fourth");
				SendDlgItemMessage(hDlg,IDC_LIST,LB_ADDSTRING,0,(LPARAM)"Fifth");
				return TRUE;

		case WM_COMMAND:
			switch (wmId)
			{
			case IDOK:
			case IDCANCEL:
				EndDialog(hDlg, LOWORD(wParam));
				PostQuitMessage(0);
				return TRUE;
				break;
			case IDC_ADD:
				GetDlgItemText(hDlg,IDC_EDIT,buffer,256);
				if(strlen(buffer) != 0){
				SendDlgItemMessage(hDlg,IDC_LIST,LB_ADDSTRING,0,(LPARAM)buffer);
				}
				break;
			case IDC_DELETE:
				SendDlgItemMessage(hDlg,IDC_LIST,LB_DELETESTRING,currentNumber,0);
				break;
			case IDC_CHANGE:
				SendDlgItemMessage(hDlg,IDC_LIST,LB_GETTEXT,currentNumber,(LPARAM)buffer);
				SendDlgItemMessage(hDlg,IDC_LIST,LB_DELETESTRING,currentNumber,0);
				SetDlgItemText(hDlg,IDC_EDIT,buffer);
				break;
			}
			break;
	}
    return FALSE;
}
