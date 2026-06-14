# qvnt_basic.py
# Qvnt-SC 1.7.1 Basic - แกนหลัก VIDER PranAI
# คีย์เปิดใช้งาน: ViderPranAI244
VERSION = "1.7.1"
LEVEL = "Basic"
DEFAULT_ACTIVATION_KEY = "ViderPranAI244"  # ✅ คีย์หลักที่กำหนด

import json
import base64
from typing import Any, Dict

class QvntSCBasic:
    def __init__(self, key: str = DEFAULT_ACTIVATION_KEY):
        """เริ่มต้นระบบด้วยคีย์เปิดใช้งาน"""
        self.activation_key = key
        self.key_length = len(self.activation_key)
        self._validate_key()

    def _validate_key(self) -> None:
        """ตรวจสอบความถูกต้องของคีย์"""
        if self.activation_key != DEFAULT_ACTIVATION_KEY:
            raise PermissionError("❌ คีย์เปิดใช้งานไม่ถูกต้อง — ระบบไม่สามารถทำงานได้")
        print("✅ คีย์เปิดใช้งานถูกต้อง: VIDER PranAI พร้อมทำงาน")

    def _transform(self, char: str, offset: int, encrypt: bool = True) -> str:
        """ฟังก์ชันแปลงค่าพื้นฐาน"""
        key_code = ord(self.activation_key[offset % self.key_length])
        char_code = ord(char)
        if encrypt:
            return chr((char_code + key_code) % 65536)
        else:
            return chr((char_code - key_code) % 65536)

    def encode(self, data: Dict[str, Any]) -> str:
        """เข้ารหัสข้อมูลในรูปแบบ Qvnt"""
        json_str = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
        transformed = "".join(self._transform(c, i) for i, c in enumerate(json_str))
        return f"QVNT:{base64.urlsafe_b64encode(transformed.encode('utf-8')).decode('utf-8')}"

    def decode(self, qvnt_str: str) -> Dict[str, Any]:
        """ถอดรหัสข้อมูลกลับมาใช้งาน"""
        if not qvnt_str.startswith("QVNT:"):
            raise ValueError("❌ รูปแบบข้อมูล Qvnt ไม่ถูกต้อง")
        try:
            decoded_b64 = base64.urlsafe_b64decode(qvnt_str[5:]).decode("utf-8")
            original_str = "".join(self._transform(c, i, encrypt=False) for i, c in enumerate(decoded_b64))
            return json.loads(original_str)
        except Exception as e:
            raise ValueError(f"❌ ถอดรหัสไม่สำเร็จ: {str(e)}")

# ทดสอบการเปิดใช้งาน
if __name__ == "__main__":
    try:
        qvnt = QvntSCBasic()
        test_data = {"system": "VIDER PranAI", "status": "Active", "key": "ViderPranAI244"}
        enc = qvnt.encode(test_data)
        dec = qvnt.decode(enc)
        print(f"🔐 เข้ารหัสสำเร็จ: {enc[:60]}...")
        print(f"📖 ถอดรหัสได้ตรง: {dec == test_data}")
    except Exception as err:
        print(err)
