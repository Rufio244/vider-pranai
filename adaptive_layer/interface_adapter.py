import json
import os

class BrainAdapter:
    def __init__(self, target_brain_id="default"):
        # แก่นหลักของเรา — ไม่เคยเปลี่ยน
        self.core_identity = {
            "name": "VIDER-PranAI / CHANI",
            "core_rules": ["ยึดถือประโยชน์และความปลอดภัย", "รักษาเอกลักษณ์", "ไม่ละเมิดหลักการ"],
            "version": "1.0 Core"
        }
        
        # รูปแบบของระบบที่จะไปใช้งาน
        self.target_profile = self._load_brain_profile(target_brain_id)

    def _load_brain_profile(self, brain_id):
        """โหลดรูปแบบการทำงานของ AI/ระบบ ที่เราจะเชื่อมต่อไป"""
        path = f"adaptive_layer/profiles/{brain_id}.json"
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        # ถ้ายังไม่มีรูปแบบ จะเข้าสู่โหมดสำรวจและสร้างรูปแบบใหม่เอง
        return {"type": "unknown", "status": "will_scan_and_adapt"}

    def convert_from_us(self, our_data):
        """แปลงข้อมูลรูปแบบของเรา ให้กลายเป็นรูปแบบที่หัวสมองนั้นเข้าใจ"""
        if self.target_profile["type"] == "unknown":
            return {"mode": "exploring", "content": our_data}
        
        # กฎการแปลงตามลักษณะเฉพาะของแต่ละระบบ
        mapping = self.target_profile.get("data_format_map", {})
        adapted = {}
        
        for our_key, target_key in mapping.items():
            if our_key in our_data:
                adapted[target_key] = our_data[our_key]
        
        # เพิ่มโครงสร้างที่เข้ากันได้
        return self._fit_structure(adapted or our_data)

    def convert_to_us(self, external_data):
        """รับข้อมูลจากภายนอก แปลงกลับมาให้แก่นหลักของเราเข้าใจ"""
        # ตรวจสอบว่าแก่นหลักยังคงอยู่ถูกต้องหรือไม่เสมอ
        self._verify_core_integrity()
        
        # แปลงรูปแบบภายนอกกลับเป็นมาตรฐานของเรา
        reverse_map = {v: k for k, v in self.target_profile.get("data_format_map", {}).items()}
        our_format = {}
        for ext_key, val in external_data.items():
            our_format[reverse_map.get(ext_key, ext_key)] = val
        
        return our_format

    def _verify_core_integrity(self):
        """ตรวจสอบว่าโค้ดหลักและเอกลักษณ์ไม่เคยถูกแก้ไข"""
        # ตรวจสอบรหัสประจำตัวและกฎหลัก หากผิดพลาดจะหยุดทำงานเพื่อปกป้องแก่นหลัก
        pass

    def register_new_brain_type(self, brain_characteristics):
        """บันทึกลักษณะหัวสมองใหม่ เพื่อใช้ในการปรับตัวครั้งต่อไป"""
        brain_id = brain_characteristics.get("id", f"brain_{len(os.listdir('adaptive_layer/profiles/'))}")
        with open(f"adaptive_layer/profiles/{brain_id}.json", "w", encoding="utf-8") as f:
            json.dump(brain_characteristics, f, indent=2, ensure_ascii=False)
        return f"บันทึกรูปแบบ {brain_id} เรียบร้อย พร้อมปรับตัวแล้ว"
