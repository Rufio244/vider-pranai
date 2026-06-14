# pranai_core.py
from qvnt_basic import QvntSCBasic
from typing import Dict, List

class PranAICore:
    def __init__(self):
        self.qvnt = QvntSCBasic()
        self.knowledge_base: Dict[str, str] = {}  # เก็บในรูปแบบ Qvnt
        self.version = "PranAI v1.0"

    def search_and_collect(self, query: str) -> Dict[str, Any]:
        """ค้นหาและรวบรวมข้อมูลที่เกี่ยวข้องจากทุกแหล่ง
        *สำหรับ GitHub: สามารถเชื่อมต่อ API สาธารณะเพิ่มเติมได้เอง*
        """
        print(f"🔍 ค้นหา: {query}")
        # จำลองการรวบรวมความรู้พื้นฐาน
        collected = {
            "query": query,
            "sources": ["Global Knowledge Base", "Scientific Papers", "Open Tech"],
            "summary": f"ข้อมูลพื้นฐานและหลักการเกี่ยวกับ {query}",
            "principles": ["กฎทางฟิสิกส์", "หลักวิศวกรรม", "ตรรกะทางคณิตศาสตร์"]
        }
        # บันทึกลงฐานข้อมูล
        encoded = self.qvnt.encode(collected)
        self.knowledge_base[query] = encoded
        return collected

    def get_knowledge(self, topic: str) -> Dict[str, Any]:
        """เรียกข้อมูลที่เก็บไว้"""
        if topic not in self.knowledge_base:
            return {"error": "ไม่พบข้อมูล กรุณาค้นหาก่อน"}
        return self.qvnt.decode(self.knowledge_base[topic])

