# pranai_core.py
from qvnt_basic import QvntSCBasic
from typing import Dict, List

class PranAICore:
    def __init__(self):
        self.qvnt = QvntSCBasic()  # ใช้คีย์ ViderPranAI244 อัตโนมัติ
        self.knowledge_base: Dict[str, str] = {}
        self.system_name = "VIDER PranAI"
        self.version = "v1.0.0"
