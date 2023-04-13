// 4_10_1.h : main header file for the 4_10_1 application
//

#if !defined(AFX_4_10_1_H__E0D1380A_5155_4CB0_8834_5ADEC215E5C5__INCLUDED_)
#define AFX_4_10_1_H__E0D1380A_5155_4CB0_8834_5ADEC215E5C5__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CMy4_10_1App:
// See 4_10_1.cpp for the implementation of this class
//

class CMy4_10_1App : public CWinApp
{
public:
	CMy4_10_1App();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMy4_10_1App)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

public:
	//{{AFX_MSG(CMy4_10_1App)
	afx_msg void OnAppAbout();
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_4_10_1_H__E0D1380A_5155_4CB0_8834_5ADEC215E5C5__INCLUDED_)
