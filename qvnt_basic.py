# qvnt_basic.py
# Qvnt-SC 1.7.1 Basic - แกนพื้นฐานสำหรับ VIDER PranAI
VERSION = "1.7.1"
LEVEL = "Basic"

import json
import base64
from typing import Any, Dict

class QvntSCBasic:
    def __init__(self, key: str = "VIDER-PRANAI-2026"):
        self.key = key
        self.key_len = len(key)

    def _simple_transform(self, char: str, offset: int) -> str:
        """แปลงตัวอักษรแบบเบา รวดเร็ว ปลอดภัยพื้นฐาน"""
        return chr((ord(char) + ord(self.key[offset % self.key_len])) % 65536)

    def _reverse_transform(self, char: str, offset: int) -> str:
        """แปลงกลับ"""
        return chr((ord(char) - ord(self.key[offset % self.key_len])) % 65536)

    def encode(self, data: Dict[str, Any]) -> str:
        """เข้ารหัสข้อมูลให้อยู่ในรูปแบบ Qvnt"""
        json_str = json.dumps(data, ensure_ascii=False)
        transformed = "".join(self._simple_transform(c, i) for i, c in enumerate(json_str))
        return "QVNT:" + base64.urlsafe_b64encode(transformed.encode("utf-8")).decode("utf-8")

    def decode(self, qvnt_str: str) -> Dict[str, Any]:
        """ถอดรหัสกลับมาใช้งาน"""
        if not qvnt_str.startswith("QVNT:"):
            raise ValueError("รูปแบบ Qvnt ไม่ถูกต้อง")
        try:
            decoded_b64 = base64.urlsafe_b64decode(qvnt_str[5:]).decode("utf-8")
            original = "".join(self._reverse_transform(c, i) for i, c in enumerate(decoded_b64))
            return json.loads(original)
        except Exception as e:
            raise ValueError(f"ถอดรหัสไม่สำเร็จ: {e}")

# ทดสอบการทำงาน
if __name__ == "__main__":
    qvnt = QvntSCBasic()
    data = {"name": "VIDER PranAI", "type": "Search & Invent Engine"}
    enc = qvnt.encode(data)
    dec = qvnt.decode(enc)
    print(f"✅ เข้ารหัส: {enc[:50]}...")
    print(f"✅ ถอดรหัส: {dec}")

