import c4d
from c4d import gui
# Welcome to the world of Python


# Script state in the menu or the command palette
# Return True or c4d.CMD_ENABLED to enable, False or 0 to disable
# Alternatively return c4d.CMD_ENABLED|c4d.CMD_VALUE to enable and check/mark
#def state():
#    return True

# Main function
def main():
#    gui.MessageDialog('Hello World!')

    c4d.CallCommand(5160, 5160) # 球体
#    mydoc = c4d.documents.GetActiveDocument()
    sph = doc.GetFirstObject()
    sph[c4d.PRIM_SPHERE_RAD] = 15000
    sph.SetName("HFD") 


    comp = c4d.BaseTag(5637)
    sph.InsertTag(comp)
    comp[c4d.COMPOSITINGTAG_SEENBYCAMERA] = 0
    c4d.EventAdd()
    
# Execute main()
if __name__=='__main__':
    main()