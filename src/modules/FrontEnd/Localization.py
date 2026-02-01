import json, os, locale
from run_config import __ROOT__


class Localization:

    Folder: str = "Localization"
    DefaultLang = "en"

    @classmethod
    def _getSystemLang(cls):
        """Get system language code, e.g. 'zh_CN', 'zh_TW', 'en', 'ja'"""
        try:
            lang = locale.getdefaultlocale()[0]
            if lang:
                return lang
        except:
            pass
        return cls.DefaultLang

    @classmethod
    def GetJson(cls) -> json:
        location = os.path.join(os.path.curdir, cls.Folder)
        if not os.path.exists(location):
            location = os.path.join(__ROOT__, cls.Folder)

        # Try to use system language (e.g. zh_CN, zh_TW)
        system_lang = cls._getSystemLang()
        json_file = os.path.join(location, f"{system_lang}.json")

        # If specific locale file doesn't exist, try base language (e.g. zh.json for zh_CN)
        if not os.path.exists(json_file) and '_' in system_lang:
            base_lang = system_lang.split('_')[0]
            json_file = os.path.join(location, f"{base_lang}.json")

        # If system language file doesn't exist, use default en.json
        if not os.path.exists(json_file):
            json_file = os.path.join(location, f"{cls.DefaultLang}.json")

        with open(json_file, "r", encoding="utf-8") as file:
            return json.load(file)
