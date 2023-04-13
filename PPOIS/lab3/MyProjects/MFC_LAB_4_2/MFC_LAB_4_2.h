// MFC_LAB_4_2.h : main header file for the MFC_LAB_4_2 application
//

#if !defined(AFX_MFC_LAB_4_2_H__67A91CC2_20D5_4100_995C_41D35AF74439__INCLUDED_)
#define AFX_MFC_LAB_4_2_H__67A91CC2_20D5_4100_995C_41D35AF74439__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"       // main symbols

/////////////////////////////////////////////////////////////////////////////
// CMFC_LAB_4_2App:
// See MFC_LAB_4_2.cpp for the implementation of this class
//

class CMFC_LAB_4_2App : public CWinApp
{
public:
	CMFC_LAB_4_2App();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CMFC_LAB_4_2App)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

public:
	//{{AFX_MSG(CMFC_LAB_4_2App)
	afx_msg void OnAppAbout();
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MFC_LAB_4_2_H__67A91CC2_20D5_4100_995C_41D35AF74439__INCLUDED_)
