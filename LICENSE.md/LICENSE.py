# Нода category
# Нода All Elemnts of Category
# Нода PythonScrit
# Тело script ниже

import clr
import sys

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
#Open File and Revit application
doc = DocumentManager.Instance.CurrentDBDocument
app = DocumentManager.Instance.CurrentUIApplication.Application

uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

elements = IN[0]


outList = []
familyType = []

for i in UnwrapElement(elements):
    p = i.LookupParameter("Огнестойкость") # имя параметра пистаь так, как в Revit
    TransactionManager.Instance.EnsureInTransaction(doc)
    p.Set("25") # значение параметра
    TransactionManager.Instance.TransactionTaskDone()
