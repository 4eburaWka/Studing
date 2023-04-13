#include    <afxwin.h>         
//#include  <afxext.h>          
//#include  <afxdisp.h>        
//#include  <afxdtctl.h>        
//#ifndef   _AFX_NO_AFXCMN_SUPPORT
//#include  <afxcmn.h>	
//#endif   // _AFX_NO_AFXCMN_SUPPORT
#include  <iostream> 
using namespace std;

// ===== класс главного ОКНА приложения ====================
class WINDOW : public CFrameWnd   
{
public:
     // Конструктор окна
	   WINDOW ();
      // Прототип обработчика сообщения WM_LBUTTONDOWN
  	 // afx_msg void  OnLButtonDown (UINT flags, CPoint loc); 
      // Макрос объявления очереди сообщений окна
	    DECLARE_MESSAGE_MAP()  
};

// ===== конструктор окна - Создание окна 
WINDOW:: WINDOW ()  
{
	 Create ( NULL,   // имя стиля окна 
                           "Главное окно MFC-приложения",  // заголовок окна
                         // DWORD Style = WS_OVERLAPPEDWINDOW,  // стиль окна 
                         // const RECT &XYsize =  rectDefault,  // положение и размеры окна
                         // CWnd *Parent = NULL,  // окно-предок
                         // LPCSTR MenuName = NULL,  // имя главного меню
                         // DWORD ExStyle = 0,  // спецификатор расширенного стиля
                         // CCreateContext  * Context  = NULL);  // дополнительная информация 
}

// ===== метод Обработчик сообщения 
//            нажата левая клавиша "мыши"  WM_LBUTTONDOWN 
// afx_msg void WINDOW::OnLButtonDown (UINT flags, CPoint loc)
//  { < ФРАГМЕНТ_ПОЛЬЗОВАТЕЛЯ > };

// ===== очередь сообщений главного окна  
BEGIN_MESSAGE_MAP(WINDOW, CFrameWnd)   
       // Макрокоманды включения обрабатываемых сообщений 
       // ON_WM_LBUTTONDOWN()
       //  …………….
END_MESSAGE_MAP()

// ===== класс ПРИЛОЖЕНИЕ ====================
class APPLICATION : public CWinApp   
{
public:
    // Конструктор приложения
	  BOOL InitInstance();
};

// ===== конструктор приложения - Инициализации приложения 
BOOL APPLICATION::InitInstance ()
{    
       // Создание объекта класса WINDOW 
          m_pMainWnd = new  WINDOW; 
       // Визуализация окна в заданном при запуске приложения стиле m_nCmdShow
	     m_pMainWnd -> ShowWindow ( m_nCmdShow );  
       // Посылка сообщения о необходимости обновить содержимое окна
          m_pMainWnd -> UpdateWindow (); 
	     return TRUE;
}

// ===== создание и запуск экземпляра приложения ====================
APPLICATION    TheApplication;


