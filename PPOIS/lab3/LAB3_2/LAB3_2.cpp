// LAB3_2.cpp : Defines the entry point for the application.
//

#include "stdafx.h"
#include "resource.h"
#include "stdio.h"
//=========== ÓÔËÒ‡ÌËˇ „ÎÓ·‡Î¸Ì˚ı Ó·˙ÂÍÚÓ‚ =============
LRESULT CALLBACK  lcwnd (HWND, UINT, WPARAM, LPARAM);
LRESULT CALLBACK  lcwnd2(HWND hWnd, UINT  Mess, WPARAM  wParam, LPARAM lParam);
char   szWindowStyle [ ] = "lab32";
char   szWindowStyle2 [ ] = "lab324";
HWND hwndgl;
int Cmdshow;
HINSTANCE hInstg;
//================√À¿¬Õ¿ﬂ ‘”Õ ÷»ﬂ===================
int  WINAPI  WinMain (HINSTANCE hInst,  HINSTANCE hPreInst,  
                                      LPSTR  lpszCmdLine,    int   nCmdShow) 
{         
	Cmdshow=nCmdShow;
	hInstg=hInst;
	HWND                               hWnd;   
	MSG                                  lpMsg;   
	WNDCLASS                       wcApp2;  
	wcApp2.lpszClassName   = szWindowStyle2;  
	wcApp2.hInstance	       = hInst;  
	wcApp2.lpfnWndProc	       = lcwnd2; 
	wcApp2.hCursor	       = LoadCursor (NULL, IDC_ARROW);  
	wcApp2.hIcon		       = 0;  
	wcApp2.lpszMenuName   = 0;  
	wcApp2.hbrBackground    = (HBRUSH) GetStockObject (WHITE_BRUSH);
	wcApp2.style		       = CS_HREDRAW | CS_VREDRAW;	
      wcApp2.cbClsExtra	       = 0;
	wcApp2.cbWndExtra	       = 0;       
	if    ( ! RegisterClass (&wcApp2))  return  0;
    DialogBox(hInst, (LPCTSTR)IDD_DIALOG1, 0, (DLGPROC)lcwnd);
	//CreateWindow  (szWindowStyle, " ¿– ¿— œ–»ÀŒ∆≈Õ»ﬂ",
                //                               WS_OVERLAPPEDWINDOW, CW_USEDEFAULT,
                  //                             CW_USEDEFAULT, CW_USEDEFAULT, 
                    //                           CW_USEDEFAULT, (HWND) NULL,               
                      //                         ( HMENU )NULL,  hInst,  NULL);                                                                                                                                                                                     
       //ShowWindow (hWnd, nCmdShow);
       //UpdateWindow (hWnd); 
       while ( GetMessage (&lpMsg, NULL, 0, 0) ) 
	{
		TranslateMessage (&lpMsg);
		DispatchMessage  (&lpMsg);    
       }
     	return (lpMsg.wParam);
}
int status=0;
//=== ‘”Õ ÷»ﬂ-Œ¡–¿¡Œ“◊»  —ŒŒ¡Ÿ≈Õ»… √À¿¬ÕŒ√Œ Œ Õ¿  ===
LRESULT CALLBACK  lcwnd(HWND hWnd, UINT  Mess, WPARAM  wParam, LPARAM lParam)
{	
	switch (Mess)
	{
		case WM_INITDIALOG:
				return TRUE;
		case WM_LBUTTONDOWN:
			if(!status){
				hwndgl=CreateWindow (szWindowStyle2, " ¿– ¿— œ–»ÀŒ∆≈Õ»ﬂ",
                                               WS_OVERLAPPEDWINDOW, CW_USEDEFAULT,
                                              CW_USEDEFAULT, CW_USEDEFAULT, 
                                               CW_USEDEFAULT, (HWND) hWnd,               
                                               ( HMENU )NULL, hInstg,  NULL);                                                                                                                                                                                     
				ShowWindow (hwndgl, Cmdshow);
				UpdateWindow (hwndgl);
				status++;
				return TRUE;}
				if(status%2!=0){
					ShowWindow(hwndgl,0);
				}
				if(status%2==0){
					ShowWindow(hwndgl,1);
				}
				status++;
				return TRUE;
			break;
		case WM_COMMAND:
			if (LOWORD(wParam) == IDOK) 
			{	
				//EnableWindow(hWnd,0);
				
				if(!status){
				hwndgl=CreateWindow (szWindowStyle2, " ¿– ¿— œ–»ÀŒ∆≈Õ»ﬂ",
                                               WS_OVERLAPPEDWINDOW, CW_USEDEFAULT,
                                              CW_USEDEFAULT, CW_USEDEFAULT, 
                                               CW_USEDEFAULT, (HWND) hWnd,               
                                               ( HMENU )NULL, hInstg,  NULL);                                                                                                                                                                                     
				ShowWindow (hwndgl, Cmdshow);
				UpdateWindow (hwndgl);
				status++;
				return TRUE;}
				if(status%2!=0){
					ShowWindow(hwndgl,0);
				}
				if(status%2==0){
					ShowWindow(hwndgl,1);
				}
				status++;
				return TRUE;
			}
			if(LOWORD(wParam) == IDCANCEL){
				PostQuitMessage(0);
				EndDialog(hWnd, LOWORD(wParam));
				return TRUE;
			}
			break;
	}
    return FALSE;
}
int count=0;

LRESULT CALLBACK  lcwnd2(HWND hWnd, UINT  Mess, WPARAM  wParam, LPARAM lParam)
{	
	HDC hdc;
	PAINTSTRUCT     ps;
	switch (Mess)
		{
	case WM_LBUTTONDOWN:
		count++;
		break;
	case WM_RBUTTONDOWN:
		InvalidateRect(hWnd,NULL,TRUE);
	     case WM_PAINT:  
		        hdc = BeginPaint (hWnd, &ps);            
                char lpszString[256];
				sprintf(lpszString,"%d",count);
					//< ‘–¿√Ã≈Õ“ œŒÀ‹«Œ¬¿“≈Àﬂ >
				TextOut(hdc,50,50,lpszString,strlen(lpszString));
		        ValidateRect (hWnd,NULL);
		        EndPaint (hWnd, &ps);
		       break;
                 //case  <  Ó‰—ÓÓ·˘ÂÌËˇ > :
		        //hdc = BeginPaint (hWnd, &ps);            
                          //< ‘–¿√Ã≈Õ“ œŒÀ‹«Œ¬¿“≈Àﬂ >
		        //ValidateRect (hWnd,NULL);
		        //EndPaint (hWnd, &ps);
		        //break;
		case WM_DESTROY:  
		         PostQuitMessage (0);
		         break;
		default: 
		         return DefWindowProc (hWnd, Mess, wParam, lParam); 
       }
   return  0;}

