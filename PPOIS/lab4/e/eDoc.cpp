// eDoc.cpp : implementation of the CEDoc class
//

#include "stdafx.h"
#include "e.h"

#include "eDoc.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CEDoc

IMPLEMENT_DYNCREATE(CEDoc, CDocument)

BEGIN_MESSAGE_MAP(CEDoc, CDocument)
	//{{AFX_MSG_MAP(CEDoc)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CEDoc construction/destruction

CEDoc::CEDoc()
{
	// TODO: add one-time construction code here

}

CEDoc::~CEDoc()
{
}

BOOL CEDoc::OnNewDocument()
{
	if (!CDocument::OnNewDocument())
		return FALSE;

	// TODO: add reinitialization code here
	// (SDI documents will reuse this document)

	return TRUE;
}



/////////////////////////////////////////////////////////////////////////////
// CEDoc serialization

void CEDoc::Serialize(CArchive& ar)
{
	if (ar.IsStoring())
	{
		// TODO: add storing code here
	}
	else
	{
		// TODO: add loading code here
	}
}

/////////////////////////////////////////////////////////////////////////////
// CEDoc diagnostics

#ifdef _DEBUG
void CEDoc::AssertValid() const
{
	CDocument::AssertValid();
}

void CEDoc::Dump(CDumpContext& dc) const
{
	CDocument::Dump(dc);
}
#endif //_DEBUG

/////////////////////////////////////////////////////////////////////////////
// CEDoc commands
