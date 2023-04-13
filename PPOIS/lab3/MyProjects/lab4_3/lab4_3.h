// lab4_3.h : main header file for the LAB4_3 application
//

#if !defined(AFX_LAB4_3_H__81656487_0E6D_4C05_BBA8_2AC39045C14D__INCLUDED_)
#define AFX_LAB4_3_H__81656487_0E6D_4C05_BBA8_2AC39045C14D__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CLab4_3App:
// See lab4_3.cpp for the implementation of this class
//

class CLab4_3App : public CWinApp
{
public:
	CLab4_3App();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CLab4_3App)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

public:
	//{{AFX_MSG(CLab4_3App)
	afx_msg void OnAppAbout();
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_LAB4_3_H__81656487_0E6D_4C05_BBA8_2AC39045C14D__INCLUDED_)
