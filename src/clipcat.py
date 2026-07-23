import sys
import argparse
import ctypes
CF_UNICODETEXT = 13
User32 = ctypes.WinDLL("user32", use_last_error=True)
Kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
User32.OpenClipboard.argtypes = [ctypes.c_void_p]
User32.OpenClipboard.restype = ctypes.c_bool
User32.GetClipboardData.argtypes = [ctypes.c_uint]
User32.GetClipboardData.restype = ctypes.c_void_p
Kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
Kernel32.GlobalLock.restype = ctypes.c_void_p
Kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
Kernel32.GlobalUnlock.restype = ctypes.c_bool
def getClipboard():
	if not User32.OpenClipboard(None):
		ErrorCode = ctypes.get_last_error()
		raise RuntimeError(f"[WinError: {ErrorCode}] Unable to open clipboard.")
	try:
		Handle = User32.GetClipboardData(CF_UNICODETEXT)
		if not Handle:
			raise RuntimeError("Clipboard does not contain text.")
		Pointer = Kernel32.GlobalLock(Handle)
		if not Pointer:
			ErrorCode = ctypes.get_last_error()
			raise RuntimeError(f"[WinError: {ErrorCode}] Unable to lock clipboard data.")
		try:
			return ctypes.wstring_at(Pointer)
		finally:
			Kernel32.GlobalUnlock(Handle)
	finally:
		User32.CloseClipboard()
def printClipboard():
	try:
		Clipboard_Text = getClipboard()
	except RuntimeError as Error:
		sys.stderr.write(f"{Error}\n")
		return 2
	if not Clipboard_Text.strip():
		sys.stderr.write("Clipboard is empty\n")
		return 1
	sys.stdout.write(Clipboard_Text)
	return 0
def parseArgs():
	Parser = argparse.ArgumentParser(prog="Clipcat", description="Print your clipboard content to the standard output.", allow_abbrev=False)
	Parser.add_argument("-v", "--version", action="version", version="Clipcat version 1.0")
	return Parser.parse_args()
def main():
	parseArgs()
	sys.exit(printClipboard())
if __name__ == "__main__":
	main()