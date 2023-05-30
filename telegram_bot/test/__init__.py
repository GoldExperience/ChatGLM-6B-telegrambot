import importlib.util
import sys
spec = importlib.util.spec_from_file_location("text_splitter", "telegram_bot/text_splitter/__init__.py")
text_splitter = importlib.util.module_from_spec(spec)
sys.modules["text_splitter"] = text_splitter
spec.loader.exec_module(text_splitter)

text_splitter.test()
duckduckgo.test()