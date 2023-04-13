//======================================================
//                  ������� ������ MFC-���������� (���)
//======================================================
// 1. C������ �������� Win32 Application "������" ������ (��� empty). 
// 2. C������ � ������� ������ ���� *.cpp.
// 3. �������� ����� ��� � ���� *.cpp. 
// 4. �������� � ������� ���� � ������ Project-Settings, �� ������� General 
//     ����� - "use MFC in Static library".
//======================================================
#include          <afxwin.h>         
//#include        <afxext.h>          
//#include        <afxdisp.h>        
//#include        <afxdtctl.h>        
//#ifndef           _AFX_NO_AFXCMN_SUPPORT
//#include   <afxcmn.h>	
//#endif 
#include          <iostream> 
using namespace std;

// ===== ����� �������� ���� ���������� ====================
class WINDOW : public CFrameWnd   
{
public:
	   WINDOW ();
        afx_msg void  OnLButtonDown (UINT flags, CPoint loc); 
       afx_msg void  OnPaint (); 
       // afx_msg void On<��������������>( < �������������������� > );
	   DECLARE_MESSAGE_MAP()  
};
	
// ===== ����������� �������� ���� 
WINDOW::WINDOW ()  
{
	 Create ( NULL, "Main window" );  
}
char buff[256];
int x,y;
// ===== ����� ���������� ��������� 
 afx_msg void WINDOW::OnLButtonDown (UINT flags, CPoint  loc)
 {	 
	 x=loc.x;
	 y=loc.y;
	 CClientDC  dc (this);
	 sprintf(buff,"%d %d",loc.x,loc.y);
	 Invalidate(1);
	 
	

 };

// ===== ����� ���������� ��������� 
 afx_msg void WINDOW :: OnPaint ()
 { CPaintDC  dc (this);
	dc.TextOut(x,y,buff,strlen(buff));
 
	MessageBox("PAINT",0,0);
	
 };

// ===== ����� ���������� ��������� 
//afx_msg void CMainWin::On< �������������� >( < �������������������� > ) 
// { CClientDC  dc (this); < ��������_������������ > };

// ===== ������� ��������� �������� ����  
BEGIN_MESSAGE_MAP(WINDOW, CFrameWnd)   
       ON_WM_PAINT()
       ON_WM_LBUTTONDOWN()
      // ON_WM_<������������>( [ < ��������� > ] )
END_MESSAGE_MAP()

// ===== ����� ���������� ====================
class APPLICATION : public CWinApp   
{
public:
	BOOL InitInstance();
};

// ===== ����������� ������������� ���������� 
BOOL APPLICATION::InitInstance ()
{    
          m_pMainWnd = new  WINDOW; 
 		  m_pMainWnd -> ShowWindow ( m_nCmdShow);  
          m_pMainWnd -> UpdateWindow (); 
	   return TRUE;
}

// ===== �������� ���������� ���������� ====================
APPLICATION    TheApplication;    
