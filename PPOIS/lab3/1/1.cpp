#include    <afxwin.h>         
//#include  <afxext.h>          
//#include  <afxdisp.h>        
//#include  <afxdtctl.h>        
//#ifndef   _AFX_NO_AFXCMN_SUPPORT
//#include  <afxcmn.h>	
//#endif   // _AFX_NO_AFXCMN_SUPPORT
#include  <iostream> 
using namespace std;

// ===== ����� �������� ���� ���������� ====================
class WINDOW : public CFrameWnd   
{
public:
     // ����������� ����
	   WINDOW ();
      // �������� ����������� ��������� WM_LBUTTONDOWN
  	 // afx_msg void  OnLButtonDown (UINT flags, CPoint loc); 
      // ������ ���������� ������� ��������� ����
	    DECLARE_MESSAGE_MAP()  
};

// ===== ����������� ���� - �������� ���� 
WINDOW:: WINDOW ()  
{
	 Create ( NULL,   // ��� ����� ���� 
                           "������� ���� MFC-����������",  // ��������� ����
                         // DWORD Style = WS_OVERLAPPEDWINDOW,  // ����� ���� 
                         // const RECT &XYsize =  rectDefault,  // ��������� � ������� ����
                         // CWnd *Parent = NULL,  // ����-������
                         // LPCSTR MenuName = NULL,  // ��� �������� ����
                         // DWORD ExStyle = 0,  // ������������ ������������ �����
                         // CCreateContext  * Context  = NULL);  // �������������� ���������� 
}

// ===== ����� ���������� ��������� 
//            ������ ����� ������� "����"  WM_LBUTTONDOWN 
// afx_msg void WINDOW::OnLButtonDown (UINT flags, CPoint loc)
//  { < ��������_������������ > };

// ===== ������� ��������� �������� ����  
BEGIN_MESSAGE_MAP(WINDOW, CFrameWnd)   
       // ������������ ��������� �������������� ��������� 
       // ON_WM_LBUTTONDOWN()
       //  �����.
END_MESSAGE_MAP()

// ===== ����� ���������� ====================
class APPLICATION : public CWinApp   
{
public:
    // ����������� ����������
	  BOOL InitInstance();
};

// ===== ����������� ���������� - ������������� ���������� 
BOOL APPLICATION::InitInstance ()
{    
       // �������� ������� ������ WINDOW 
          m_pMainWnd = new  WINDOW; 
       // ������������ ���� � �������� ��� ������� ���������� ����� m_nCmdShow
	     m_pMainWnd -> ShowWindow ( m_nCmdShow );  
       // ������� ��������� � ������������� �������� ���������� ����
          m_pMainWnd -> UpdateWindow (); 
	     return TRUE;
}

// ===== �������� � ������ ���������� ���������� ====================
APPLICATION    TheApplication;


