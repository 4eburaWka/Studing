//======================================================
//                  ТИПОВОЙ КАРКАС MFC-ПРИЛОЖЕНИЯ (ТКП)
//======================================================
// 1. Cоздать мастером Win32 Application "пустой" каркас (тип empty). 
// 2. Cоздать в каркасе пустой файл *.cpp.
// 3. Вставить текст ТКП в файл *.cpp. 
// 4. Включить в главном меню в пункте Project-Settings, на вкладке General 
//     режим - "use MFC in Static library".
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

// ===== класс главного ОКНА приложения ====================
class WINDOW : public CFrameWnd   
{
public:
	   WINDOW ();
        afx_msg void  OnLButtonDown (UINT flags, CPoint loc); 
       afx_msg void  OnPaint (); 
       // afx_msg void On<ИмяОбработчика>( < ПараметрыОбработчика > );
	   DECLARE_MESSAGE_MAP()  
};
	
// ===== конструктор Создание окна 
WINDOW::WINDOW ()  
{
	 Create ( NULL, "Main window" );  
}
char buff[256];
int x,y;
// ===== метод Обработчик сообщения 
 afx_msg void WINDOW::OnLButtonDown (UINT flags, CPoint  loc)
 {	 
	 x=loc.x;
	 y=loc.y;
	 CClientDC  dc (this);
	 sprintf(buff,"%d %d",loc.x,loc.y);
	 Invalidate(1);
	 
	

 };

// ===== метод Обработчик сообщения 
 afx_msg void WINDOW :: OnPaint ()
 { CPaintDC  dc (this);
	dc.TextOut(x,y,buff,strlen(buff));
 
	MessageBox("PAINT",0,0);
	
 };

// ===== метод Обработчик сообщения 
//afx_msg void CMainWin::On< ИмяОбработчика >( < ПараметрыОбработчика > ) 
// { CClientDC  dc (this); < ФРАГМЕНТ_ПОЛЬЗОВАТЕЛЯ > };

// ===== очередь сообщений главного окна  
BEGIN_MESSAGE_MAP(WINDOW, CFrameWnd)   
       ON_WM_PAINT()
       ON_WM_LBUTTONDOWN()
      // ON_WM_<ИмяСообщения>( [ < Параметры > ] )
END_MESSAGE_MAP()

// ===== класс ПРИЛОЖЕНИЕ ====================
class APPLICATION : public CWinApp   
{
public:
	BOOL InitInstance();
};

// ===== конструктор Инициализация приложения 
BOOL APPLICATION::InitInstance ()
{    
          m_pMainWnd = new  WINDOW; 
 		  m_pMainWnd -> ShowWindow ( m_nCmdShow);  
          m_pMainWnd -> UpdateWindow (); 
	   return TRUE;
}

// ===== создание экземпляра приложения ====================
APPLICATION    TheApplication;    
