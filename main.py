# main.py
from pranai_core import PranAICore
from pranai_inventor import PranAIInventor
from pranai_evaluator import PranAIEvaluator

def main():
    print("=" * 60)
    print("🚀 VIDER PranAI v1.0")
    print("🔍 ค้นหา วิเคราะห์ ประดิษฐ์ และพิสูจน์เทคโนโลยี")
    print("⚙️  ใช้แกนหลัก Qvnt‑SC 1.7.1 Basic")
    print("=" * 60)

    # เริ่มระบบ
    core = PranAICore()
    inventor = PranAIInventor(core)

    # ตัวอย่างการใช้งาน
    query = "ระบบกักเก็บพลังงานที่มีประสิทธิภาพสูง"
    result = inventor.invent_technology(query)

    # แสดงผล
    print("\n📜 ผลการประดิษฐ์และตรวจสอบ:")
    for k, v in result.items():
        print(f"{k}: {v}")

    # ประเมินอีกครั้ง
    eval_res = PranAIEvaluator.evaluate_result(result["expected_efficiency"])
    print(f"\n📊 ผลการประเมิน: {eval_res}")

if __name__ == "__main__":
    main()

