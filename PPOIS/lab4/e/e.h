// e.h : main header file for the E application
//

#if !defined(AFX_E_H__6D488070_6F05_451B_928A_4F6FC5EAC89D__INCLUDED_)
#define AFX_E_H__6D488070_6F05_451B_928A_4F6FC5EAC89D__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CEApp:
// See e.cpp for the implementation of this class
//

class CEApp : public CWinApp
{
public:
	CEApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CEApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation
	//{{AFX_MSG(CEApp)
	afx_msg void OnAppAbout();
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_E_H__6D488070_6F05_451B_928A_4F6FC5EAC89D__INCLUDED_)
