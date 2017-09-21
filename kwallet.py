# I just wanted to find a simple way to store credentials in KWallet, and fetch it from
# a command line application. Here's how (assumes the credentials are already set):

def getCredentials():
    from PyKDE5.kdeui import KWallet
    from PyQt4 import QtGui
    from PyQt4 import QtCore

    app = QtGui.QApplication([])
    wallet = KWallet.Wallet.openWallet(KWallet.Wallet.LocalWallet(), 0)
    if not wallet.hasFolder("myapp"):
        wallet.createFolder("myapp")
    wallet.setFolder("myapp")
    key, quname = wallet.readPassword('username')
    key, qpass = wallet.readPassword('password')

    return str(quname), str(qpass)