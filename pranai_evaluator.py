# pranai_evaluator.py
class PranAIEvaluator:
    @staticmethod
    def evaluate_result(metric: float, base: float = 1.0) -> Dict[str, Any]:
        """ประเมินผลลัพธ์ตามกฎผลบวกเท่านั้น"""
        change = ((metric - base) / base) * 100
        status = "APPROVED" if change >= 0.01 else "REJECTED"
        return {
            "change_percent": round(change, 4),
            "status": status,
            "note": "ยอมรับเป็นส่วนหนึ่งของ VIDER PranAI" if status == "APPROVED" else "ไม่สอดคล้องกับหลักการพัฒนา"
        }

